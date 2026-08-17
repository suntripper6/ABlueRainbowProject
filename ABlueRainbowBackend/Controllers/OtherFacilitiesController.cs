using Microsoft.AspNetCore.Authorization;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;
using ABlueRainbowBackend.Services;

namespace ABlueRainbowBackend.Controllers
{
    [Route("api/homehealth")]
    [ApiController]
    public class HomeHealthController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        private readonly IAdminAuditLogger _auditLogger;
        public HomeHealthController(ApplicationDbContext context, IAdminAuditLogger auditLogger) { _context = context; _auditLogger = auditLogger; }

        [HttpGet]
        public async Task<ActionResult<PaginatedResponse<HomeHealthFacility>>> GetFacilities([FromQuery] int page = 1, [FromQuery] string? search = null)
        {
            var query = _context.HomeHealthFacilities.AsQueryable();
            if (!string.IsNullOrEmpty(search)) {
                var ls = search.ToLower();
                query = query.Where(f => f.Name.ToLower().Contains(ls) || f.City.ToLower().Contains(ls) || f.ZipCode.ToLower().Contains(ls));
            }
            var count = await query.CountAsync();
            var results = await query.OrderBy(f => f.Name).Skip((page - 1) * 10).Take(10).ToListAsync();
            return new PaginatedResponse<HomeHealthFacility> { Count = count, Results = results };
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<HomeHealthFacility>> GetFacility(int id)
        {
            var facility = await _context.HomeHealthFacilities.FindAsync(id);
            return facility == null ? NotFound() : facility;
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPost]
        public async Task<ActionResult<HomeHealthFacility>> PostFacility(HomeHealthFacility facility)
        {
            _context.HomeHealthFacilities.Add(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.created", "HomeHealthFacility", facility.Id.ToString(), $"Created home health facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPut("{id}")]
        public async Task<IActionResult> PutFacility(int id, HomeHealthFacility facility)
        {
            if (id != facility.Id)
            {
                return BadRequest();
            }

            if (!await _context.HomeHealthFacilities.AnyAsync(existing => existing.Id == id))
            {
                return NotFound();
            }

            _context.Entry(facility).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.updated", "HomeHealthFacility", facility.Id.ToString(), $"Updated home health facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteFacility(int id)
        {
            var facility = await _context.HomeHealthFacilities.FindAsync(id);
            if (facility == null)
            {
                return NotFound();
            }

            _context.HomeHealthFacilities.Remove(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.deleted", "HomeHealthFacility", facility.Id.ToString(), $"Deleted home health facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }
    }

    [Route("api/skillednursing")]
    [ApiController]
    public class SkilledNursingController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        private readonly IAdminAuditLogger _auditLogger;
        public SkilledNursingController(ApplicationDbContext context, IAdminAuditLogger auditLogger) { _context = context; _auditLogger = auditLogger; }

        [HttpGet]
        public async Task<ActionResult<PaginatedResponse<SkilledNursingFacility>>> GetFacilities([FromQuery] int page = 1, [FromQuery] string? search = null)
        {
            var query = _context.SkilledNursingFacilities.AsQueryable();
            if (!string.IsNullOrEmpty(search)) {
                var ls = search.ToLower();
                query = query.Where(f => f.Name.ToLower().Contains(ls) || f.City.ToLower().Contains(ls) || f.ZipCode.ToLower().Contains(ls));
            }
            var count = await query.CountAsync();
            var results = await query.OrderBy(f => f.Name).Skip((page - 1) * 10).Take(10).ToListAsync();
            return new PaginatedResponse<SkilledNursingFacility> { Count = count, Results = results };
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<SkilledNursingFacility>> GetFacility(int id)
        {
            var facility = await _context.SkilledNursingFacilities.FindAsync(id);
            return facility == null ? NotFound() : facility;
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPost]
        public async Task<ActionResult<SkilledNursingFacility>> PostFacility(SkilledNursingFacility facility)
        {
            _context.SkilledNursingFacilities.Add(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.created", "SkilledNursingFacility", facility.Id.ToString(), $"Created skilled nursing facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPut("{id}")]
        public async Task<IActionResult> PutFacility(int id, SkilledNursingFacility facility)
        {
            if (id != facility.Id)
            {
                return BadRequest();
            }

            if (!await _context.SkilledNursingFacilities.AnyAsync(existing => existing.Id == id))
            {
                return NotFound();
            }

            _context.Entry(facility).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.updated", "SkilledNursingFacility", facility.Id.ToString(), $"Updated skilled nursing facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteFacility(int id)
        {
            var facility = await _context.SkilledNursingFacilities.FindAsync(id);
            if (facility == null)
            {
                return NotFound();
            }

            _context.SkilledNursingFacilities.Remove(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.deleted", "SkilledNursingFacility", facility.Id.ToString(), $"Deleted skilled nursing facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }
    }

    [Route("api/hospice")]
    [ApiController]
    public class HospiceController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        private readonly IAdminAuditLogger _auditLogger;
        public HospiceController(ApplicationDbContext context, IAdminAuditLogger auditLogger) { _context = context; _auditLogger = auditLogger; }

        [HttpGet]
        public async Task<ActionResult<PaginatedResponse<HospiceFacility>>> GetFacilities([FromQuery] int page = 1, [FromQuery] string? search = null)
        {
            var query = _context.HospiceFacilities.AsQueryable();
            if (!string.IsNullOrEmpty(search)) {
                var ls = search.ToLower();
                query = query.Where(f => f.Name.ToLower().Contains(ls) || f.City.ToLower().Contains(ls) || f.ZipCode.ToLower().Contains(ls));
            }
            var count = await query.CountAsync();
            var results = await query.OrderBy(f => f.Name).Skip((page - 1) * 10).Take(10).ToListAsync();
            return new PaginatedResponse<HospiceFacility> { Count = count, Results = results };
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<HospiceFacility>> GetFacility(int id)
        {
            var facility = await _context.HospiceFacilities.FindAsync(id);
            return facility == null ? NotFound() : facility;
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPost]
        public async Task<ActionResult<HospiceFacility>> PostFacility(HospiceFacility facility)
        {
            _context.HospiceFacilities.Add(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.created", "HospiceFacility", facility.Id.ToString(), $"Created hospice facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpPut("{id}")]
        public async Task<IActionResult> PutFacility(int id, HospiceFacility facility)
        {
            if (id != facility.Id)
            {
                return BadRequest();
            }

            if (!await _context.HospiceFacilities.AnyAsync(existing => existing.Id == id))
            {
                return NotFound();
            }

            _context.Entry(facility).State = EntityState.Modified;
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.updated", "HospiceFacility", facility.Id.ToString(), $"Updated hospice facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }

        [Authorize(Policy = "AdminOnly")]
        [HttpDelete("{id}")]
        public async Task<IActionResult> DeleteFacility(int id)
        {
            var facility = await _context.HospiceFacilities.FindAsync(id);
            if (facility == null)
            {
                return NotFound();
            }

            _context.HospiceFacilities.Remove(facility);
            await _context.SaveChangesAsync();
            await _auditLogger.LogAsync(HttpContext, "facility.deleted", "HospiceFacility", facility.Id.ToString(), $"Deleted hospice facility '{facility.Name}'.", metadata: new { facility.Name, facility.City, facility.State });

            return NoContent();
        }
    }
}
