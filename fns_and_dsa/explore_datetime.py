# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current Date and Time: {formatted_date}")

def calculate_future_date():
    try:
        days = int(input("Enter number of days to add: "))
        future_date = datetime.now() + timedelta(days=days)
        formatted_future = future_date.strftime("%Y-%m-%d")
        print(f"Future Date after {days} days: {formatted_future}")
    except ValueError:
        print("Please enter a valid integer for days.")

def main():
    print("Date and Time Explorer")
    display_current_datetime()
    calculate_future_date()

if __name__ == "__main__":
    main()
