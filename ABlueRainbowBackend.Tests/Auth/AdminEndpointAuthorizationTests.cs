using System.Net;
using System.Net.Http.Json;
using System.Text.Json;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Tests.TestInfrastructure;
using Xunit;

namespace ABlueRainbowBackend.Tests.Auth;

public class AdminEndpointAuthorizationTests : IClassFixture<TestApplicationFactory>
{
    private readonly TestApplicationFactory _factory;

    public AdminEndpointAuthorizationTests(TestApplicationFactory factory)
    {
        _factory = factory;
    }

    [Fact]
    public async Task PostAssistedLiving_WithoutBearerToken_ReturnsUnauthorized()
    {
        using var client = _factory.CreateClient();

        var response = await client.PostAsJsonAsync("/api/assistedliving", CreateFacilityRequest());

        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
    }

    [Fact]
    public async Task Login_WithValidCredentials_ReturnsJwtToken()
    {
        using var client = _factory.CreateClient();

        var response = await client.PostAsJsonAsync("/api/auth/login", new
        {
            username = TestApplicationFactory.AdminUsername,
            password = TestApplicationFactory.AdminPassword,
        });

        var payload = await response.Content.ReadFromJsonAsync<LoginResponse>();

        Assert.Equal(HttpStatusCode.OK, response.StatusCode);
        Assert.NotNull(payload);
        Assert.False(string.IsNullOrWhiteSpace(payload.Token));
    }

    [Fact]
    public async Task PostAssistedLiving_WithBearerToken_ReturnsCreated()
    {
        using var client = await CreateAdminClientAsync();

        var response = await client.PostAsJsonAsync("/api/assistedliving", CreateFacilityRequest());

        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
    }

    [Fact]
    public async Task GetAuditLogs_WithoutBearerToken_ReturnsUnauthorized()
    {
        using var client = _factory.CreateClient();

        var response = await client.GetAsync("/api/admin/audit-logs");

        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
    }

    [Fact]
    public async Task CreateAdminUser_WithBearerToken_CreatesUserThatCanLogIn()
    {
        using var client = await CreateAdminClientAsync();

        var createResponse = await client.PostAsJsonAsync("/api/admin/users", new
        {
            username = "second-admin",
            display_name = "Second Admin",
            password = "second-admin-password",
        });

        Assert.Equal(HttpStatusCode.Created, createResponse.StatusCode);

        using var anonymousClient = _factory.CreateClient();
        var loginResponse = await anonymousClient.PostAsJsonAsync("/api/auth/login", new
        {
            username = "second-admin",
            password = "second-admin-password",
        });

        Assert.Equal(HttpStatusCode.OK, loginResponse.StatusCode);
    }

    [Fact]
    public async Task RotateAdminUserPassword_WithBearerToken_ChangesCredentials()
    {
        using var client = await CreateAdminClientAsync();

        var createResponse = await client.PostAsJsonAsync("/api/admin/users", new
        {
            username = "password-rotate-admin",
            display_name = "Password Rotate Admin",
            password = "initial-password",
        });

        var createdUser = await createResponse.Content.ReadFromJsonAsync<AdminUserSummaryResponse>();
        Assert.NotNull(createdUser);

        var rotateResponse = await client.PutAsJsonAsync($"/api/admin/users/{createdUser!.Id}/password", new
        {
            password = "updated-password",
        });

        Assert.Equal(HttpStatusCode.NoContent, rotateResponse.StatusCode);

        using var anonymousClient = _factory.CreateClient();
        var oldLoginResponse = await anonymousClient.PostAsJsonAsync("/api/auth/login", new
        {
            username = "password-rotate-admin",
            password = "initial-password",
        });
        var newLoginResponse = await anonymousClient.PostAsJsonAsync("/api/auth/login", new
        {
            username = "password-rotate-admin",
            password = "updated-password",
        });

        Assert.Equal(HttpStatusCode.Unauthorized, oldLoginResponse.StatusCode);
        Assert.Equal(HttpStatusCode.OK, newLoginResponse.StatusCode);
    }

    [Fact]
    public async Task UpdateAdminUser_WithBearerToken_CanDeactivateOtherAdmin()
    {
        using var client = await CreateAdminClientAsync();

        var createResponse = await client.PostAsJsonAsync("/api/admin/users", new
        {
            username = "inactive-admin",
            display_name = "Inactive Admin",
            password = "inactive-admin-password",
        });

        var createdUser = await createResponse.Content.ReadFromJsonAsync<AdminUserSummaryResponse>();
        Assert.NotNull(createdUser);

        var updateResponse = await client.PutAsJsonAsync($"/api/admin/users/{createdUser!.Id}", new
        {
            display_name = "Inactive Admin",
            is_active = false,
        });

        Assert.Equal(HttpStatusCode.OK, updateResponse.StatusCode);

        using var anonymousClient = _factory.CreateClient();
        var loginResponse = await anonymousClient.PostAsJsonAsync("/api/auth/login", new
        {
            username = "inactive-admin",
            password = "inactive-admin-password",
        });

        Assert.Equal(HttpStatusCode.Unauthorized, loginResponse.StatusCode);
    }

