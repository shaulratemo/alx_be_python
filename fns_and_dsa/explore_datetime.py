from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    days_to_add = input("Enter the number of days to add to the current date: ")
    if days_to_add == '':
        print("You did not enter a number.")
    else:
        days_to_add = int(days_to_add)
        future_date = datetime.now() + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")


def main():
    calculate_future_date()

if __name__ == "__main__":
    main()