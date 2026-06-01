import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "src"))

from roman_converter.converter import to_roman, to_intager


def main():
    print("Roman Numeral Converter")
    print("1. Integer -> Roman")
    print("2. Roman -> Integer")

    option = input("Choose option: ")

    if option == "1":
        number = int(input("Enter integer: "))
        result = to_roman(number)
        print(f"Roman numeral: {result}")

    elif option == "2":
        roman = input("Enter roman numeral: ").upper()
        result = to_intager(roman)
        print(f"Integer: {result}")

    else:
        print("Invalid option")


if __name__ == "__main__":
    main()