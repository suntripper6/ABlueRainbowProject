import axios from 'axios';
import { authState, clearAuthSession } from './auth';

const API_BASE_URL = (import.meta.env.VITE_API_BASE_URL || 'http://localhost:5080/api').replace(/\/+$/, '');

const api = axios.create({
  baseURL: `${API_BASE_URL}/`,
  headers: {
    'Content-Type': 'application/json',
  },
});

api.interceptors.request.use((config) => {
  if (authState.token) {
    config.headers.Authorization = `Bearer ${authState.token}`;
  }

  return config;
});

api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401 && authState.token) {
      clearAuthSession();
    }

    return Promise.reject(error);
  },
);

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
export const loginAdmin = (credentials) => api.post('auth/login', credentials);
export const createFacility = (resourcePath, data) => api.post(`${resourcePath}/`, data);
export const getAdminUsers = () => api.get('admin/users/');
export const createAdminUser = (data) => api.post('admin/users/', data);
export const updateAdminUser = (id, data) => api.put(`admin/users/${id}`, data);
export const rotateAdminUserPassword = (id, data) => api.put(`admin/users/${id}/password`, data);
export const getAdminAuditLogs = (params) => api.get('admin/audit-logs/', { params });
export const exportAdminAuditLogs = (params) => api.get('admin/audit-logs/', {
  params: { ...params, format: 'csv' },
  responseType: 'blob',
});
export const updateFacility = (resourcePath, id, data) => api.put(`${resourcePath}/${id}/`, data);
export const deleteFacility = (resourcePath, id) => api.delete(`${resourcePath}/${id}/`);

export default api;
