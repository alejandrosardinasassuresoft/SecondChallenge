from roman_converter.converter import to_roman

def test_convert_1_to_1():
    assert to_roman(1) == "I"