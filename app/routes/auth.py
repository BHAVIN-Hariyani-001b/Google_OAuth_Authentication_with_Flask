from flask import Blueprint, render_template, redirect, request, url_for
import requests
from app.config import Config as auth

auth_bp = Blueprint('auth', __name__)

CLIENT_ID = auth.CLIENT_ID
CLIENT_SECRET = auth.CLIENT_SECRET
REDIRECT_URI = auth.REDIRECT_URI


# Home page
@auth_bp.route('/')
def home():
    """home page"""
    return render_template('index.html')


# Login route → redirect to Google
@auth_bp.route('/login')
def login():
    """login route redirect to google signIn/signUp"""
    google_url = (
        "https://accounts.google.com/o/oauth2/v2/auth"
        f"?client_id={CLIENT_ID}"
        f"&redirect_uri={REDIRECT_URI}"
        "&response_type=code"
        "&scope=openid email profile"
        "&access_type=offline"
        "&prompt=consent"
    )
    return redirect(google_url)

# Callback route ← Google redirects here
@auth_bp.route('/callback')
def callback():
    """callback rounte google page is redirect to callback and this callback is redirect profile page"""
    code = request.args.get("code")

    if not code:
        return "Error: No code received"

    token_url = auth.TOKEN_URI

    data = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "redirect_uri": REDIRECT_URI,
        "grant_type": "authorization_code"
    }

    token_response = requests.post(token_url, data=data).json()
    print(token_response)
    access_token = token_response.get("access_token")

    if not access_token:
        return f"Error getting token: {token_response}"

    print("Access Token:", access_token)

    userinfo = requests.get(
        "https://www.googleapis.com/oauth2/v2/userinfo",
        headers={"Authorization": f"Bearer {access_token}"}
    ).json()

    print("User Info:", userinfo)

    return render_template("profile.html", user=userinfo)