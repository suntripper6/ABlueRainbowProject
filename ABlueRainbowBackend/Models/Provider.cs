using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ABlueRainbowBackend.Models
{
    [Table("a_blue_rainbow_providers")]
    public class Provider
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [MaxLength(50)]
        public string FacilityType { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        public string FacilityName { get; set; } = string.Empty;

        // Navigation properties
        public virtual ICollection<HospiceFacility> HospiceFacilities { get; set; } = new List<HospiceFacility>();
        public virtual ICollection<SkilledNursingFacility> SkilledNursingFacilities { get; set; } = new List<SkilledNursingFacility>();
        public virtual ICollection<AssistedLivingFacility> AssistedLivingFacilities { get; set; } = new List<AssistedLivingFacility>();
        public virtual ICollection<HomeHealthFacility> HomeHealthFacilities { get; set; } = new List<HomeHealthFacility>();
    }
}
