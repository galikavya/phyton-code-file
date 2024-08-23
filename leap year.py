def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def anniversary_date(date_str):
    day, month, year = map(int, date_str.split('/'))
     
    if is_leap_year(year):
        next_anniversary = year + 1
        print(f"Given Anniversary Year: Leap Year. Anniversary Date: {day:02}/{month:02}/{next_anniversary}")
    else:
        previous_anniversary = year - 1
        print(f"Given Anniversary Year: Non Leap Year. Anniversary Date: {day:02}/{month:02}/{previous_anniversary}")

input_date = input("Enter Date (DD/MM/YYYY): ")
anniversary_date(input_date)
