MONTH_NAMES = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
               6: 'June', 7: 'July', 8: 'August', 9: 'September',
               10: 'October', 11: 'November', 12: 'December'}


def month(n: int) -> str:
    try:
        return MONTH_NAMES[n]
    except KeyError:
        raise ValueError(f'{n} is not a valid month.')
