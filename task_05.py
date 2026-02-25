from datetime import datetime, timedelta

def date_in_future(num):
    now_date = datetime.now()
    if not isinstance(num, int):
        return now_date.strftime('%d-%m-%Y %H:%M:%S')

    new_date = now_date + timedelta(days=num)
    return new_date.strftime('%d-%m-%Y %H:%M:%S')
