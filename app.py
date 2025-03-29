import streamlit as st
from database import init_db, add_user, check_email_location
from scheduler import schedule_notifications


# Initialize the database
init_db()

# Streamlit UI
st.title("🌤️ Weather Forecast Notifier Setup")

st.subheader("📋 Enter your details to receive personalized weather updates:")

# Input fields
username = st.text_input("👤 Username")
email = st.text_input("✉️ Email")
location = st.text_input("📍 Location")
frequency = st.selectbox("⏰ Frequency", ["Daily", "Weekly"])
preferred_time = st.time_input("🕒 Preferred Notification Time")
language = st.selectbox("🌐 Language", ["English", "Spanish", "French", "German", "Others"])

# Submit button
if st.button("Submit"):
    if not username or not email or not location:
        st.error("❌ All fields are required!")
    else:
        # Check for existing email-location pair
        if check_email_location(email, location):
            st.error("❌ This email is already subscribed for this location!")
        else:
            # Add user to the database
            add_user(username, email, location, frequency, preferred_time.strftime("%H:%M"), language)
            st.success(
                f"✅ Details saved! You'll receive {frequency.lower()} weather updates for {location} at {preferred_time} in {language}."
            )
            schedule_notifications()
