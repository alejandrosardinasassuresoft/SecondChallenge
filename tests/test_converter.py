from roman_converter.converter import to_roman

def test_convert_1_to_1():
    assert to_roman(1) == "I"

def test_convert_2_to_ii():
    assert to_roman(2) == "II"

def test_convert_3_to_iii():
    assert to_roman(3) == "III"

def test_convert_4_to_iv():
    assert to_roman(4) == "IV"