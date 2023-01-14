import random
from string import ascii_letters, digits

SYMBOLS_CHOICE = list(ascii_letters + digits)


def get_unique_short_url():
    """Алгоритм формирования коротких идентификаторов переменной длины."""
    new_url = random.choices(SYMBOLS_CHOICE, k=6)
    return ''.join(new_url)


def check_symbols(short_url):
    for elem in short_url:
        if elem not in SYMBOLS_CHOICE:
            return False
    return True
