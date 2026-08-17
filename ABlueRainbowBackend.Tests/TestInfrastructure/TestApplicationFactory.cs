using ABlueRainbowBackend.Data;
using Microsoft.AspNetCore.Hosting;
using Microsoft.AspNetCore.Mvc.Testing;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.DependencyInjection.Extensions;

namespace ABlueRainbowBackend.Tests.TestInfrastructure;

public sealed class TestApplicationFactory : WebApplicationFactory<Program>
{
    public const string AdminUsername = "admin";
    public const string AdminPassword = "test-password";
    public const string JwtSigningKey = "test-jwt-signing-key-1234567890-abcdef";
    private readonly string _databaseName = $"abluerainbow-tests-{Guid.NewGuid()}";

    public TestApplicationFactory()
    {
        Environment.SetEnvironmentVariable("ConnectionStrings__DefaultConnection", "Host=localhost;Database=test;Username=test;Password=test");
        Environment.SetEnvironmentVariable("Authentication__AdminUsername", AdminUsername);
        Environment.SetEnvironmentVariable("Authentication__AdminPassword", AdminPassword);
        Environment.SetEnvironmentVariable("Authentication__JwtSigningKey", JwtSigningKey);
        Environment.SetEnvironmentVariable("Authentication__JwtIssuer", "ABlueRainbowBackend");
        Environment.SetEnvironmentVariable("Authentication__JwtAudience", "ABlueRainbowFrontend");
    }

    protected override void ConfigureWebHost(IWebHostBuilder builder)
    {
        builder.UseEnvironment("Development");

        builder.ConfigureAppConfiguration((_, configBuilder) =>
        {
            configBuilder.AddInMemoryCollection(new Dictionary<string, string?>
            {
                ["ConnectionStrings:DefaultConnection"] = "Host=localhost;Database=test;Username=test;Password=test",
                ["Authentication:AdminUsername"] = AdminUsername,
                ["Authentication:AdminPassword"] = AdminPassword,
                ["Authentication:JwtSigningKey"] = JwtSigningKey,
                ["Cors:AllowedOrigins:0"] = "http://localhost:5173",
            });
        });

        builder.ConfigureServices(services =>
        {
            services.RemoveAll(typeof(DbContextOptions<ApplicationDbContext>));
            services.RemoveAll(typeof(ApplicationDbContext));

            services.AddDbContext<ApplicationDbContext>(options =>
                options.UseInMemoryDatabase(_databaseName));

            using var serviceProvider = services.BuildServiceProvider();
            using var scope = serviceProvider.CreateScope();
            var context = scope.ServiceProvider.GetRequiredService<ApplicationDbContext>();
            var configuration = scope.ServiceProvider.GetRequiredService<IConfiguration>();
            DbInitializer.Initialize(context, configuration);
        });
    }

    protected override void Dispose(bool disposing)
    {
        Environment.SetEnvironmentVariable("ConnectionStrings__DefaultConnection", null);
        Environment.SetEnvironmentVariable("Authentication__AdminUsername", null);
        Environment.SetEnvironmentVariable("Authentication__AdminPassword", null);
        Environment.SetEnvironmentVariable("Authentication__JwtSigningKey", null);
        Environment.SetEnvironmentVariable("Authentication__JwtIssuer", null);
        Environment.SetEnvironmentVariable("Authentication__JwtAudience", null);
        base.Dispose(disposing);
    }
}