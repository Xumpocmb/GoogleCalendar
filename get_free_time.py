from datetime import datetime
from schedule import set_schedule


# функция нахождения свободных окошек для записи
def find_free_time():
    # считываем ближайшиеи записи из файла
    with open('events-list.txt', 'r', encoding='utf-8') as file:
        events = file.read().split('\n')
    print(events)

    # сортировка событий по датам
    event_dates = {}
    for event in events:
        if not event == '':
            event_date = datetime.fromisoformat(event).date()
            if event_date in event_dates:
                event_dates[event_date].append(event)
            else:
                event_dates[event_date] = [event]

    # нахождение записей на текущий день
    print('ивенты на сегодня')
    today_events = event_dates.get(datetime.fromisoformat(datetime.today().isoformat()).date(), None)
    print(today_events)

    # запись в файл событий текущего дня
    with open('today_events.txt', 'w', encoding='utf-8') as file:
        file.write('\n'.join(today_events))

    # получаем список часов рабочего дня
    hours_for_work = [datetime.fromisoformat(event).hour for event in set_schedule()]
    for event in today_events:
        event_hr = datetime.fromisoformat(event).hour
        # удаление часов на которые уже есть записи
        if event_hr in hours_for_work:
            hours_for_work.remove(event_hr)

    print('Свободные часы')
    print(hours_for_work)


if __name__ == '__main__':
    find_free_time()
