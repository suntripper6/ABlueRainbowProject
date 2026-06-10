import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Spinner, Alert } from 'react-bootstrap';

const FacilityList = ({ title, subtitle, kicker, fetchData, detailPath }) => {
  const [facilities, setFacilities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData()
      .then(response => {
        setFacilities(Array.isArray(response.data) ? response.data : response.data.results || []);
        setLoading(false);
      })
      .catch(err => {
        setError(`Failed to fetch ${title.toLowerCase()}.`);
        setLoading(false);
      });
  }, [fetchData, title]);

  if (loading) return (
    <div className="text-center py-5">
      <Spinner animation="border" variant="primary" />
    </div>
  );
  
  if (error) return (
    <div className="container py-5">
      <Alert variant="danger">{error}</Alert>
    </div>
  );

  return (
    <section className="page-shell page-shell--wide">
      <div className="page-intro">
        <p className="section-kicker">{kicker}</p>
        <div className="section-heading">
          <div>
            <h1 className="page-title">{title}</h1>
            <p className="page-subtitle">{subtitle}</p>
            <div className="page-meta">
              <span className="count-pill">{facilities.length} facilities</span>
            </div>
          </div>
        </div>
      </div>

      <div className="panel table-panel">
        <div className="table-responsive">
          <table className="table app-table align-middle">
            <thead>
              <tr>
                <th>Name</th>
                <th>Address</th>
                <th>City</th>
                <th>State</th>
                <th>Zip</th>
              </tr>
            </thead>
            <tbody>
              {facilities.length > 0 ? (
                facilities.map(facility => (
                  <tr key={facility.id}>
                    <td>
                      <Link to={`/${detailPath}/${facility.id}`} className="fw-bold text-decoration-none">
                        {facility.name}
                      </Link>
                    </td>
                    <td>{facility.address || facility.address_line_1}</td>
                    <td>{facility.city}</td>
                    <td>{facility.state}</td>
                    <td>{facility.zip_code || facility.zipcode}</td>
                  </tr>
                ))
              ) : (
                <tr>
                  <td colSpan="5" className="empty-cell">
                    <div className="table-empty-state">
                      <strong>No {title.toLowerCase()} list yet</strong>
                      <p>Start building the directory by adding the first {title.toLowerCase()} provider.</p>
                    </div>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>
    </section>
  );
};

export default FacilityList;
