using System.Security.Claims;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Services;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Identity;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ABlueRainbowBackend.Controllers;

[Route("api/admin/users")]
[ApiController]
[Authorize(Policy = "AdminOnly")]
public class AdminUsersController : ControllerBase
{
    private readonly ApplicationDbContext _context;
    private readonly IPasswordHasher<AdminUser> _passwordHasher;
    private readonly IAdminAuditLogger _auditLogger;

    public AdminUsersController(ApplicationDbContext context, IPasswordHasher<AdminUser> passwordHasher, IAdminAuditLogger auditLogger)
    {
        _context = context;
        _passwordHasher = passwordHasher;
        _auditLogger = auditLogger;
    }

    [HttpGet]
    public async Task<ActionResult<IEnumerable<AdminUserSummaryResponse>>> GetAdminUsers()
    {
        var users = await _context.AdminUsers
            .AsNoTracking()
            .OrderBy(user => user.Username)
            .Select(user => ToSummary(user))
            .ToListAsync();

        return users;
    }

    [HttpGet("{id}")]
    public async Task<ActionResult<AdminUserSummaryResponse>> GetAdminUser(int id)
    {
        var user = await _context.AdminUsers.AsNoTracking().SingleOrDefaultAsync(adminUser => adminUser.Id == id);
        return user == null ? NotFound() : ToSummary(user);
    }

    [HttpPost]
    public async Task<ActionResult<AdminUserSummaryResponse>> CreateAdminUser(CreateAdminUserRequest request)
    {
        if (string.IsNullOrWhiteSpace(request.Username)
            || string.IsNullOrWhiteSpace(request.DisplayName)
            || string.IsNullOrWhiteSpace(request.Password))
        {
            return BadRequest(new { message = "Username, display name, and password are required." });
        }

        if (request.Password.Length < 8)
        {
            return BadRequest(new { message = "Password must be at least 8 characters long." });
        }

        var normalizedUsername = request.Username.Trim();
        var exists = await _context.AdminUsers.AnyAsync(user => user.Username == normalizedUsername);
        if (exists)
        {
            return Conflict(new { message = "An admin with that username already exists." });
        }

        var adminUser = new AdminUser
        {
            Username = normalizedUsername,
            DisplayName = request.DisplayName.Trim(),
            IsActive = true,
            CreatedAtUtc = DateTimeOffset.UtcNow,
        };

        adminUser.PasswordHash = _passwordHasher.HashPassword(adminUser, request.Password);

        _context.AdminUsers.Add(adminUser);
        await _context.SaveChangesAsync();

        await _auditLogger.LogAsync(
            HttpContext,
            "admin_user.created",
            "AdminUser",
            adminUser.Id.ToString(),
            $"Created admin user '{adminUser.Username}'.",
            metadata: new { adminUser.Username, adminUser.DisplayName });

        return CreatedAtAction(nameof(GetAdminUser), new { id = adminUser.Id }, ToSummary(adminUser));
    }

    [HttpPut("{id}")]
    public async Task<ActionResult<AdminUserSummaryResponse>> UpdateAdminUser(int id, UpdateAdminUserRequest request)
    {
        var adminUser = await _context.AdminUsers.SingleOrDefaultAsync(user => user.Id == id);
        if (adminUser == null)
        {
            return NotFound();
        }

        if (string.IsNullOrWhiteSpace(request.DisplayName))
        {
            return BadRequest(new { message = "Display name is required." });
        }

        var currentUserId = User.FindFirstValue(ClaimTypes.NameIdentifier);
        if (!request.IsActive && currentUserId == adminUser.Id.ToString())
        {
            return BadRequest(new { message = "You cannot deactivate the account you are currently using." });
        }

        if (!request.IsActive && adminUser.IsActive)
        {
            var activeAdminCount = await _context.AdminUsers.CountAsync(user => user.IsActive);
            if (activeAdminCount <= 1)
            {
                return BadRequest(new { message = "At least one active admin account must remain." });
            }
        }

        var previousDisplayName = adminUser.DisplayName;
        var previousIsActive = adminUser.IsActive;
        adminUser.DisplayName = request.DisplayName.Trim();
        adminUser.IsActive = request.IsActive;
        await _context.SaveChangesAsync();

        await _auditLogger.LogAsync(
            HttpContext,
            "admin_user.updated",
            "AdminUser",
            adminUser.Id.ToString(),
            $"Updated admin user '{adminUser.Username}'.",
            metadata: new
            {
                previousDisplayName,
                adminUser.DisplayName,
                previousIsActive,
                adminUser.IsActive,
            });

        return Ok(ToSummary(adminUser));
    }

    [HttpPut("{id}/password")]
    public async Task<IActionResult> RotateAdminUserPassword(int id, RotateAdminUserPasswordRequest request)
    {
        var adminUser = await _context.AdminUsers.SingleOrDefaultAsync(user => user.Id == id);
        if (adminUser == null)
        {
            return NotFound();
        }

        if (string.IsNullOrWhiteSpace(request.Password) || request.Password.Length < 8)
        {
            return BadRequest(new { message = "Password must be at least 8 characters long." });
        }

        adminUser.PasswordHash = _passwordHasher.HashPassword(adminUser, request.Password);
        await _context.SaveChangesAsync();

        await _auditLogger.LogAsync(
            HttpContext,
            "admin_user.password_rotated",
            "AdminUser",
            adminUser.Id.ToString(),
            $"Rotated password for admin user '{adminUser.Username}'.",
            metadata: new { adminUser.Username });

        return NoContent();
    }

    private static AdminUserSummaryResponse ToSummary(AdminUser user)
    {
        return new AdminUserSummaryResponse
        {
            Id = user.Id,
            Username = user.Username,
            DisplayName = user.DisplayName,
            IsActive = user.IsActive,
            CreatedAtUtc = user.CreatedAtUtc,
        };
    }
}