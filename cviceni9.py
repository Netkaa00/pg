def nejvetsi(seznam_cisel):

    if not seznam_cisel:
        return None

    maximum = seznam_cisel[0] 

    for i in seznam_cisel[1:]:
        if i > maximum:
            maximum = i

    return maximum

    
    


def test_nejvetsi():
    assert nejvetsi([1,2,3,4,5]) == 5
    assert nejvetsi([100, 50, 30, 10]) == 100
    assert nejvetsi([]) == None
    assert nejvetsi([1]) == 1