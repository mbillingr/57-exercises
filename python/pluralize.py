

def pluralize(n: int, s: str) -> str:
    singular, plural = find_pluralization(s)
    if n == 1:
        return singular
    else:
        return plural


def register_pluralization(singular, plural):
    IRREGULAR_FORMS.add((singular, plural))


def find_pluralization(word):
    for form in IRREGULAR_FORMS:
        if word in form:
            return form
    if word.endswith('s'):
        return word[:-1], word
    else:
        return word, word + 's'


IRREGULAR_FORMS = set()

register_pluralization('ass', 'asses')
register_pluralization('is', 'are')
register_pluralization('person', 'people')
