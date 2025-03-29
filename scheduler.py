from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from database import get_users
from weather import get_weather
from emailer import send_email
from llm import generate_message

# Global variable to prevent multiple scheduler instances
scheduler_started = False

def notify_user(username, email, location, frequency, preferred_time, language):
    """
    Fetches weather data and sends an email notification to the user.
    """
    try:
        weather = get_weather(location)
        if weather:
            # Generate a personalized message using the language model
            message = generate_message(username, weather, language)
            # Send the email notification
            send_email(
                subject=f"Weather Update for {location}",
                receiver_email=email,
                body=message
            )
            print(f"Notification sent successfully to {username} ({email}) for location {location}")
        else:
            print(f"No weather data available for location: {location}")
    except Exception as e:
        print(f"Error while notifying {username} ({email}): {e}")

def schedule_notifications():
    """
    Schedules email notifications based on user preferences.
    """
    global scheduler_started
    if scheduler_started:
        print("Scheduler is already running.")
        return
    
    scheduler = BackgroundScheduler()
    users = get_users()

    if not users:
        print("No users found in the database to schedule notifications.")
        return

    for user in users:
        try:
            # Extract user data
            username, email, location, frequency, preferred_time, language = (
                user[1],
                user[2],
                user[3],
                user[4],
                user[5],
                user[6],
            )

            hour, minute = map(int, preferred_time.split(":"))

            # Schedule notifications based on user preferences
            if frequency.lower() == "daily":
                scheduler.add_job(
                    notify_user,
                    trigger=CronTrigger(hour=hour, minute=minute),
                    args=[username, email, location, frequency, preferred_time, language],
                    id=f"{email}_{location}_daily"
                )
                print(f"Scheduled daily notification for {username} at {preferred_time}.")
            elif frequency.lower() == "weekly":
                scheduler.add_job(
                    notify_user,
                    trigger=CronTrigger(day_of_week="mon", hour=hour, minute=minute),
                    args=[username, email, location, frequency, preferred_time, language],
                    id=f"{email}_{location}_weekly"
                )
                print(f"Scheduled weekly notification for {username} at {preferred_time}.")
            else:
                print(f"Invalid frequency {frequency} for user {username}. Skipping.")
        except Exception as e:
            print(f"Error scheduling notification for user {user}: {e}")

    scheduler.start()
    scheduler_started = True
    print("Scheduler started successfully.")
