using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Models;

namespace ABlueRainbowBackend.Data
{
    public class ApplicationDbContext : DbContext
    {
        public ApplicationDbContext(DbContextOptions<ApplicationDbContext> options)
            : base(options)
        {
        }

        public DbSet<Provider> Providers { get; set; }
        public DbSet<HospiceFacility> HospiceFacilities { get; set; }
        public DbSet<SkilledNursingFacility> SkilledNursingFacilities { get; set; }
        public DbSet<AssistedLivingFacility> AssistedLivingFacilities { get; set; }
        public DbSet<HomeHealthFacility> HomeHealthFacilities { get; set; }
        public DbSet<State> States { get; set; }
        public DbSet<UserFeedback> UserFeedbacks { get; set; }
        public DbSet<AdminUser> AdminUsers { get; set; }
        public DbSet<AdminAuditLog> AdminAuditLogs { get; set; }

        protected override void OnModelCreating(ModelBuilder modelBuilder)
        {
            base.OnModelCreating(modelBuilder);

            // Configure TPC (Table-per-Concrete-Type) or just plain mapping since they have [Table] attributes
            // By default EF Core will use TPH if we don't specify. 
            // Since I added [Table] attributes to each child, it should use TPT or TPC.
            // For facility types, I'll ensure they map to their specific tables.
            
            modelBuilder.Entity<HospiceFacility>().ToTable("a_blue_rainbow_hospicefacilities");
            modelBuilder.Entity<SkilledNursingFacility>().ToTable("a_blue_rainbow_skillednursingfacilities");
            modelBuilder.Entity<AssistedLivingFacility>().ToTable("a_blue_rainbow_assistedlivingfacilities");
            modelBuilder.Entity<HomeHealthFacility>().ToTable("a_blue_rainbow_homehealthfacilities");
            modelBuilder.Entity<AdminUser>().ToTable("a_blue_rainbow_adminusers");
            modelBuilder.Entity<AdminAuditLog>().ToTable("a_blue_rainbow_adminauditlogs");
        }
    }
}
