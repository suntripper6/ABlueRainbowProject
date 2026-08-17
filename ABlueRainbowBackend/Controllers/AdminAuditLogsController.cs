using System.Text;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;

namespace ABlueRainbowBackend.Controllers;

[Route("api/admin/audit-logs")]
[ApiController]
[Authorize(Policy = "AdminOnly")]
public class AdminAuditLogsController : ControllerBase
{
    private readonly ApplicationDbContext _context;

    public AdminAuditLogsController(ApplicationDbContext context)
    {
        _context = context;
    }

    [HttpGet]
    public async Task<IActionResult> GetAuditLogs(
        [FromQuery] int take = 100,
        [FromQuery] string? actor_username = null,
        [FromQuery] string? action_type = null,
        [FromQuery] DateTimeOffset? occurred_after_utc = null,
        [FromQuery] DateTimeOffset? occurred_before_utc = null,
        [FromQuery] string? format = null)
    {
        take = Math.Clamp(take, 1, 250);

        var query = _context.AdminAuditLogs.AsNoTracking().AsQueryable();

        if (!string.IsNullOrWhiteSpace(actor_username))
        {
            var actorFilter = actor_username.Trim().ToLower();
            query = query.Where(log => log.ActorUsername.ToLower().Contains(actorFilter));
        }

        if (!string.IsNullOrWhiteSpace(action_type))
        {
            var actionFilter = action_type.Trim().ToLower();
            query = query.Where(log => log.ActionType.ToLower() == actionFilter);
        }

        if (occurred_after_utc.HasValue)
        {
            query = query.Where(log => log.OccurredAtUtc >= occurred_after_utc.Value);
        }

        if (occurred_before_utc.HasValue)
        {
            query = query.Where(log => log.OccurredAtUtc <= occurred_before_utc.Value);
        }

        var logs = await query
            .OrderByDescending(log => log.OccurredAtUtc)
            .Take(take)
            .Select(log => new AdminAuditLogResponse
            {
                Id = log.Id,
                ActorAdminUserId = log.ActorAdminUserId,
                ActorUsername = log.ActorUsername,
                ActionType = log.ActionType,
                EntityType = log.EntityType,
                EntityId = log.EntityId,
                Description = log.Description,
                MetadataJson = log.MetadataJson,
                IpAddress = log.IpAddress,
                UserAgent = log.UserAgent,
                OccurredAtUtc = log.OccurredAtUtc,
            })
            .ToListAsync();

        if (string.Equals(format, "csv", StringComparison.OrdinalIgnoreCase))
        {
            var csvBytes = Encoding.UTF8.GetBytes(BuildCsv(logs));
            return File(csvBytes, "text/csv", $"admin-audit-logs-{DateTime.UtcNow:yyyyMMddHHmmss}.csv");
        }

        return Ok(logs);
    }

    private static string BuildCsv(IEnumerable<AdminAuditLogResponse> logs)
    {
        var lines = new List<string>
        {
            "id,actor_admin_user_id,actor_username,action_type,entity_type,entity_id,description,metadata_json,ip_address,user_agent,occurred_at_utc"
        };

        lines.AddRange(logs.Select(log => string.Join(',',
            EscapeCsv(log.Id),
            EscapeCsv(log.ActorAdminUserId),
            EscapeCsv(log.ActorUsername),
            EscapeCsv(log.ActionType),
            EscapeCsv(log.EntityType),
            EscapeCsv(log.EntityId),
            EscapeCsv(log.Description),
            EscapeCsv(log.MetadataJson),
            EscapeCsv(log.IpAddress),
            EscapeCsv(log.UserAgent),
            EscapeCsv(log.OccurredAtUtc.UtcDateTime.ToString("O")))));

        return string.Join(Environment.NewLine, lines);
    }

    private static string EscapeCsv(object? value)
    {
        var text = value?.ToString() ?? string.Empty;
        if (text.Contains(',') || text.Contains('"') || text.Contains('\n') || text.Contains('\r'))
        {
            return $"\"{text.Replace("\"", "\"\"")}\"";
        }

        return text;
    }
}