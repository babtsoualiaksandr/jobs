from datetime import datetime


def get_zodiac(birthday):
    """
    Return  Zodiac sign for users’ birthday

    Args:
    birthday ([str]): [exp: 1972-11-03]

    Returns:
    [str]: [sign zodiac]
    """
    dt = datetime.strptime(birthday, '%Y-%m-%d')
    month = dt.month
    day = dt.day
    if ((month == 12 and day >= 22) or (month == 1 and day <= 19)):
        Signo_Zodiacal = ("\n Capricorn")
    elif ((month == 1 and day >= 20) or (month == 2 and day <= 17)):
        zodiac_sign = ("\n aquarium")
    elif ((month == 2 and day >= 18) or (month == 3 and day <= 19)):
        zodiac_sign = ("\n Pices")
    elif ((month == 3 and day >= 20) or (month == 4 and day <= 19)):
        zodiac_sign = ("\n Aries")
    elif ((month == 4 and day >= 20) or (month == 5 and day <= 20)):
        zodiac_sign = ("\n Taurus")
    elif ((month == 5 and day >= 21) or (month == 6 and day <= 20)):
        zodiac_sign = ("\n Gemini")
    elif ((month == 6 and day >= 21) or (month == 7 and day <= 22)):
        zodiac_sign = ("\n Cancer")
    elif ((month == 7 and day >= 23) or (month == 8 and day <= 22)):
        zodiac_sign = ("\n Leo")
    elif ((month == 8 and day >= 23) or (month == 9 and day <= 22)):
        Signo_Zodiacal = ("\n Virgo")
    elif ((month == 9 and day >= 23) or (month == 10 and day <= 22)):
        zodiac_sign = ("\n Libra")
    elif ((month == 10 and day >= 23) or (month == 11 and day <= 21)):
        zodiac_sign = ("\n Scorpio")
    elif ((month == 11 and day >= 22) or (month == 12 and day <= 21)):
        zodiac_sign = ("\n Sagittarius")
    return zodiac_sign


if __name__ == "__main":
    zodiac = get_zodiac("1971-23-05")
    print(zodiac)
