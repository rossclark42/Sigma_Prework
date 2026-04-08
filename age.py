from datetime import datetime


def age_cal(user_date):
    birth_date = datetime.strptime(user_date, "%d-%m-%Y").date()
    today_date = datetime.today().date()
    age = today_date.year - birth_date.year
    if (today_date.month, today_date.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


def get_date():
    day = input("Enter the day: ")
    month = input("Enter the month number: ")
    year = input("Enter the year: ")

    day = day.zfill(2)
    month = month.zfill(2)

    return f"{day}-{month}-{year}"


date_input = get_date()
print(f"Your age is {age_cal(date_input)}.")
