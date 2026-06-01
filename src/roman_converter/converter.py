ROMAN_MAP = [
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
]

ROMAN_VALUES = [
    ("M", 1000),
    ("CM", 900),
    ("D", 500),
    ("CD", 400),
    ("C", 100),
    ("XC", 90),
    ("L", 50),
    ("XL", 40),
    ("X", 10),
    ("IX", 9),
    ("V", 5),
    ("IV", 4),
    ("I", 1),
]

def to_roman(number: int) -> str:
    result = ""
    
    for value, symbol in ROMAN_MAP:
        while number >= value:
            result += symbol
            number -= value

    return result

def to_intager(roman: str) -> int:
    result = 0
    index = 0

    for symbol, value in ROMAN_VALUES:
        while roman[index:index + len(symbol)] == symbol:
            result += value
            index += len(symbol)

            if index >= len(roman):
                break

    return result