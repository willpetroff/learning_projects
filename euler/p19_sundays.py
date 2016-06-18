def leap_year_chk(input_year):
    if (input_year % 4 == 0 and input_year % 100 != 0) or input_year % 400 == 0:
        return 1
    else:
        return 0


def day_start_check(day_start_dict, first_day, leap_year):
    if day_start_dict[first_day][leap_year]['sundays']:
        return day_start_dict[first_day][leap_year]['sundays'], day_start_dict[first_day][leap_year]['last_day']
    else:
        sun_count, next_start_day = sunday_counter(first_day, leap_year)
        return sun_count, next_start_day


def sunday_counter(first_day, leap_year):
    month_len = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    sundays = 0
    current_day = first_day
    for month in month_len:
        days = 1
        if month == 2 and leap_year:
            while days <= 29:
                if current_day == 7 and days == 1:
                    sundays += 1
                    current_day = 0
                elif current_day == 7:
                    current_day = 0
                current_day += 1
                days += 1
        else:
            while days <= month_len[month]:
                if current_day == 7 and days == 1:
                    sundays += 1
                    current_day = 0
                elif current_day == 7:
                    current_day = 0
                current_day += 1
                days += 1
    return sundays, current_day


day_start_year = {1: {0: {'last_day': 2, 'sundays': 2}, 1: {'last_day': 0, 'sundays': 0}},
                  2: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}},
                  3: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}},
                  4: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}},
                  5: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}},
                  6: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}},
                  7: {0: {'last_day': 0, 'sundays': 0}, 1: {'last_day': 0, 'sundays': 0}}}
counted_sundays = 0
day_of_week = 2
for year in range(1901, 2001):
    ly_val = leap_year_chk(year)
    yearly_sundays, new_day_of_week = day_start_check(day_start_year, day_of_week, ly_val)
    day_start_year[day_of_week][ly_val]['sundays'] = yearly_sundays
    day_start_year[day_of_week][ly_val]['last_day'] = new_day_of_week
    counted_sundays += yearly_sundays
    day_of_week = day_start_year[day_of_week][ly_val]['last_day']
print(counted_sundays)
# this is a test
