using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Services;

namespace ABlueRainbowBackend.Controllers
{
    [Route("api/assistedliving")]
    [ApiController]
    public class AssistedLivingController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        private readonly IAdminAuditLogger _auditLogger;

        public AssistedLivingController(ApplicationDbContext context, IAdminAuditLogger auditLogger)
        {
            _context = context;
            _auditLogger = auditLogger;
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

        [Authorize(Policy = "AdminOnly")]
        [HttpPost]
        public async Task<ActionResult<AssistedLivingFacility>> PostFacility(AssistedLivingFacility facility)
        {
            _context.AssistedLivingFacilities.Add(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(
                HttpContext,
                "facility.created",
                "AssistedLivingFacility",
                facility.Id.ToString(),
                $"Created assisted living facility '{facility.Name}'.",
                metadata: new { facility.Name, facility.City, facility.State });
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPut("{id}")]
        public async Task<IActionResult> PutFacility(int id, AssistedLivingFacility facility)
        {
            if (id != facility.Id)
            {
                return BadRequest();
            }

            if (!await _context.AssistedLivingFacilities.AnyAsync(existing => existing.Id == id))
            {
                return NotFound();
            }

            _context.Entry(facility).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(
                HttpContext,
                "facility.updated",
                "AssistedLivingFacility",
                facility.Id.ToString(),
                $"Updated assisted living facility '{facility.Name}'.",
                metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteFacility(int id)
        {
            var facility = await _context.AssistedLivingFacilities.FindAsync(id);
            if (facility == null)
            {
                return NotFound();
            }

            _context.AssistedLivingFacilities.Remove(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(
                HttpContext,
                "facility.deleted",
                "AssistedLivingFacility",
                facility.Id.ToString(),
                $"Deleted assisted living facility '{facility.Name}'.",
                metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }
    }
}
