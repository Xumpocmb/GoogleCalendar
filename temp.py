from datetime import datetime, timedelta

# date_string = '2023-08-11T14:00:00+03:00'
# date = datetime.fromisoformat(date_string)
# new_date = date + timedelta(hours=1)
#
# new_date_string = new_date.isoformat()
# print(new_date_string)


date_strings = ['2023-08-11T14:00:00+03:00', '2023-08-11T16:00:00+03:00', '2023-08-11T18:00:00+03:00']
dates = [datetime.fromisoformat(date_string) for date_string in date_strings]
date1 = '2023-08-11T14:00:00+03:00'
date2 = '2023-08-11T16:00:00+03:00'
hour = datetime.fromisoformat(date1).hour

hours_between = []
for i in range(len(dates) - 1):
    start_date = dates[i]
    end_date = dates[i + 1]
    hours = (end_date - start_date).total_seconds() / 3600
    hours_between.append(hours)

print(hours_between)