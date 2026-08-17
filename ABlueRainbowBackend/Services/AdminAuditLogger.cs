using System.Security.Claims;
using System.Text.Json;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;

namespace ABlueRainbowBackend.Services;

public interface IAdminAuditLogger
{
    Task LogAsync(
        HttpContext httpContext,
        string actionType,
        string entityType,
        string entityId,
        string description,
        object? metadata = null,
        int? actorAdminUserIdOverride = null,
        string? actorUsernameOverride = null);
}

public sealed class AdminAuditLogger : IAdminAuditLogger
{
    private readonly ApplicationDbContext _context;

    public AdminAuditLogger(ApplicationDbContext context)
    {
        _context = context;
    }

    public async Task LogAsync(
        HttpContext httpContext,
        string actionType,
        string entityType,
        string entityId,
        string description,
        object? metadata = null,
        int? actorAdminUserIdOverride = null,
        string? actorUsernameOverride = null)
    {
        var actorId = actorAdminUserIdOverride;
        if (!actorId.HasValue && int.TryParse(httpContext.User.FindFirstValue(ClaimTypes.NameIdentifier), out var parsedActorId))
        {
            actorId = parsedActorId;
        }

        var actorUsername = actorUsernameOverride
            ?? httpContext.User.FindFirstValue(ClaimTypes.Name)
            ?? "unknown";

        var auditLog = new AdminAuditLog
        {
            ActorAdminUserId = actorId,
            ActorUsername = actorUsername,
            ActionType = actionType,
            EntityType = entityType,
            EntityId = entityId,
            Description = description,
            MetadataJson = metadata == null ? null : JsonSerializer.Serialize(metadata),
            IpAddress = httpContext.Connection.RemoteIpAddress?.ToString(),
            UserAgent = httpContext.Request.Headers.UserAgent.ToString(),
            OccurredAtUtc = DateTimeOffset.UtcNow,
        };

        _context.AdminAuditLogs.Add(auditLog);
        await _context.SaveChangesAsync();
    }
}