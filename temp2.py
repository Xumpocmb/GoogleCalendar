from datetime import datetime, timedelta

dates = ['2023-08-11T14:00:00+03:00', '2023-08-11T16:00:00+03:00', '2023-08-11T18:00:00+03:00']
hours_between = []

for i in range(len(dates) - 1):
    start_date = datetime.fromisoformat(dates[i])
    end_date = datetime.fromisoformat(dates[i + 1])
    hours = [start_date.hour]

    while start_date < end_date:
        start_date += timedelta(hours=1)
        hours.append(start_date.hour)

    hours_between.extend(hours)

print(hours_between)
