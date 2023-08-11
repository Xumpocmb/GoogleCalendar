import datetime


def main():
    month = input('month:   ')
    day = input('day:   ')
    hr = input('hr:   ')
    mins = input('mins:   ')
    event_time = f'2023-{month}-{day}T{hr}:{mins}:00+03:00'
    print(event_time)
    print('2023-08-11T10:00:00+03:00')


if __name__ == '__main__':
    main()
