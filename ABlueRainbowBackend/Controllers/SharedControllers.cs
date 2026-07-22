using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
using ABlueRainbowBackend.Data;
using ABlueRainbowBackend.Models;

namespace ABlueRainbowBackend.Controllers
{
    [Route("api/providers")]
    [ApiController]
    public class ProviderController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public ProviderController(ApplicationDbContext context) { _context = context; }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<Provider>>> GetProviders()
        {
            return await _context.Providers.OrderBy(p => p.FacilityType).ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<Provider>> GetProvider(int id)
        {
            var provider = await _context.Providers.FindAsync(id);
            return provider == null ? NotFound() : provider;
        }
    }

    [Route("api/states")]
    [ApiController]
    public class StateController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public StateController(ApplicationDbContext context) { _context = context; }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<State>>> GetStates()
        {
            return await _context.States.OrderBy(s => s.StateName).ThenBy(s => s.City).ToListAsync();
        }

        [HttpGet("{id}")]
        public async Task<ActionResult<State>> GetState(int id)
        {
            var state = await _context.States.FindAsync(id);
            return state == null ? NotFound() : state;
        }
    }

    [Route("api/feedback")]
    [ApiController]
    public class FeedbackController : ControllerBase
    {
        private readonly ApplicationDbContext _context;
        public FeedbackController(ApplicationDbContext context) { _context = context; }

        [HttpGet]
        public async Task<ActionResult<IEnumerable<UserFeedback>>> GetFeedbacks()
        {
            return await _context.UserFeedbacks.OrderBy(f => f.Name).ToListAsync();
        }

        [HttpPost]
        public async Task<ActionResult<UserFeedback>> PostFeedback(UserFeedback feedback)
        {
            _context.UserFeedbacks.Add(feedback);
            await _context.SaveChangesAsync();
            return CreatedAtAction(nameof(GetFeedbacks), new { id = feedback.Id }, feedback);
        }
    }
}
