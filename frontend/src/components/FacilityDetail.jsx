import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import { Spinner, Alert } from 'react-bootstrap';

const FacilityDetail = ({ kicker, fetchData }) => {
  const { id } = useParams();
  const [facility, setFacility] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchData(id)
      .then(response => {
        setFacility(response.data);
        setLoading(false);
      })
      .catch(err => {
        setError('Failed to fetch facility details.');
        setLoading(false);
      });
  }, [id, fetchData]);

  if (loading) return (
    <div className="text-center py-5">
      <Spinner animation="border" variant="primary" />
    </div>
  );

  if (error || !facility) return (
    <div className="container py-5">
      <Alert variant="danger">{error || 'Facility not found.'}</Alert>
      <Link to="/" className="btn btn-secondary mt-3">Back to Home</Link>
    </div>
  );

  return (
    <section className="page-shell">
      <div className="panel detail-panel">
        <p className="section-kicker">{kicker}</p>
        <h1 className="page-title">{facility.name}</h1>
        <p className="detail-address">{facility.address || facility.address_line_1}</p>
        <p className="detail-description">
          {facility.city}, {facility.state} {facility.zip_code || facility.zipcode || facility.zipCode}
        </p>

        <div className="detail-grid mt-4">
          <div className="detail-card">
            <h3>Phone</h3>
            <p>{facility.phone_number || facility.phoneNumber || 'Not listed'}</p>
          </div>
          <div className="detail-card">
            <h3>Website</h3>
            {facility.official_website || facility.officialWebsite ? (
              <a href={facility.official_website || facility.officialWebsite} className="detail-link" target="_blank" rel="noreferrer">
                Visit official site
              </a>
            ) : (
              <p>Not listed</p>
            )}
          </div>
          <div className="detail-card">
            <h3>Map</h3>
            {facility.map ? (
              <a href={facility.map} className="detail-link" target="_blank" rel="noreferrer">
                Open map
              </a>
            ) : (
              <p>Not listed</p>
            )}
          </div>
        </div>

        <div className="action-row mt-5">
          {facility.map && (
            <a href={facility.map} target="_blank" rel="noreferrer" className="btn btn-success me-2">
              Find on Map
            </a>
          )}
          <Link to="/" className="btn btn-outline-secondary">Back to Search</Link>
        </div>
      </div>
    </section>
  );
};

export default FacilityDetail;
