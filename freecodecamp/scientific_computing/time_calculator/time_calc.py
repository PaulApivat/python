# function add_time takes two required parameters, one optional parameter

# start time ending in AM or PM
# duration time in Hours:Minutes
# (optional) a starting day of the week, case INsensitive

def add_time(start, duration, optional_start_day=False):

    # Start time is valid
    # split start w/ .split() function - results in list with two strings ['hour:minute', 'AM/PM']
    start_split = start.split()
    # take first string in list (list[0]) and .split(':') with colon - result in split hour from minute
    hour_min = start_split[0].split(':')

    # Check if Duration time is valid
    # split duration w/ .split(':') and colon - results in ['hour', 'minute']
    duration_split = duration.split(':')
    # minute < 60, else print('Error: Minutes in the duration time must be less than 60')
    if int(duration_split[1]) > 59:
        print('Error: Minutes in duration time must be less than 60')
    # check if hour is a whole number, hour%1==0 else print('Error: the Hour must be a whole number')
    elif float(duration_split[0])*10 % 10 != 0:
        print('Error: the Hour must be a whole number')
    else:
        print('Duration time is valid')

    # new_hour = start[hour] + duration[hour]
    new_hour = int(hour_min[0]) + int(duration_split[0])
    # new_minute = start[minute] + duration[minute]
    new_minute = int(hour_min[1]) + int(duration_split[1])
    # if new_minute > 60, add 1 to new_hour AND turn new_minute in '00'
    if new_minute > 59:
        new_hour += 1
        new_minute = '0' + str(new_minute - 60)
        #new_time = str(new_hour) + ':' + str(new_minute)
    else:
        new_hour += 0
        #new_time = str(new_hour) + ':' + str(new_minute)

    print("new_hour check: ", new_hour)
    print("new_minute check: ", new_minute)
    # if new_hour > 12, return PM, else return AM
    if (new_hour > 12) and (start_split[1] == 'AM'):
        new_time = str(new_hour - 12) + ':' + str(new_minute) + str(' PM')
    elif (new_hour > 12) and (start_split[1] == 'PM'):
        new_time = str(new_hour - 12) + ':' + str(new_minute) + str(' AM')
    elif (new_hour < 12) and (start_split[1] == 'PM'):
        new_time = str(new_hour) + ':' + str(new_minute) + str(' PM')
    else:
        new_time = str(new_hour) + ':' + str(new_minute) + str(' AM')

    print("new_time check: ", new_time)
    print("old time check: ", start)
    # multi-day result
    # if new_hour > 24 & < 48, print '(next day)'
    # then for every 24 hours added to new_hour, update 'n' in '(n days later)'

    # (optional parameter): day-of-week
    # since its case INsensitive, convert day-of-week to lower case
    # days_of_week_list = ['Sunday', 'Monday', 'Tuesday', Wednesday', 'Thursday', 'Friday', 'Saturday']
    # check if provided day-of-week parameter "matches" a string in days_of_week_list
    # if not, print('Error: you misspelled the day of week')
    # for every 24 hours added, take day-of-week parameter, and increment to the next day.

    # if new_time is the next day, return 'new_time (next day)'
    # if new_time is n =< 1 day later, return 'new_time (next day)'
    # if new_time is n > 1 day later, return 'new_time (n days later)'
    # if optional_start_day = True, return 'new_time, day-of-week, (n days later)'

    return new_time


#print(add_time("3:00 PM", "3:10"))
#print(add_time("11:30 AM", "2:32"))
#print(add_time("11:30 AM", "2:32", "Monday"))
#print(add_time("11:43 AM", "00:20"))
print(add_time("10:10 PM", "3:30"))
#print(add_time("11:43 PM", "24:20"))
#print(add_time("6:30 PM", "205:12"))
