from roman_converter.converter import to_intager, to_roman

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

def test_convert_900_to_cm():
    assert to_roman(900) == "CM"

def test_convert_1000_to_m():
    assert to_roman(1000) == "M"

def test_convert_58_to_lviii():
    assert to_roman(58) == "LVIII"

# Test for to_intager
def test_convert_i_to_1():
    assert to_intager("I") == 1

def test_convert_ii_to_2():
    assert to_intager("II") == 2

def test_convert_iii_to_3():
    assert to_intager("III") == 3