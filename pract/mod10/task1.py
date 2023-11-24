import re
import doctest


def is_valid_password(password: str) -> bool:
    """
    Функция для проверки корректности пароля.

    >>> is_valid_password('aAaAaA')
    True

    >>> is_valid_password('AAAAA')
    False
    """

    pattern = (
        r'^([a-z]{2,})'  # at least two lowercase letters
    )
    return bool(re.match(pattern, password))


if __name__ == "__main__":
    doctest.testmod()