from datetime import datetime , timedelta



def get_days_from_today(past_day):
    today = datetime.now() 
    day_now = today.date()
    past_day = datetime.strptime(date, "%Y-%m-%d").date()
    result = past_day.toordinal() - day_now.toordinal()
    return result
    
date = input("Enter the date in YYYY-MM-DD format: ")
get_days_from_today(date)