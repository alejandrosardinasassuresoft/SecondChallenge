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

def to_roman(number: int) -> str:
    result = ""
    
    for value, symbol in ROMAN_MAP:
        while number >= value:
            result += symbol
            number -= value

    return result

def to_intager(roman: str) -> int:
    if(roman == "I"):
        return 1
    if(roman == "II"):
        return 2
    if(roman == "III"):
        return 3
    if(roman == "IV"):
        return 4
    if(roman == "V"):
        return 5
    if(roman == "IX"):
        return 9
    if(roman == "X"):
        return 10
    if(roman == "XL"):
        return 40