import React, { useState } from 'react';
import { Form, Button, Alert, Spinner } from 'react-bootstrap';
import { postFeedback } from '../api';

const Feedback = () => {
  const [formData, setFormData] = useState({ name: '', email: '', comments: '' });
  const [status, setStatus] = useState({ type: '', message: '' });
  const [loading, setLoading] = useState(false);

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    postFeedback(formData)
      .then(() => {
        setStatus({ type: 'success', message: 'Thank you for your feedback!' });
        setFormData({ name: '', email: '', comments: '' });
        setLoading(false);
      })
      .catch(() => {
        setStatus({ type: 'danger', message: 'Failed to send feedback. Please try again.' });
        setLoading(false);
      });
  };

  return (
    <section className="page-shell">
      <div className="page-intro">
        <p className="section-kicker">Feedback</p>
        <h1 className="page-title">Tell us what would help families more</h1>
        <p className="page-subtitle">Share ideas, corrections, or gaps in the directory through a calmer feedback form.</p>
      </div>
      
      <div className="panel form-panel mt-4">
        {status.message && <Alert variant={status.type}>{status.message}</Alert>}
        
        <Form onSubmit={handleSubmit} className="form-shell">
          <Form.Group className="mb-4">
            <Form.Label>Your Name</Form.Label>
            <Form.Control 
              type="text" 
              placeholder="How should we address you?"
              value={formData.name}
              onChange={(e) => setFormData({...formData, name: e.target.value})}
              required
            />
          </Form.Group>

          <Form.Group className="mb-4">
            <Form.Label>Email Address</Form.Label>
            <Form.Control 
              type="email" 
              placeholder="Where can we reach you if we have questions?"
              value={formData.email}
              onChange={(e) => setFormData({...formData, email: e.target.value})}
              required
            />
          </Form.Group>

          <Form.Group className="mb-4">
            <Form.Label>Your Comments</Form.Label>
            <Form.Control 
              as="textarea" 
              rows={5} 
              placeholder="What can we improve?"
              value={formData.comments}
              onChange={(e) => setFormData({...formData, comments: e.target.value})}
              required
            />
          </Form.Group>

          <Button 
            variant="secondary" 
            type="submit" 
            className="btn btn-secondary"
            disabled={loading}
          >
            {loading ? <Spinner animation="border" size="sm" /> : 'Send Feedback'}
          </Button>
        </Form>
      </div>
    </section>
  );
};

export default Feedback;
