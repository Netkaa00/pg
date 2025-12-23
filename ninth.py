def dec_to_bin(decimalni_cislo):
    decimalni_cislo = int(decimalni_cislo)  

    if decimalni_cislo == 0:
        return "0"

    binarni = ""
    while decimalni_cislo > 0:
        binarni = str(decimalni_cislo % 2) + binarni
        decimalni_cislo //= 2

    return binarni




def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"