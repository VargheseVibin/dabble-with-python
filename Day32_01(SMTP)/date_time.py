import datetime as dt

now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()
print(f"Year={year}")
print(f"Day Of week:{day_of_week}")

dob = dt.datetime(year=1980, month=12, day=31, hour=4, minute=45, second=58, microsecond=2568)
print(dob)


