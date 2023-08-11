from datetime import datetime, timedelta


def set_schedule():
    # start_hour = int(input('Введите час начала работы (к примеру: 10): '))
    # end_hour = int(input('Введите час начала работы (к примеру: 10): '))

    start_work = datetime.now().replace(hour=10, minute=0, second=0, microsecond=0)
    end_work = start_work.replace(hour=18)

    hours_for_work = []
    while start_work <= end_work:
        hours_for_work.append(start_work.isoformat())
        start_work += timedelta(hours=1)

    return hours_for_work


if __name__ == '__main__':
    set_schedule()
