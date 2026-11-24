from my_arithmetic_murtaza.gcd import gcd

def test_gcd():
    assert gcd(48, 18) == 6
    assert gcd(17, 13) == 1
    assert gcd(0, 5) == 5