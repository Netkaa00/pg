def prevod_c_na_f(stupne):
    return (stupne * 1,8 + 32) 


def test_prevod_c_na_f():
    assert prevod_c_na_f(100) == 212
    assert prevod_c_na_f(0) == 32