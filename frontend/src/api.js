import axios from 'axios';

const API_BASE_URL = 'http://localhost:5080/api/';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getAssistedLiving = (params) => api.get('assistedliving/', { params });
export const getAssistedLivingDetail = (id) => api.get(`assistedliving/${id}/`);
export const getHomeHealth = (params) => api.get('homehealth/', { params });
export const getHomeHealthDetail = (id) => api.get(`homehealth/${id}/`);
export const getSkilledNursing = (params) => api.get('skillednursing/', { params });
export const getSkilledNursingDetail = (id) => api.get(`skillednursing/${id}/`);
export const getHospice = (params) => api.get('hospice/', { params });
export const getHospiceDetail = (id) => api.get(`hospice/${id}/`);
export const getProviders = () => api.get('providers/');
export const postFeedback = (data) => api.post('feedback/', data);

export default api;
