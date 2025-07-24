import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import smtplib
import ssl
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

app = Flask(__name__)
CORS(app) # Enable CORS for frontend communication

# --- Configuration from Environment Variables ---
# Ensure these are set in your .env file:
# YOUTUBE_API_KEY="YOUR_YOUTUBE_API_KEY_HERE"
# SENDER_EMAIL="your_email@example.com"
# SENDER_EMAIL_PASSWORD="your_email_app_password_here"
# RECIPIENT_EMAIL="destination_email@example.com"

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
CHANNEL_ID = 'UCjhAWGLaxd124jxAdD_digQ'

SENDER_EMAIL = os.getenv("SENDER_EMAIL")
SENDER_EMAIL_PASSWORD = os.getenv("SENDER_EMAIL_PASSWORD")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL")

# --- YouTube API Endpoint ---
@app.route('/api/latest-video', methods=['GET'])
def get_latest_youtube_video():
    if not YOUTUBE_API_KEY:
        return jsonify({"error": "YouTube API key not configured."}), 500

    youtube_api_url = (
        f"https://www.googleapis.com/youtube/v3/search?"
        f"key={YOUTUBE_API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=1"
    )

    try:
        response = requests.get(youtube_api_url)
        response.raise_for_status()
        data = response.json()

        if data.get('items') and len(data['items']) > 0:
            return jsonify({"videoId": data['items'][0]['id']['videoId']})
        else:
            return jsonify({"message": "No videos found."}), 404
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YouTube video: {e}")
        return jsonify({"error": "Failed to fetch video."}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error."}), 500

# --- Contact Form Endpoint ---
@app.route('/api/contact', methods=['POST'])
def handle_contact_form():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not all([name, email, message]):
        return jsonify({"error": "All fields are required."}), 400

    if not (SENDER_EMAIL and SENDER_EMAIL_PASSWORD and RECIPIENT_EMAIL):
        return jsonify({"error": "Email credentials not configured."}), 500

    subject = f"New Contact Form Message from {name}"
    email_body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

    try:
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(SENDER_EMAIL, SENDER_EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, RECIPIENT_EMAIL, f"Subject: {subject}\n\n{email_body}")
        return jsonify({"message": "Message sent successfully!"}), 200
    except smtplib.SMTPAuthenticationError:
        return jsonify({"error": "Email authentication failed. Check credentials."}), 500
    except smtplib.SMTPException as e:
        print(f"SMTP error: {e}")
        return jsonify({"error": "Failed to send email."}), 500
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return jsonify({"error": "Internal server error."}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
