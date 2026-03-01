# 🔐 Google OAuth 2.0 Authentication using Flask

This project implements secure user authentication using **Google OAuth 2.0** in a Flask web application. Users can log in with their Google account, and the application retrieves their profile information such as name, email, and profile picture.

---

## 📌 Description

This project demonstrates the complete Google OAuth authentication flow, including:

- Redirecting users to Google login
- Handling authorization callback
- Exchanging authorization code for access token
- Fetching user profile data securely
- Managing authentication in Flask backend

This project is useful for learning real-world authentication systems used in modern web applications.

---

## 🚀 Features

- Google OAuth 2.0 Login
- Secure token exchange
- Retrieve user profile information
- Flask Blueprint modular structure
- Clean and beginner-friendly code
- Ready for database integration

---

## 🛠️ Technologies Used

- Python 3
- Flask
- Requests library
- Google OAuth 2.0 API
- HTML/CSS

---


## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/BHAVIN-Hariyani-001b/Google_OAuth_Authentication_with_Flask.git
cd Google_OAuth_Authentication_with_Flask

```

---

### 2. Create virtual environment
```bash
python -m venv venv
```
- Activate environment:
    - Windows
    ```bash
    venv\Scripts\activate
    ```
    - Linux / Mac
    ```bash
    source venv/bin/activate
    ```
---
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
---
### 4. Configure Google OAuth Credentials
- Go to Google Cloud Console and create OAuth credentials.
Update ```config.py```:

### 5. Run the application

```bash
python run.py
```
- Open browser:
```code
http://localhost:5000
```

### 🔄 OAuth Flow
1. User clicks "Login with Google"
2. Redirect to Google authorization page
3. User grants permission
4. Google sends authorization code
5. Application exchanges code for access token
6. Application fetches user profile data
7. User successfully logged in

### 📊 Example User Data
```json
{
  "id": "123456789",
  "email": "user@gmail.com",
  "name": "John Doe",
  "picture": "profile_url"
}
```


### 🔐 Security Notes

- Never expose your Client Secret publicly
- Use HTTPS in production
- Store tokens securely
- Use environment variables for credentials

### 🎯 Future Improvements

- Database integration (MySQL / PostgreSQL)
- JWT authentication
- Session management
- Logout functionality
- Support multiple OAuth providers

### 📜 License
This project is licensed under the MIT License.

---
If you want, I can also create:

- `requirements.txt`  
- complete Flask OAuth code  
- or advanced version with JWT + database (production-level)
```
---