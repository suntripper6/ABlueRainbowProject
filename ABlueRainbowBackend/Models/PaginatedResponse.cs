namespace ABlueRainbowBackend.Models
{
    public class PaginatedResponse<T>
    {
        public int Count { get; set; }
        public string? Next { get; set; }
        public string? Previous { get; set; }
        public IEnumerable<T> Results { get; set; } = new List<T>();
    }
}
