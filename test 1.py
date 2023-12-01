def get_days_in_month(month):
    month_days = {
        "January": 31,
        "February": 28,
        "March": 31,
        "April": 30,
        "May": 31,
        "June": 30,
        "July": 31,
        "August": 31,
        "September": 30,
        "October": 31,
        "November": 30,
        "December": 31
    }

    return month_days.get(month, None)


def main():
    month = input("january")

    days = get_days_in_month(month)
    if days:
        print(f"{month} has {days} days.")
    else:
        print("Invalid month. Please enter a valid month name.")

if __name__ == "__main__":
    main()

