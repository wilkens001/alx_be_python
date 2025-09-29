from datetime import datetime, timedelta

def display_current_datetime():
    """
    Display the current date and time in a readable format.
    Returns the current date for use in other functions.
    """
    current_date = datetime.now()
    print(f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date

def calculate_future_date(current_date):
    """
    Calculate and display a future date based on user input.
    Args:
        current_date: The current datetime to add days to
    """
    # Get number of days from user
    days = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate future date
    future_date = current_date + timedelta(days=days)
    
    # Display the future date
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")

def main():
    # Get and display current datetime
    current_date = display_current_datetime()
    
    # Calculate and display future date
    calculate_future_date(current_date)

if __name__ == "__main__":
    main()