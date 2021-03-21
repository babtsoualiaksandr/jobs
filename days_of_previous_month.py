from datetime import datetime, timedelta
import calendar


def days_of_previous_month(string_data):
    """
    enter any date and return first day and last day of previous month

    Args:
        string_data ([str]): [all date ex "2021-03-24"]

    Returns:
        [tuple]: [monthrange ferst an last day of of previous month ]
    """

    dt = datetime.strptime(string_data, '%Y-%m-%d')
    one_day = timedelta(days=1)
    one_month_earlier = dt - one_day
    while one_month_earlier.month == dt.month or one_month_earlier.day > dt.day:
        one_month_earlier -= one_day
    return calendar.monthrange(one_month_earlier.year, one_month_earlier.month)


if __name__ == "__main__":
    print(days_of_previous_month('2021-03-24'))
