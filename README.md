# A BLUE RAINBOW PROJECT

### An online database and dashboard for elderly care

### This is a centralized, online resource to assist primary caretakers in locating the best possible care for their loved ones.

### Initially the Project will start with 1 county and 1 state.

## PROFESSIONAL LINKS

---

### [LinkedIn](https://www.linkedin.com/in/jason-bundy)

## USER STORIES

---

- As an user/visitor, I want to search by zip code
- As an user/visitor, I want to select types of facility providers
- As an user/visitor, I want to see more details on a selected provider
- As an user/visitor, I want to click on a map hyperlink to locate a provider
- As an user/visitor, I want to provide feedback/comments
- As an user/admin, I want the ability to Create an entry
- As an user/admin, I want the ability to Update an entry
- As an user/admin, I want the ability to Delete an entry

## MVP

---

- Centralized care directory
- Professional UI using React & Bootstrap 5
- Robust backend using ASP.NET Core 8
- PostgreSQL for reliable data storage
- Full CRUD operations on care facilities

## TECHNOLOGIES USED

---

- **Backend**: [ASP.NET Core 8 Web API (C#)](ABlueRainbowBackend/)
- **Frontend**: [React (Vite)](frontend/)
- **Database**: PostgreSQL
- **ORM**: Entity Framework Core 8
- **Styling**: Bootstrap 5

## GETTING STARTED

---

### Prerequisites

- [.NET 8 SDK](https://dotnet.microsoft.com/en-us/download/dotnet/8.0)
- [Node.js](https://nodejs.org/)
- [PostgreSQL](https://www.postgresql.org/)

### Local development

#### 1. Backend Setup

Configure your PostgreSQL connection string in [ABlueRainbowBackend/appsettings.json](ABlueRainbowBackend/appsettings.json).

```bash
cd ABlueRainbowBackend
dotnet run
```
The backend will automatically create the database and seed it with sample data on first run.

#### 2. Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

The application will be available at http://localhost:5174.

## RESOURCES

---

- [W3 SCHOOLS](https://www.w3schools.com/)
- [Microsoft Entity Framework](https://learn.microsoft.com/en-us/ef/core/)
- [React Documentation](https://react.dev/)

## CREDITS

---

- © 2026 A Blue Rainbow
