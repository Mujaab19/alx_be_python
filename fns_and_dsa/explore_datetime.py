from datetime import datetime, timedelta

def display_current_datetime():
    """
    Gets the current date and time, saves it in current_date,
    prints it in YYYY-MM-DD HH:MM:SS format, and returns it.
    """
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

def calculate_future_date(current_date, days_to_add):
    """
    Calculates future_date by adding days_to_add (an int) to current_date,
    prints it in YYYY-MM-DD format, and returns the future_date.
    """
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d"))
    return future_date

def main():
    # Part 1: show current date/time and keep the value in current_date
    current_date = display_current_datetime()

    # Part 2: ask user for an integer number of days to add
    user_input = input("Enter the number of days to add to the current date: ")
    try:
        days = int(user_input)
    except ValueError:
        print("Invalid input. Please enter an integer number of days (e.g. 10).")
        return

    # calculate and print the future date
    calculate_future_date(current_date, days)

if __name__ == "__main__":
    main()
