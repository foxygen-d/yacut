import random
from string import ascii_letters, digits

SYMBOLS_CHOICE = list(ascii_letters + digits)


def get_unique_short_url():
    """Алгоритм формирования коротких идентификаторов переменной длины."""
    short = random.choices(SYMBOLS_CHOICE, k=6)
    return ''.join(short)


def check_symbols(custom_id):
    for elem in custom_id:
        if elem not in SYMBOLS_CHOICE:
            return False
    return True
