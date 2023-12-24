'''
Given a time in -hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
Example
s='12:01:00PM'
Return '12:01:00'

s='12:01:00AM'
Return '00:01:00'

s='07:05:45PM'
Return '19:05:45'.
'''
def time_conversion(time_12_hours):
    print(f"Input time : {time_12_hours}")
    time_component = time_12_hours[:-2].split(':')
    print(f"Split Time Components : {time_component}")
    hours, mins,secs = map(int,time_component)
    period = time_12_hours[-2:]
    print(f"Period od the time: {period}")
    if period.upper() == 'PM' and hours != 12:
        hours += 12
    elif period.upper() == 'AM' and hours == 12:
        hours = 0
    time_24_hors = "{:02d}:{:02d}:{:02d}".format(hours,mins,secs)
    print(time_24_hors)




time_12_hours='1:05:45PM'
time_conversion(time_12_hours)
