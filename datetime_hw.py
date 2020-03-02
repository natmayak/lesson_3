from datetime import datetime, timedelta
today = datetime.now()
delta = timedelta(days=1)
yesterday = today - delta
yesterday
datetime.datetime(2020, 2, 28, 11, 44, 0, 57526)
delta_month = timedelta(days=30)
month_ago = today - delta_month
month_ago
datetime.datetime(2020, 1, 30, 11, 44, 0, 57526)
today.strftime('%A %d %B %Y')
'Saturday 29 February 2020'
text_date = '12/15/2019'
text_date_converted = datetime.strptime(text_date, '%m/%d/%Y')
text_date_converted
datetime.datetime(2019, 12, 15, 0, 0)



# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime