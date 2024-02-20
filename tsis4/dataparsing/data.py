import datetime

# Function to subtract five days from current date
def subtract_five_days():
    current_date = datetime.datetime.now()
    five_days_ago = current_date - datetime.timedelta(days=5)
    return five_days_ago

# Function to print yesterday, today, and tomorrow
def print_yesterday_today_tomorrow():
    today = datetime.datetime.now().date()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    print("Yesterday:", yesterday)
    print("Today:", today)
    print("Tomorrow:", tomorrow)

# Function to drop microseconds from datetime
def drop_microseconds(dt):
    dt_without_microseconds = dt.replace(microsecond=0)
    return dt_without_microseconds

# Function to calculate the difference between two dates in seconds
def date_difference_seconds(date1, date2):
    difference = date1 - date2
    difference_seconds = difference.total_seconds()
    return abs(difference_seconds)

if __name__ == "__main__":
    # Subtract five days from current date
    print("Five days ago from now:", subtract_five_days())

    # Print yesterday, today, and tomorrow
    print("\nYesterday, today, and tomorrow:")
    print_yesterday_today_tomorrow()

    # Drop microseconds from datetime
    current_datetime = datetime.datetime.now()
    print("\nCurrent datetime with microseconds:", current_datetime)
    print("Current datetime without microseconds:", drop_microseconds(current_datetime))

    # Calculate the difference between two dates in seconds
    date1 = datetime.datetime(2024, 2, 10, 12, 0, 0)
    date2 = datetime.datetime(2024, 2, 5, 12, 0, 0)
    print("\nDifference between", date1, "and", date2, "in seconds:", date_difference_seconds(date1, date2))
