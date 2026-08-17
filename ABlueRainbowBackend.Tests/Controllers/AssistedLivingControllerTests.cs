using ABlueRainbowBackend.Controllers;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Services;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using Xunit;

namespace ABlueRainbowBackend.Tests.Controllers;

public class AssistedLivingControllerTests
{
    [Fact]
    public async Task GetFacilities_ReturnsSecondPageOfAlphabetizedResults()
    {
        await using var context = CreateContext();

        var facilities = Enumerable.Range(1, 12)
            .Select(index => CreateFacility(index, $"Facility {index:00}"));

        context.AssistedLivingFacilities.AddRange(facilities);
        await context.SaveChangesAsync();

        var controller = CreateController(context);

        ActionResult<PaginatedResponse<AssistedLivingFacility>> actionResult = await controller.GetFacilities(page: 2);
        var response = Assert.IsType<PaginatedResponse<AssistedLivingFacility>>(actionResult.Value);

        Assert.Equal(12, response.Count);
        Assert.Collection(
            response.Results,
            facility => Assert.Equal("Facility 11", facility.Name),
            facility => Assert.Equal("Facility 12", facility.Name));
    }

    [Fact]
    public async Task GetFacilities_FiltersAcrossSearchableFields()
    {
        await using var context = CreateContext();

        context.AssistedLivingFacilities.AddRange(
            CreateFacility(1, "Blue Haven", address: "1 Main St", city: "Austin"),
            CreateFacility(2, "Green Valley", address: "22 Bluebird Lane", city: "Dallas"),
            CreateFacility(3, "Oak Terrace", address: "99 Elm St", city: "Houston"));
        await context.SaveChangesAsync();

        var controller = CreateController(context);

        ActionResult<PaginatedResponse<AssistedLivingFacility>> actionResult = await controller.GetFacilities(search: "blue");
        var response = Assert.IsType<PaginatedResponse<AssistedLivingFacility>>(actionResult.Value);

        Assert.Equal(2, response.Count);
        Assert.All(response.Results, facility =>
        {
            var haystack = string.Join(' ', facility.Name, facility.Address, facility.City, facility.State, facility.ZipCode).ToLowerInvariant();
            Assert.Contains("blue", haystack);
        });
    }

    [Fact]
    public async Task GetFacility_ReturnsNotFoundWhenFacilityDoesNotExist()
    {
        await using var context = CreateContext();
        var controller = CreateController(context);

        ActionResult<AssistedLivingFacility> actionResult = await controller.GetFacility(404);

        Assert.IsType<NotFoundResult>(actionResult.Result);
    }

    [Fact]
    public async Task PutFacility_UpdatesExistingFacility()
    {
        await using var context = CreateContext();
        var facility = CreateFacility(1, "Original Name");
        context.AssistedLivingFacilities.Add(facility);
        await context.SaveChangesAsync();

        var controller = CreateController(context);
        facility.Name = "Updated Name";

        var result = await controller.PutFacility(facility.Id, facility);

        Assert.IsType<NoContentResult>(result);
        Assert.Equal("Updated Name", (await context.AssistedLivingFacilities.FindAsync(facility.Id))!.Name);
    }

    [Fact]
    public async Task DeleteFacility_RemovesExistingFacility()
    {
        await using var context = CreateContext();
        var facility = CreateFacility(1, "Delete Me");
        context.AssistedLivingFacilities.Add(facility);
        await context.SaveChangesAsync();

        var controller = CreateController(context);

        var result = await controller.DeleteFacility(facility.Id);

        Assert.IsType<NoContentResult>(result);
        Assert.Null(await context.AssistedLivingFacilities.FindAsync(facility.Id));
    }

    private static ApplicationDbContext CreateContext()
    {
        var options = new DbContextOptionsBuilder<ApplicationDbContext>()
            .UseInMemoryDatabase(Guid.NewGuid().ToString())
            .Options;

        return new ApplicationDbContext(options);
    }

    private static AssistedLivingController CreateController(ApplicationDbContext context)
    {
        return new AssistedLivingController(context, new NoOpAdminAuditLogger())
        {
            ControllerContext = new ControllerContext
            {
                HttpContext = new DefaultHttpContext()
            }
        };
    }

    private static AssistedLivingFacility CreateFacility(int id, string name, string address = "100 Main St", string city = "Austin")
    {
        return new AssistedLivingFacility
        {
            Id = id,
            Name = name,
            Address = address,
            City = city,
            State = "TX",
            ZipCode = $"787{id:00}",
            ProviderId = 1,
        };
    }

    private sealed class NoOpAdminAuditLogger : IAdminAuditLogger
    {
        public Task LogAsync(
            HttpContext httpContext,
            string actionType,
            string entityType,
            string entityId,
            string description,
            object? metadata = null,
            int? actorAdminUserIdOverride = null,
            string? actorUsernameOverride = null)
        {
            return Task.CompletedTask;
        }
    }
}