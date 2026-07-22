using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;

namespace ABlueRainbowBackend.Controllers
{
    [Route("api/homehealth")]
    [ApiController]
    public class HomeHealthController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public HomeHealthController(ApplicationDbContext context) { _context = context; }

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

        [HttpPost]
        public async Task<ActionResult<HomeHealthFacility>> PostFacility(HomeHealthFacility facility)
        {
            _context.HomeHealthFacilities.Add(facility);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetFacility), new { id = facility.Id }, facility);
        }
    }

    [Route("api/skillednursing")]
    [ApiController]
    public class SkilledNursingController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public SkilledNursingController(ApplicationDbContext context) { _context = context; }

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
    }

    [Route("api/hospice")]
    [ApiController]
    public class HospiceController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public HospiceController(ApplicationDbContext context) { _context = context; }

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
    }
}
