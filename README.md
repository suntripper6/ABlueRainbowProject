# A Blue Rainbow Project

A Blue Rainbow is a care-directory application for families comparing assisted living, home health, skilled nursing, and hospice providers.

## Stack

- Backend: ASP.NET Core 8 Web API with Entity Framework Core and PostgreSQL
- Frontend: Vue 3, Vue Router, Vite, Axios, Bootstrap 5
- Tooling: ESLint flat config, GitHub Actions CI

## Current Capabilities

- Browse multiple facility categories
- Search provider lists by name and address terms
- View facility details and external map or website links
- Submit feedback through the public site

## Local Development

### Prerequisites

- .NET 8 SDK
- Node.js 20.19 or newer
- PostgreSQL

### Backend

The backend now expects the connection string outside source control.

From [ABlueRainbowBackend](ABlueRainbowBackend/):

```bash
dotnet user-secrets set "ConnectionStrings:DefaultConnection" "Host=localhost;Database=abluerainbow;Username=postgres;Password=postgres"
dotnet user-secrets set "Authentication:AdminUsername" "admin"
dotnet user-secrets set "Authentication:AdminPassword" "change-this-password"
dotnet user-secrets set "Authentication:JwtSigningKey" "replace-with-a-long-random-secret"
dotnet run
```

On first startup, those bootstrap admin credentials are hashed and seeded into the database as the initial persisted admin account.

The API runs on `http://localhost:5080` by default and exposes Swagger in development.

### Frontend

Copy the example environment file and start Vite:

```bash
cd frontend
cp .env.example .env.local
npm install
npm run dev
```

The frontend runs on `http://localhost:5173` by default.

## Quality Gates

- Frontend lint: `cd frontend && npm run lint`
- Frontend tests: `cd frontend && npm test`
- Frontend build: `cd frontend && npm run build`
- Backend build: `cd ABlueRainbowBackend && dotnet build`
- Backend tests: `dotnet test ABlueRainbowBackend.Tests/ABlueRainbowBackend.Tests.csproj`

## Notes

- Production CORS origins are configured through `Cors:AllowedOrigins`.
- Admin login is available at `/api/auth/login`, and protected endpoints require a Bearer token.
- Auth now uses a persisted `AdminUser` record store; the configured username and password are only used to seed the first admin account.
- Admin accounts can be managed in-app from `/admin/users`, including creating new admins, deactivating them, and rotating passwords.
- Audit logs are available to admins at `/admin/audit-logs`, with filtering by actor, action type, and date range plus CSV export.
- The repository includes a CI workflow for frontend lint, test, and build plus backend build and test validation.

## Credits

© 2026 A Blue Rainbow
