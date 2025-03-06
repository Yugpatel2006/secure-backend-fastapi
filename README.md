# 🔥 FastAPI JWT Authentication with MongoDB 🚀  

[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-blue?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)  
[![MongoDB](https://img.shields.io/badge/MongoDB-6.x-green?style=for-the-badge&logo=mongodb)](https://www.mongodb.com/)  
[![JWT](https://img.shields.io/badge/JWT-Auth-red?style=for-the-badge&logo=jsonwebtokens)](https://jwt.io/)  
[![License](https://img.shields.io/badge/license-MIT-brightgreen?style=for-the-badge)](LICENSE)  

> 🚀 A **secure authentication system** using **FastAPI**, **JWT Tokens**, and **MongoDB**.  
> ✅ Includes **User Registration, Login, Token Refresh & Protected Routes**.  

---

## 🐜 **Table of Contents**
- [✨ Features](#-features)
- [🛠 Tech Stack](#-tech-stack)
- [🚀 Installation & Setup](#-installation--setup)
- [📂 Folder Structure](#-folder-structure)
- [🔑 API Endpoints](#-api-endpoints)
- [🎯 Future Improvements](#-future-improvements)
- [🐜 License](#-license)

---

## ✨ **Features**
✅ **User Registration & Login with JWT Authentication**  
✅ **Secure Password Hashing** using `bcrypt`  
✅ **Access & Refresh Tokens** for session management  
✅ **MongoDB Database Integration** for storing user data  
✅ **FastAPI Dependency Injection for Security**  
✅ **Role-based Access Control (Future Scope)**  

---

## 🛠 **Tech Stack**
🔹 **FastAPI** – High-performance web framework  
🔹 **MongoDB** – NoSQL database  
🔹 **JWT (JSON Web Token)** – Authentication system  
🔹 **bcrypt** – Secure password hashing  
🔹 **Uvicorn** – ASGI server for FastAPI  

---

## 🚀 **Installation & Setup**

### 1️⃣ **Clone the repository**
```bash
git clone https://github.com/Yugpatel2006/secure-backend-fastapi.git
cd secure-backend-fastapi
```

### 2️⃣ **Create a Virtual Environment & Activate**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Set Up Environment Variables**
Create a `.env` file in the root directory and add:
```ini
SECRET_KEY=your_secret_key
MONGO_URI=your_mongodb_uri
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 5️⃣ **Run the FastAPI Server**
```bash
uvicorn main:app --reload
```
🚀 The API will be available at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) (Swagger UI)

---

## 📂 **Folder Structure**
```bash
secure-backend-fastapi/
│-- main.py          # Main FastAPI app
│-- auth/            # Authentication logic
│   ├── jwt_handler.py  # JWT token functions
│   ├── hashing.py      # Password hashing utilities
│   ├── dependencies.py # Security dependencies
│-- models/          # Database models
│-- routes/          # API routes
│-- .env.example     # Example environment file
│-- README.md        # Project documentation
```

---

## 🔑 **API Endpoints**

| Method | Endpoint          | Description                     | Auth Required |
|--------|------------------|---------------------------------|--------------|
| POST   | `/register`      | Register new user              | ❌          |
| POST   | `/login`         | User login (returns JWT)       | ❌          |
| GET    | `/protected-route` | Example of a protected route | ✅          |
| POST   | `/refresh`       | Refresh access token           | ✅          |

📌 Test the API in Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🎯 **Future Improvements**
✅ OAuth2 authentication (Google, GitHub login)  
✅ Role-based access control (Admin, User)  
✅ Two-Factor Authentication (2FA)  
✅ Full CRUD operations  

---

## 🐜 **License**
This project is **MIT Licensed** – Feel free to use and modify!

---

## 🚀 **Like this project?**
⭐ Give it a **star** on GitHub!
🔗 **GitHub Repo:** [https://github.com/Yugpatel2006/secure-backend-fastapi](https://github.com/Yugpatel2006/secure-backend-fastapi)
