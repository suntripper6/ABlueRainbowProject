using System.IdentityModel.Tokens.Jwt;
using System.Security.Claims;
using System.Text;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Services;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Microsoft.IdentityModel.Tokens;

namespace ABlueRainbowBackend.Controllers;

[Route("api/auth")]
[ApiController]
public class AuthController : ControllerBase
{
    private readonly IConfiguration _configuration;
    private readonly ApplicationDbContext _context;
    private readonly IPasswordHasher<AdminUser> _passwordHasher;
    private readonly IAdminAuditLogger _auditLogger;

    public AuthController(
        IConfiguration configuration,
        ApplicationDbContext context,
        IPasswordHasher<AdminUser> passwordHasher,
        IAdminAuditLogger auditLogger)
    {
        _configuration = configuration;
        _context = context;
        _passwordHasher = passwordHasher;
        _auditLogger = auditLogger;
    }

    [AllowAnonymous]
    [HttpPost("login")]
    public async Task<ActionResult<LoginResponse>> Login(LoginRequest request)
    {
        var issuer = _configuration["Authentication:JwtIssuer"] ?? "ABlueRainbowBackend";
        var audience = _configuration["Authentication:JwtAudience"] ?? "ABlueRainbowFrontend";
        var signingKey = _configuration["Authentication:JwtSigningKey"];
        var expiresMinutes = int.TryParse(_configuration["Authentication:TokenExpiresMinutes"], out var parsedMinutes)
            ? parsedMinutes
            : 120;

        if (string.IsNullOrWhiteSpace(signingKey))
        {
            return Problem("Authentication is not configured.", statusCode: StatusCodes.Status500InternalServerError);
        }

        var adminUser = await _context.AdminUsers
            .AsNoTracking()
            .SingleOrDefaultAsync(user => user.Username == request.Username && user.IsActive);

        if (adminUser == null)
        {
            return Unauthorized(new { message = "Invalid credentials." });
        }

        var passwordVerification = _passwordHasher.VerifyHashedPassword(adminUser, adminUser.PasswordHash, request.Password);
        if (passwordVerification == PasswordVerificationResult.Failed)
        {
            return Unauthorized(new { message = "Invalid credentials." });
        }

        var expiresAt = DateTimeOffset.UtcNow.AddMinutes(expiresMinutes);
        var credentials = new SigningCredentials(
            new SymmetricSecurityKey(Encoding.UTF8.GetBytes(signingKey)),
            SecurityAlgorithms.HmacSha256);

        var token = new JwtSecurityToken(
            issuer: issuer,
            audience: audience,
            claims:
            [
                new Claim(ClaimTypes.NameIdentifier, adminUser.Id.ToString()),
                new Claim(ClaimTypes.Name, adminUser.Username),
                new Claim(ClaimTypes.Role, "Admin"),
            ],
            expires: expiresAt.UtcDateTime,
            signingCredentials: credentials);

        await _auditLogger.LogAsync(
            HttpContext,
            "admin_user.login",
            "AdminUser",
            adminUser.Id.ToString(),
            $"Admin user '{adminUser.Username}' signed in.",
            metadata: new { adminUser.Username },
            actorAdminUserIdOverride: adminUser.Id,
            actorUsernameOverride: adminUser.Username);

        return Ok(new LoginResponse
        {
            Token = new JwtSecurityTokenHandler().WriteToken(token),
            Username = adminUser.Username,
            ExpiresAt = expiresAt,
        });
    }
}