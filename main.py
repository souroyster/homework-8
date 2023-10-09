from datetime import date, timedelta, datetime
from collections import defaultdict

current_date = date.today()
last_date = current_date + timedelta(7)

def get_period(current_date: date, days: int):
    result = {}
    for _ in range(days + 1):
        result[current_date.day, current_date.month] = current_date.year
        current_date += timedelta(1)
    return result

def get_birthdays_per_week(users: list) -> list:
    res = defaultdict(list)
    current_date = date.today()
    period = get_period(current_date, 7)

    if not users:
        res = {}
        return res
    for user in users:
        bd: date = user["birthday"]
        date_bd = bd.day, bd.month
        if date_bd in list(period):
            date_bd_week = bd.replace(
                year=period[date_bd])
            bd__weekday = date_bd_week.weekday()
            if bd__weekday in (5, 6):
                res["Monday"].append(user["name"])
            else:
                res[date_bd_week.strftime("%A")].append(user["name"])
    return res

if __name__ == "__main__":
    users = [
        {"name": "Bill Gates", "birthday": datetime(2023, 10, 8).date()},
        {"name": "Jan Doe", "birthday": datetime(1980, 12, 15).date()},
        {"name": "Harry Potter", "birthday": datetime(1994, 9, 1).date()},
        {"name": "Stepan Bandera", "birthday": datetime(1980, 1, 2).date()},
        {"name": "Dart Vaider", "birthday": datetime(2001, 2, 5).date()},
        {"name": "Walter White", "birthday": datetime(1965, 4, 11).date()},
        {"name": "Chicken Rooster", "birthday": datetime(1991, 3, 12).date()},
    ]
    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
    get_period(current_date, 7)