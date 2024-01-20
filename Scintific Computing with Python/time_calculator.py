# am pm days
hour_in_day = 24
minutes_in_hour = 60

def time_splitter(time):
    meridiem = ''
    try:
        time, meridiem = time.split(' ')
    except:
        pass
    hour, minutes = time.split(':')
    return int(hour), int(minutes), meridiem;

def minute_converter(start_minutes, duration_minutes):
    hour_flag = 0
    new_minutes = start_minutes + duration_minutes
    if new_minutes > minutes_in_hour:
        hour_flag = new_minutes // minutes_in_hour
        new_minutes = new_minutes % minutes_in_hour
    return new_minutes, hour_flag

def hour_converter(start_hour, duration_hour, hour_flag):
    days_passed = 0
    new_hour = start_hour + duration_hour + hour_flag
    if new_hour > 24:
        days_passed = new_hour // hour_in_day
        new_hour = new_hour % hour_in_day
    return new_hour, days_passed

def day_calculator(day_index, days_passed):

    # new_day_index = (start_day_index + days_to_add) % len(valid_days)
    try:
        new_day_index = (day_index + days_passed) % 7
    except:
        new_day_index = day_index
    return new_day_index

def convert24to12(hours, minutes):
    minutes = str(minutes).zfill(2)
    if hours == 0 and int(minutes) < 60:
        hours += 12
        return hours, minutes, 'AM'
    elif hours < 12 and int(minutes) < 60:
        return hours, minutes, 'AM'
    elif hours == 12 and int(minutes) < 60:
        return hours, minutes, 'PM'
    else:
        hours -= 12
        return hours, minutes, 'PM'

def add_time(start, duration, day = ''):

    # to split time format :- '3:30{ AM}'
    start_hour, start_minutes, start_meridiem =  time_splitter(start)
    if start_meridiem == 'PM':
        start_hour += 12
    # print(start_hour, start_minutes, start_meridiem)

    duration_hour, duration_minutes, duration_meridiem =  time_splitter(duration)
    # print(duration_hour, duration_minutes, duration_meridiem)

    converted_minutes, hour_flag = minute_converter(start_minutes, duration_minutes)
    # print(converted_minutes, hour_flag)

    converted_hour, days_passed = hour_converter(start_hour, duration_hour, hour_flag)
    # print(converted_hour, converted_minutes, days_passed)

    days_in_week = {0:'Sunday', 1:'Monday', 2:'Tuesday', 3:'Wednesday', 4:'Thursday', 5:'Friday', 6:'Saturday'}

    day_index = { 'sunday': 0, 'monday': 1, 'tuesday': 2, 'wednesday': 3, 'thursday': 4, 'friday': 5, 'saturday': 6}.get(day.lower())
    # print(day_index)

    new_day_index = day_calculator(day_index, days_passed)
    # print(days_in_week[new_day_index])

    try:
        the_day = days_in_week[new_day_index]
    except:
        the_day = ''

    reconverted_hour, reconverted_minutes, reconverted_meridiem = convert24to12(converted_hour, converted_minutes)
    # print(reconverted_hour, reconverted_minutes, reconverted_meridiem, days_passed,the_day)

    result_time = f'{reconverted_hour}:{reconverted_minutes} {reconverted_meridiem}'

    if day:
        result_time += f', {the_day}'

    if days_passed > 0 and days_passed <= 1:
        result_time += f' (next day)'
    elif days_passed > 1:
        result_time += f' ({days_passed} days later)'


    return result_time

print(add_time("11:43 PM", "0:60", "tueSday"))