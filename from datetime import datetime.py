from datetime import datetime

def calculate_age(birth_date):
    today = datetime.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    # Adjust for negative values
    if days < 0:
        months -= 1
        days += (datetime(today.year, today.month, 1) - datetime(today.year if today.month > 1 else today.year - 1,
                                                                 today.month - 1 if today.month > 1 else 12, 1)).days

    if months < 0:
        years -= 1
        months += 12

    return years, months, days

def main():
    dob_input = input("Enter your date of birth (YYYY-MM-DD): ")
    try:
        birth_date = datetime.strptime(dob_input, "%Y-%m-%d")
        years, months, days = calculate_age(birth_date)
        print(f"You are {years} years, {months} months, and {days} days old.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")

if __name__ == "__main__":
    main()
