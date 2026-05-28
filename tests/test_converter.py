from roman_converter.converter import to_roman

def test_convert_1_to_1():
    assert to_roman(1) == "I"

def test_convert_2_to_ii():
    assert to_roman(2) == "II"

def test_convert_3_to_iii():
    assert to_roman(3) == "III"

def test_convert_4_to_iv():
    assert to_roman(4) == "IV"

def test_convert_5_to_v():
    assert to_roman(5) == "V"

def test_convert_9_to_ix():
    assert to_roman(9) == "IX"

def test_convert_10_to_x():
    assert to_roman(10) == "X"

def test_convert_40_to_xl():
    assert to_roman(40) == "XL"

def test_convert_50_to_l():
    assert to_roman(50) == "L"

def test_convert_90_to_xc():
    assert to_roman(90) == "XC"

def test_convert_100_to_c():
    assert to_roman(100) == "C"

def test_convert_400_to_cd():
    assert to_roman(400) == "CD"

def test_convert_500_to_d():
    assert to_roman(500) == "D"