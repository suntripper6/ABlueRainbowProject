import React from 'react';
import { Link, NavLink } from 'react-router-dom';

const Header = () => {
  return (
    <header className="site-header">
      <nav className="navbar navbar-expand-lg navbar-dark site-nav">
        <div className="container-fluid px-0">
          <Link className="navbar-brand brand-mark" to="/">A Blue Rainbow</Link>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#mynavbar">
            <span className="navbar-toggler-icon"></span>
          </button>
          
          <div className="collapse navbar-collapse" id="mynavbar">
            <ul className="navbar-nav me-auto">
              <li className="nav-item">
                <NavLink className="nav-link" to="/">Home</NavLink>
              </li>
              <li className="nav-item dropdown">
                <a 
                  className="nav-link dropdown-toggle" 
                  href="#" 
                  role="button" 
                  data-bs-toggle="dropdown" 
                  aria-expanded="false"
                >
                  Resources
                </a>
                <ul className="dropdown-menu">
                  <li><Link className="dropdown-item" to="/assistedliving">Assisted Living</Link></li>
                  <li><Link className="dropdown-item" to="/homehealth">Home Health Care</Link></li>
                  <li><Link className="dropdown-item" to="/skillednursing">Skilled Nursing</Link></li>
                  <li><Link className="dropdown-item" to="/hospice">Hospice</Link></li>
                </ul>
              </li>
              <li className="nav-item">
                <NavLink className="nav-link" to="/feedback">Feedback</NavLink>
              </li>
            </ul>
            
            <div className="d-flex align-items-center gap-3 flex-column flex-lg-row ms-lg-auto">
              <form className="d-flex top-search" action="/search" method="GET">
                <input 
                  type="search" 
                  className="form-control" 
                  aria-label="Search" 
                  placeholder="Search facilities by name" 
                  name="q" 
                />
                <button className="btn btn-outline-secondary" type="submit">Search</button>
              </form>
              
              <div className="d-flex align-items-center gap-2">
                <Link className="btn btn-outline-light" to="/login">Admin Login</Link>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </header>
  );
};

export default Header;
