import schedule
import time

def remind():
    # Replace this print statement with your reminder message or transaction logic
    print("Don't forget to review your weekly transactions!")

def schedule_weekly_reminder():
    # Schedule the reminder to run every Monday at 9:00 AM
    schedule.every().monday.at("09:00").do(remind)

    # You can adjust the day and time as per your preference

    # Start the schedule loop
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    schedule_weekly_reminder()
