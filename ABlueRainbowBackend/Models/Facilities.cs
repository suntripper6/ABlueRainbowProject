using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ABlueRainbowBackend.Models
{
    public abstract class FacilityBase
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [MaxLength(500)]
        public string Name { get; set; } = string.Empty;

        [Required]
        [MaxLength(500)]
        public string Address { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        public string City { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        public string State { get; set; } = string.Empty;

        [Required]
        [MaxLength(15)]
        public string ZipCode { get; set; } = string.Empty;

        [MaxLength(15)]
        public string? PhoneNumber { get; set; }

        public bool? MedicareElig { get; set; } = true;

        public string? Map { get; set; }

        public int? Rating { get; set; }

        public string? Reviews { get; set; }

        [MaxLength(255)]
        public string? OfficialWebsite { get; set; }

        [ForeignKey("Provider")]
        public int ProviderId { get; set; }
        public virtual Provider? Provider { get; set; }
    }

    [Table("a_blue_rainbow_hospicefacilities")]
    public class HospiceFacility : FacilityBase { }

    [Table("a_blue_rainbow_skillednursingfacilities")]
    public class SkilledNursingFacility : FacilityBase
    {
        public bool? TransportationServices { get; set; } = true;
        public bool? CaseManagement { get; set; } = true;
    }

    [Table("a_blue_rainbow_assistedlivingfacilities")]
    public class AssistedLivingFacility : FacilityBase
    {
        public bool? TransportationServices { get; set; } = true;
        public bool? CaseManagement { get; set; } = true;
    }

    [Table("a_blue_rainbow_homehealthfacilities")]
    public class HomeHealthFacility : FacilityBase { }
}
