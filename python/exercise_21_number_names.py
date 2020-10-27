MONTH_NAMES = {'en': {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May',
                      6: 'June', 7: 'July', 8: 'August', 9: 'September',
                      10: 'October', 11: 'November', 12: 'December'},
               'de': {1: 'Jänner', 2: 'Februar', 3: 'März', 4: 'April', 5: 'Mai',
                      6: 'Juni', 7: 'Juli', 8: 'August', 9: 'September',
                      10: 'Oktober', 11: 'November', 12: 'Dezember'}
               }


def month(n: int, language: str = 'en') -> str:
    month_names = MONTH_NAMES[language.lower()]
    try:
        return month_names[n]
    except KeyError:
        raise ValueError(f'{n} is not a valid month.')
