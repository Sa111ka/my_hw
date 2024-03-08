from datetime import datetime , timedelta

#def get_days_from_today():
today = datetime.now() 
day_now = today.date()
past_day = datetime(year=2020, month=10, day=9)
result = past_day.toordinal() - day_now.toordinal()
print(result)
