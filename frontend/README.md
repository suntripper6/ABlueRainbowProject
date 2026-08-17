# Frontend

This frontend is a Vue 3 and Vite application for browsing elder-care resources.

## Commands

```bash
npm install
npm run dev
npm run lint
npm test
npm run build
```

## Environment

Create `.env.local` from `.env.example`.

```bash
cp .env.example .env.local
```

Available variables:

- `VITE_API_BASE_URL`: Base URL for the backend API, for example `http://localhost:5080/api`

## Tech Notes

- Vue 3 with single-file components
- Vue Router for navigation
- Axios for API requests
- Bootstrap 5 for layout and components
- Admin sign-in uses the backend `/api/auth/login` endpoint and stores the JWT in local storage
- Authenticated admins can create facilities at `/admin/facilities/new` and edit or delete them from detail pages
- Authenticated admins can manage other admin accounts at `/admin/users`
- Authenticated admins can review, filter, and export audit events at `/admin/audit-logs`
