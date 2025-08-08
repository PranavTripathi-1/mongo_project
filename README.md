# 📚 MongoDB + FastAPI Clean Architecture API

Hey there! 👋  
This is my small project where I tried to connect **FastAPI** with **MongoDB** and follow a bit of **Clean Architecture** (because my seniors keep saying “write clean code” 😅).  

It’s super simple:
- You can **add** a record (like name, email).
- You can **get** the record back by searching with name or email.
- It also tells you **which database & collection** the data is stored in.

## 🛠 Tech Stack
- **Python 3.10+**
- **FastAPI** (Backend framework)
- **MongoDB** (Database)
- **Pydantic** (For data validation)
- **Uvicorn** (ASGI server)

## 📂 Project Structure

mongo_clean_api/
├── app/
│ ├── api/ # API routes
│ │ └── v1/
│ │ └── entity.py
│ ├── core/ # Config & constants
│ │ └── config.py
│ ├── models/ # Pydantic schemas
│ │ └── entity.py
│ ├── repository/ # DB access functions
│ │ └── mongo_repo.py
│ ├── services/ # Business logic
│ │ └── entity_service.py
│ └── main.py # App entry point
└── requirements.txt

## 🚀 How to Run (Local)

### 1️⃣ Clone the Repo
```bash
git clone https://github.com/your-username/mongo-clean-api.git
cd mongo-clean-api
