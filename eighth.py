def bin_to_dec(binarni_cislo):



    for i in binarni_cislo.reversed():
        decimalni_cislo += i * (2 ** index)
        index += 1
    return decimalni_cislo

def test_bin_to_dec():
    assert bin_to_dec("0") == 0
    assert bin_to_dec(1) == 1
    assert bin_to_dec("100") == 4
    assert bin_to_dec(101) == 5
    assert bin_to_dec("010101") == 21
    assert bin_to_dec(10000000) == 128