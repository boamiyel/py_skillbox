import re


def is_valid_pass(password: str) -> bool:
    """
    >>> is_valid_pass("rtG&3FG#Tr^e")
    True
    >>> is_valid_pass("a^A1@*@1Aa")
    True
    >>> is_valid_pass("oF^a1D@y5%e6")
    True
    >>> is_valid_pass("enroi#$*rkdeR#$*092uwedchf34tguv394h")
    True
    >>> is_valid_pass("пароль")
    False
    >>> is_valid_pass("password")
    False
    >>> is_valid_pass("qwerty")
    False
    >>> is_valid_pass("lOngPa$$W0Rd")
    False
    """
    pattern = (
        r'^(?=.*[a-z].*[a-z])'
        r'(?=.*\d)' 
        r'([^,.!?])'
    )
    if len(password) < 8:
        return False
    if len(set(re.findall(r'[\^$%@#&*!?]', password))) < 3:
        return False
    return bool(re.match(pattern, password))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
