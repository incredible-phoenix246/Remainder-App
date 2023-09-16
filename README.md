# Schedule Reminder Script

A Python script for scheduling and sending reminders via SMS using Twilio.

## Table of Contents

- [Schedule Reminder Script](#schedule-reminder-script)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Features](#features)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
  - [Usage](#usage)

## Description

The Schedule Reminder Script is a Python program that allows users to schedule reminders for specific dates and times. Reminders can include custom messages, and they are sent as SMS messages to a designated phone number using Twilio.

## Features

- Schedule one-time or recurring reminders.
- Customizable reminder messages.
- SMS notifications using Twilio.

## Getting Started

Follow these steps to get started with the Schedule Reminder Script.

### Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.x
- A Twilio account with Account SID, Auth Token, and a Twilio phone number.
- The `twilio` Python package. You can install it using `pip install twilio`.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/schedule-reminder.git
    ```

2. Navigate to the project folder:

    ```
    cd schedule-reminder
    ```

3.  Edit the configuration file named config.py with your Twilio credentials and phone numbers:
    
    ```
    config.py
    TWILIO_ACCOUNT_SID = 'your_account_sid'
    TWILIO_AUTH_TOKEN = 'your_auth_token'
    TWILIO_PHONE_NUMBER = 'your_twilio_phone_number'
    RECIPIENT_PHONE_NUMBER = 'recipient_phone_number'
    ```

4. Run the script

    ```
    python schedule_reminder.py
    ```

5. Usage

    Run the script using the steps above.
    Use the menu to add schedules and start the reminder loop.
    Customize reminder messages and frequencies as needed.