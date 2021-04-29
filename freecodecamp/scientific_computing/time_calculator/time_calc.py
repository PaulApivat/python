# function add_time takes two required parameters, one optional parameter

# start time ending in AM or PM
# duration time in Hours:Minutes
# (optional) a starting day of the week, case INsensitive

def add_time(start, duration, optional_start_day=False):

    # Start time is valid
    # split start w/ .split() function - results in list with two strings ['hour:minute', 'AM/PM']
    # take first string in list (list[0]) and .split(':') with colon

    # Check if Duration time is valid
    # split duration w/ .split(':') and colon - results in ['hour', 'minute']
    # minute < 60, else print('Error: Minutes in the duration time must be less than 60')
    # check if hour is a whole number, hour%1==0 else print('Error: the Hour must be a whole number')

    # new_hour = start[hour] + duration[hour]
    # new_minute = start[minute] + duration[minute]
    # if new_minute > 60, add 1 to new_hour
    # if new_hour > 12, return PM, else return AM

    # multi-day result

    # if new_time is the next day, return 'new_time (next day)'
    # if new_time is n =< 1 day later, return 'new_time (next day)'
    # if new_time is n > 1 day later, return 'new_time (n days later)'
    # if optional_start_day = True, return 'new_time, day-of-week, (n days later)'

    return new_time
