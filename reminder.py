import datetime
import time
from twilio.rest import Client
import threading

# Twilio credentials
TWILIO_ACCOUNT_SID = 'your_account_sid'
TWILIO_AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
RECIPIENT_PHONE_NUMBER = 'recipient_phone_number'  # Designated phone number

# Define a list to store events
events = []

def reminder(event):
    event_date, message, frequency = event
    current_time = datetime.datetime.now()

    if current_time >= event_date:
        print(f"Reminder: {message} was scheduled for {event_date.strftime('%Y-%m-%d %H:%M')}")
        send_sms(f"{message} - {event_date.strftime('%Y-%m-%d %H:%M')}", RECIPIENT_PHONE_NUMBER)
        events.remove(event)
    else:
        time_left = event_date - current_time
        print(f"Reminder: {message} is scheduled for {event_date.strftime('%Y-%m-%d %H:%M')}. Time left: {time_left}")

    # Reschedule the reminder based on the frequency
    if frequency > 0:
        event_date += datetime.timedelta(minutes=frequency)
        events.append((event_date, message, frequency))

def send_sms(message, recipient):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=recipient
    )

def add_schedule():
    date_str = input("Enter the date and time (YYYY-MM-DD HH:MM): ")
    message = input("Enter a reminder message: ")
    frequency = int(input("Enter the frequency in minutes (0 for no repetition): "))
    
    try:
        event_date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M")
        events.append((event_date, message, frequency))
        print("Schedule added successfully.")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD HH:MM.")

def main():
    while True:
        for event in events[:]:
            reminder(event)
        time.sleep(60)  # Check every 60 seconds

if __name__ == "__main__":
    print("Schedule Reminder Script")
    while True:
        print("\nMenu:")
        print("1. Add Schedule")
        print("2. Start Reminder")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_schedule()
        elif choice == '2':
            main_thread = threading.Thread(target=main)
            main_thread.start()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
