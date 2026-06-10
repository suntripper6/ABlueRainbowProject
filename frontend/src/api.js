import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api/';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getAssistedLiving = () => api.get('assistedliving/');
export const getAssistedLivingDetail = (id) => api.get(`assistedliving/${id}/`);
export const getHomeHealth = () => api.get('homehealth/');
export const getHomeHealthDetail = (id) => api.get(`homehealth/${id}/`);
export const getSkilledNursing = () => api.get('skillednursing/');
export const getSkilledNursingDetail = (id) => api.get(`skillednursing/${id}/`);
export const getHospice = () => api.get('hospice/');
export const getHospiceDetail = (id) => api.get(`hospice/${id}/`);
export const getProviders = () => api.get('providers/');
export const postFeedback = (data) => api.post('feedback/', data);

export default api;
