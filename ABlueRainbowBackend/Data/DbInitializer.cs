using ABlueRainbowBackend.Models;
using Microsoft.EntityFrameworkCore;

namespace ABlueRainbowBackend.Data
{
    public static class DbInitializer
    {
        public static void Initialize(ApplicationDbContext context)
        {
            context.Database.EnsureCreated();

            // Seeding providers
            if (!context.Providers.Any())
            {
                var providers = new Provider[]
                {
                    new Provider { Id = 1, FacilityType = "Assisted Living", FacilityName = "Assisted Living Provider" },
                    new Provider { Id = 2, FacilityType = "Home Health", FacilityName = "Home Health Provider" },
                    new Provider { Id = 3, FacilityType = "Hospice", FacilityName = "Hospice Provider" },
                    new Provider { Id = 4, FacilityType = "Skilled Nursing", FacilityName = "Skilled Nursing Provider" }
                };

                foreach (var p in providers)
                {
                    context.Providers.Add(p);
                }
                context.SaveChanges();
            }

            var alProvId = 1;
            var hhProvId = 2;
            var hospProvId = 3;
            var snfProvId = 4;

            if (!context.AssistedLivingFacilities.Any())
            {
                for (int i = 1; i <= 14; i++)
                {
                    context.AssistedLivingFacilities.Add(new AssistedLivingFacility
                    {
                        Name = $"Golden Years {i}",
                        Address = $"{123 + i} Sunset Blvd",
                        City = "Los Angeles",
                        State = "CA",
                        ZipCode = $"9000{i % 10}",
                        PhoneNumber = $"555-01{i:02}",
                        ProviderId = alProvId
                    });
                }
            }

            context.HomeHealthFacilities.Add(new HomeHealthFacility
            {
                Name = "Care at Home",
                Address = "456 Hill St",
                City = "San Francisco",
                State = "CA",
                ZipCode = "94101",
                PhoneNumber = "555-0102",
                ProviderId = hhProvId
            });

            context.HospiceFacilities.Add(new HospiceFacility
            {
                Name = "Peaceful Journey",
                Address = "789 Valley Ln",
                City = "San Diego",
                State = "CA",
                ZipCode = "92101",
                PhoneNumber = "555-0103",
                ProviderId = hospProvId
            });

            context.SkilledNursingFacilities.Add(new SkilledNursingFacility
            {
                Name = "Recovery Center",
                Address = "321 Oak Way",
                City = "Sacramento",
                State = "CA",
                ZipCode = "95814",
                PhoneNumber = "555-0104",
                ProviderId = snfProvId
            });

            context.SaveChanges();
        }
    }
}
