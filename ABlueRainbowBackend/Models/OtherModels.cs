using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;

namespace ABlueRainbowBackend.Models
{
    [Table("a_blue_rainbow_states")]
    public class State
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        public int? ZipCode { get; set; }
        public double? Latitude { get; set; }
        public double? Longitude { get; set; }

        [MaxLength(50)]
        public string? City { get; set; }

        [MaxLength(50)]
        public string? StateName { get; set; }

        public bool? Zcta { get; set; }

        [MaxLength(50)]
        public string? ParentZcta { get; set; }

        public int? Population { get; set; }
        public double? Density { get; set; }
        public int? CountyFips { get; set; }

        [MaxLength(50)]
        public string? CountyName { get; set; }

        [MaxLength(128)]
        public string? CountyWeights { get; set; }

        [MaxLength(64)]
        public string? CountyNamesAll { get; set; }

        [MaxLength(50)]
        public string? CountyFipsAll { get; set; }

        public bool? Imprecise { get; set; }
        public bool? Military { get; set; }

        [MaxLength(50)]
        public string? Timezone { get; set; }

        [MaxLength(50)]
        public string? StateAbbrev { get; set; }
    }

    [Table("a_blue_rainbow_userfeedback")]
    public class UserFeedback
    {
        [Key]
        [DatabaseGenerated(DatabaseGeneratedOption.Identity)]
        public int Id { get; set; }

        [Required]
        [MaxLength(255)]
        public string Name { get; set; } = string.Empty;

        [Required]
        [MaxLength(255)]
        public string Email { get; set; } = string.Empty;

        [Required]
        public string Comments { get; set; } = string.Empty;
    }
}
