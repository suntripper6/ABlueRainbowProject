using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;

namespace ABlueRainbowBackend.Controllers
{
    [Route("api/assistedliving")]
    [ApiController]
    public class AssistedLivingController : ControllerBase
    {
        private readonly ApplicationDbContext _context;

        public AssistedLivingController(ApplicationDbContext context)
        {
            _context = context;
        }

        [HttpGet]
        public async Task<ActionResult<PaginatedResponse<AssistedLivingFacility>>> GetFacilities(
            [FromQuery] int page = 1,
            [FromQuery] string? search = null,
            [FromQuery] string? city = null,
            [FromQuery] string? state = null,
            [FromQuery] string? zip_code = null)
        {
            var query = _context.AssistedLivingFacilities.AsQueryable();

            if (!string.IsNullOrEmpty(search))
            {
                var lowerSearch = search.ToLower();
                query = query.Where(f => f.Name.ToLower().Contains(lowerSearch) || 
                                       f.Address.ToLower().Contains(lowerSearch) || 
                                       f.City.ToLower().Contains(lowerSearch) || 
                                       f.State.ToLower().Contains(lowerSearch) || 
                                       f.ZipCode.ToLower().Contains(lowerSearch));
            }

            if (!string.IsNullOrEmpty(city)) query = query.Where(f => f.City == city);
            if (!string.IsNullOrEmpty(state)) query = query.Where(f => f.State == state);
            if (!string.IsNullOrEmpty(zip_code)) query = query.Where(f => f.ZipCode == zip_code);

            var totalCount = await query.CountAsync();
            var pageSize = 10;
            var results = await query.OrderBy(f => f.Name)
                                     .Skip((page - 1) * pageSize)
                                     .Take(pageSize)
                                     .ToListAsync();

            return new PaginatedResponse<AssistedLivingFacility>
            {
                Count = totalCount,
                Results = results
            };
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<AssistedLivingFacility>> GetFacility(int id)
        {
            var facility = await _context.AssistedLivingFacilities.FindAsync(id);
            if (facility == null) return NotFound();
            return facility;
        }

        [HttpPost]
        public async Task<ActionResult<AssistedLivingFacility>> PostFacility(AssistedLivingFacility facility)
        {
            _context.AssistedLivingFacilities.Add(facility);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }
    }
}
