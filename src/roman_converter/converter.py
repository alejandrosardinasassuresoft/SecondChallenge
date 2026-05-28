def to_roman(number: int) -> str:
    if number == 1:
        return "I"
    if number == 2:
        return "II"
    if number == 3:
        return "III"
    if number == 4:
        return "IV"
    if number == 5:
        return "V"
    if number == 9:
        return "IX"
    if number == 10:
        return "X"
    if number == 40:
        return "XL"
    if number == 50:
        return "L"
    if number == 90:
        return "XC"
    if number == 100:
        return "C"
    if number == 400:
        return "CD"
    if number == 500:
        return "D"