    [Fact]
    public async Task AdminActions_WriteAuditLogs()
    {
        using var client = await CreateAdminClientAsync();

        var facilityResponse = await client.PostAsJsonAsync("/api/assistedliving", CreateFacilityRequest("Audit Trail Facility"));
        Assert.Equal(HttpStatusCode.Created, facilityResponse.StatusCode);

        var adminUserResponse = await client.PostAsJsonAsync("/api/admin/users", new
        {
            username = "audit-admin",
            display_name = "Audit Admin",
            password = "audit-admin-password",
        });
        Assert.Equal(HttpStatusCode.Created, adminUserResponse.StatusCode);

        var auditLogsResponse = await client.GetAsync("/api/admin/audit-logs?take=25");
        auditLogsResponse.EnsureSuccessStatusCode();

        using var document = JsonDocument.Parse(await auditLogsResponse.Content.ReadAsStringAsync());
        var actions = document.RootElement.EnumerateArray()
            .Select(element => element.GetProperty("action_type").GetString())
            .ToList();

        Assert.Contains("admin_user.login", actions);
        Assert.Contains("facility.created", actions);
        Assert.Contains("admin_user.created", actions);
    }

    [Fact]
    public async Task GetAuditLogs_WithFilters_ReturnsMatchingEntries()
    {
        using var client = await CreateAdminClientAsync();

        var adminUserResponse = await client.PostAsJsonAsync("/api/admin/users", new
        {
            username = "filter-admin",
            display_name = "Filter Admin",
            password = "filter-admin-password",
        });
        Assert.Equal(HttpStatusCode.Created, adminUserResponse.StatusCode);

        var auditLogsResponse = await client.GetAsync("/api/admin/audit-logs?actor_username=admin&action_type=admin_user.created&take=25");
        auditLogsResponse.EnsureSuccessStatusCode();

        using var document = JsonDocument.Parse(await auditLogsResponse.Content.ReadAsStringAsync());
        var rows = document.RootElement.EnumerateArray().ToList();

        Assert.NotEmpty(rows);
        Assert.All(rows, row =>
        {
            Assert.Equal("admin_user.created", row.GetProperty("action_type").GetString());
            Assert.Contains("admin", row.GetProperty("actor_username").GetString(), StringComparison.OrdinalIgnoreCase);
        });
    }

    [Fact]
    public async Task GetAuditLogs_WithCsvFormat_ReturnsCsvFile()
    {
        using var client = await CreateAdminClientAsync();

        var facilityResponse = await client.PostAsJsonAsync("/api/assistedliving", CreateFacilityRequest("CSV Audit Facility"));
        Assert.Equal(HttpStatusCode.Created, facilityResponse.StatusCode);

        var auditLogsResponse = await client.GetAsync("/api/admin/audit-logs?take=25&format=csv");
        auditLogsResponse.EnsureSuccessStatusCode();

        var csv = await auditLogsResponse.Content.ReadAsStringAsync();

        Assert.Equal("text/csv", auditLogsResponse.Content.Headers.ContentType?.MediaType);
        Assert.Contains("action_type", csv);
        Assert.Contains("facility.created", csv);
    }

    [Fact]
    public async Task GetFeedbacks_WithoutBearerToken_ReturnsUnauthorized()
    {
        using var client = _factory.CreateClient();

        var response = await client.GetAsync("/api/feedback");

        Assert.Equal(HttpStatusCode.Unauthorized, response.StatusCode);
    }

    [Fact]
    public async Task PostFeedback_RemainsPublic()
    {
        using var client = _factory.CreateClient();

        var response = await client.PostAsJsonAsync("/api/feedback", new UserFeedback
        {
            Name = "Test User",
            Email = "test@example.com",
            Comments = "Helpful directory.",
        });

        Assert.Equal(HttpStatusCode.Created, response.StatusCode);
    }

    private async Task<HttpClient> CreateAdminClientAsync()
    {
        var client = _factory.CreateClient();
        var loginResponse = await client.PostAsJsonAsync("/api/auth/login", new
        {
            username = TestApplicationFactory.AdminUsername,
            password = TestApplicationFactory.AdminPassword,
        });

        loginResponse.EnsureSuccessStatusCode();

        var payload = await loginResponse.Content.ReadFromJsonAsync<LoginResponse>();
        client.DefaultRequestHeaders.Authorization = new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", payload!.Token);
        return client;
    }

    private static object CreateFacilityRequest(string name = "Azure Terrace")
    {
        return new
        {
            name,
            address = "123 Main St",
            city = "Austin",
            state = "TX",
            zip_code = "78701",
            phone_number = "555-0101",
            provider_id = 1,
        };
    }

    private static int GetCreatedEntityId(HttpResponseMessage response)
    {
        var location = response.Headers.Location?.ToString();
        Assert.False(string.IsNullOrWhiteSpace(location));

        var lastSegment = location!.TrimEnd('/').Split('/').Last();
        return int.Parse(lastSegment);
    }
}