namespace ABlueRainbowBackend.Models;

using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

public class LoginRequest
{
    public string Username { get; set; } = string.Empty;
    public string Password { get; set; } = string.Empty;
}

public class LoginResponse
{
    public string Token { get; set; } = string.Empty;
    public string Username { get; set; } = string.Empty;
    public DateTimeOffset ExpiresAt { get; set; }
}

public class AdminUserSummaryResponse
{
    public int Id { get; set; }
    public string Username { get; set; } = string.Empty;
    public string DisplayName { get; set; } = string.Empty;
    public bool IsActive { get; set; }
    public DateTimeOffset CreatedAtUtc { get; set; }
}

public class CreateAdminUserRequest
{
    public string Username { get; set; } = string.Empty;
    public string DisplayName { get; set; } = string.Empty;
    public string Password { get; set; } = string.Empty;
}

public class UpdateAdminUserRequest
{
    public string DisplayName { get; set; } = string.Empty;
    public bool IsActive { get; set; }
}

public class RotateAdminUserPasswordRequest
{
    public string Password { get; set; } = string.Empty;
}

public class AdminAuditLogResponse
{
    public int Id { get; set; }
    public int? ActorAdminUserId { get; set; }
    public string ActorUsername { get; set; } = string.Empty;
    public string ActionType { get; set; } = string.Empty;
    public string EntityType { get; set; } = string.Empty;
    public string EntityId { get; set; } = string.Empty;
    public string Description { get; set; } = string.Empty;
    public string? MetadataJson { get; set; }
    public string? IpAddress { get; set; }
    public string? UserAgent { get; set; }
    public DateTimeOffset OccurredAtUtc { get; set; }
}

[Table("a_blue_rainbow_adminusers")]
public class AdminUser
{
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int Id { get; set; }

    [Required]
    [MaxLength(100)]
    public string Username { get; set; } = string.Empty;

    [Required]
    [MaxLength(150)]
    public string DisplayName { get; set; } = string.Empty;

    [Required]
    public string PasswordHash { get; set; } = string.Empty;

    public bool IsActive { get; set; } = true;

    public DateTimeOffset CreatedAtUtc { get; set; } = DateTimeOffset.UtcNow;
}

[Table("a_blue_rainbow_adminauditlogs")]
public class AdminAuditLog
{
    [Key]
    [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
    public int Id { get; set; }

    public int? ActorAdminUserId { get; set; }

    [Required]
    [MaxLength(100)]
    public string ActorUsername { get; set; } = string.Empty;

    [Required]
    [MaxLength(100)]
    public string ActionType { get; set; } = string.Empty;

    [Required]
    [MaxLength(100)]
    public string EntityType { get; set; } = string.Empty;

    [Required]
    [MaxLength(100)]
    public string EntityId { get; set; } = string.Empty;

    [Required]
    [MaxLength(400)]
    public string Description { get; set; } = string.Empty;

    public string? MetadataJson { get; set; }

    [MaxLength(100)]
    public string? IpAddress { get; set; }

    [MaxLength(512)]
    public string? UserAgent { get; set; }

    public DateTimeOffset OccurredAtUtc { get; set; } = DateTimeOffset.UtcNow;
}