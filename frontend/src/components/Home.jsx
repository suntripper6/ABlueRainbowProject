import React from 'react';
import { Link } from 'react-router-dom';

const Home = () => {
  return (
    <div className="landing-root">
      <section className="hero-shell">
        <div className="hero-logo-row">
          <div className="visual-frame hero-logo-frame">
            <img src="/img/logo.png" className="site-logo" alt="A Blue Rainbow logo" />
          </div>
        </div>

        <div className="hero-panel">
          <div className="hero-copy">
            <p className="hero-badge">Gentle Care Navigation</p>
            <h1 className="hero-title">A calmer way to move through senior care options.</h1>
            <p className="hero-subtitle">
              A Blue Rainbow brings assisted living, home health, skilled nursing, and hospice resources into one quieter, easier-to-scan directory for caregivers and families.
            </p>
            <div className="hero-actions">
              <Link to="/assistedliving" className="btn btn-primary">Browse Resources</Link>
              <Link to="/feedback" className="btn btn-secondary">Share Feedback</Link>
            </div>
          </div>
          <div className="hero-rail">
            <div className="hero-stats">
              <div className="stat-card">
                <span>Care categories</span>
                <strong>4</strong>
              </div>
              <div className="stat-card">
                <span>Core actions</span>
                <strong>Search, review, update</strong>
              </div>
              <div className="stat-card">
                <span>Built for</span>
                <strong>Caregivers first</strong>
              </div>
            </div>
            <div className="hero-note-card">
              <span className="hero-note-label">Why it works</span>
              <p>Search, compare, and revisit provider records without losing your place in the directory.</p>
            </div>
          </div>
        </div>

        <div className="resource-grid">
          <Link to="/assistedliving" className="resource-card">
            <span className="card-tag">Residential</span>
            <h3>Assisted Living</h3>
            <p>Compare facilities with a cleaner overview and faster drill-down into details.</p>
          </Link>
          <Link to="/homehealth" className="resource-card">
            <span className="card-tag">At Home</span>
            <h3>Home Health</h3>
            <p>Review home care providers in a more legible table and detail experience.</p>
          </Link>
          <Link to="/skillednursing" className="resource-card">
            <span className="card-tag">Medical</span>
            <h3>Skilled Nursing</h3>
            <p>Scan available nursing facilities with clearer navigation and stronger hierarchy.</p>
          </Link>
          <Link to="/hospice" className="resource-card">
            <span className="card-tag">Supportive</span>
            <h3>Hospice</h3>
            <p>Access hospice information with a calmer presentation and consistent actions.</p>
          </Link>
        </div>
      </section>
    </div>
  );
};

export default Home;
