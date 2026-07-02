import { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { Spinner, Alert, Pagination, Form, InputGroup } from 'react-bootstrap';

const FacilityList = ({ title, subtitle, kicker, fetchData, detailPath }) => {
  const [facilities, setFacilities] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [page, setPage] = useState(1);
  const [totalPages, setTotalPages] = useState(1);
  const [count, setCount] = useState(0);
  const [search, setSearch] = useState('');
  const [debouncedSearch, setDebouncedSearch] = useState('');

  // Debounce search term
  useEffect(() => {
    const handler = setTimeout(() => {
      if (search !== debouncedSearch) {
        setLoading(true);
        setDebouncedSearch(search);
        setPage(1);
      }
    }, 500);

    return () => clearTimeout(handler);
  }, [search, debouncedSearch]);

  // Fetch data on page or debounced search change
  useEffect(() => {
    let active = true;

    fetchData({ page, search: debouncedSearch })
      .then(response => {
        if (active) {
          setFacilities(response.data.results || []);
          setCount(response.data.count || 0);
          setTotalPages(Math.ceil((response.data.count || 0) / 10));
          setLoading(false);
        }
      })
      .catch(() => {
        if (active) {
          setError(`Failed to fetch ${title.toLowerCase()}.`);
          setLoading(false);
        }
      });

    return () => {
      active = false;
    };
  }, [page, debouncedSearch, fetchData, title]);

  const handleSearchChange = (e) => {
    setSearch(e.target.value);
  };

  const handlePageChange = (newPage) => {
    setLoading(true);
    setPage(newPage);
  };

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
              <span className="count-pill">{count} facilities</span>
            </div>
          </div>
        </div>
      </div>

      <div className="mb-4">
        <InputGroup className="max-w-md">
          <InputGroup.Text className="bg-white border-end-0">
            <i className="bi bi-search"></i>
          </InputGroup.Text>
          <Form.Control
            placeholder="Search by name, city, address..."
            value={search}
            onChange={handleSearchChange}
            className="border-start-0 ps-0"
          />
        </InputGroup>
      </div>

      <div className="panel table-panel position-relative">
        {loading && (
          <div className="position-absolute w-100 h-100 top-0 start-0 d-flex justify-content-center align-items-center bg-white bg-opacity-75 z-index-10">
            <Spinner animation="border" variant="primary" />
          </div>
        )}
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
                      <strong>No {title.toLowerCase()} match your search</strong>
                      <p>Try adjusting your search terms or filters.</p>
                    </div>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

      {totalPages > 1 && (
        <div className="d-flex justify-content-center mt-4">
          <Pagination>
            <Pagination.First onClick={() => handlePageChange(1)} disabled={page === 1} />
            <Pagination.Prev onClick={() => handlePageChange(page - 1)} disabled={page === 1} />
            {[...Array(totalPages).keys()].map(num => (
              <Pagination.Item
                key={num + 1}
                active={num + 1 === page}
                onClick={() => handlePageChange(num + 1)}
              >
                {num + 1}
              </Pagination.Item>
            ))}
            <Pagination.Next onClick={() => handlePageChange(page + 1)} disabled={page === totalPages} />
            <Pagination.Last onClick={() => handlePageChange(totalPages)} disabled={page === totalPages} />
          </Pagination>
        </div>
      )}
    </section>
  );
};

export default FacilityList;
