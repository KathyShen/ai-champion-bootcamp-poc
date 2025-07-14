import smtplib
from email.message import EmailMessage
import streamlit as st

def send_feedback_email(name, email, message):
    try:
        msg = EmailMessage()
        msg["Subject"] = f"Public Feedback from {name}"
        msg["From"] = "noreply@app.gov.sg"
        msg["To"] = "your_team@gov.sg"
        msg.set_content(f"From: {name} <{email}>\n\nMessage:\n{message}")

        # Simulate sending or use your SMTP config here
        st.success("Feedback sent (simulated). Thank you!")
        # Uncomment below and configure in production
        # with smtplib.SMTP("smtp.gov.sg", 587) as server:
        #     server.login("username", "password")
        #     server.send_message(msg)

    except Exception as e:
        st.error(f"Error sending message: {e}")
