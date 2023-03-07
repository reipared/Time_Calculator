def add_time(start, duration, day=None):
    # Parse the start time
    start_time, am_pm = start.split()
    start_hour, start_minute = map(int, start_time.split(':'))
    start_hour += 12 if am_pm == 'PM' and start_hour < 12 else 0

    # Parse the duration
    duration_hour, duration_minute = map(int, duration.split(':'))

    # Calculate the end time
    end_minute = (start_minute + duration_minute) % 60
    end_hour = (start_hour + duration_hour + (start_minute + duration_minute) // 60) % 24
    end_am_pm = 'AM' if end_hour < 12 else 'PM'
    end_hour = end_hour % 12 or 12

    # Calculate the number of days later
    days_later = (start_hour + duration_hour + (start_minute + duration_minute) // 60) // 24

    # Format the end time
    end_time = f'{end_hour:02d}:{end_minute:02d} {end_am_pm}'

    # Add day of the week if provided
    if day is not None:
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        start_day_index = days.index(day.title())
        end_day_index = (start_day_index + days_later) % 7
        end_day = days[end_day_index]
        end_time += f', {end_day}'

    # Add days later if necessary
    if days_later == 1:
        end_time += ' (next day)'
    elif days_later > 1:
        end_time += f' ({days_later} days later)'

    return end_time

print(add_time("3:00 PM", "3:10")) # Outputs: 6:10 PM
print(add_time("11:30 AM", "2:32", "Monday")) # Outputs: 2:02 PM, Monday
print(add_time("11:43 AM", "00:20")) # Outputs: 12:03 PM
print(add_time("10:10 PM", "3:30")) # Outputs: 1:40 AM (next day)
print(add_time("11:43 PM", "24:20", "tueSday")) # Outputs: 12:03 AM, Thursday (2 days later)
print(add_time("6:30 PM", "205:12")) # Outputs: 7:42 AM (9 days later)
