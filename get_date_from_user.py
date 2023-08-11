from datetime import datetime


def get_time():
    start_time = datetime.fromisoformat("2023-08-11T10:00:00+03:00")
    end_time = datetime.fromisoformat("2023-08-11T10:59:00+03:00")

    time_difference = end_time - start_time
    print(datetime.fromisoformat("2023-08-11T10:00:00+03:00").time())
    print(datetime.fromisoformat("2023-08-11T10:00:00+03:00").date())
    print(time_difference)


def main():
    month = input('month:   ')
    day = input('day:   ')
    hr = input('hr:   ')
    mins = input('mins:   ')
    event_time = f'2023-{month}-{day}T{hr}:{mins}:00+03:00'
    print(event_time)
    print('2023-08-11T10:00:00+03:00')


if __name__ == '__main__':
    get_time()
