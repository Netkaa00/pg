def my_range(start, stop, step = 1):



    result = []
    hodnota = start
    while hodnota < stop:
        result.append(hodnota)
        hodnota += step


def for_enumerate(iterable, start = 1):


    result = []

 
    for prvek in iterable:
        result.append((start, prvek))
        start += 1

    return result

def while_enumerate(iterable, start = 1):


    result = []
    
    index = 0
    while index < len(iterable):
        result.append((index + start, iterable[index]))
        index += 1

    return result

    

if __name__ == "__main__":
    
    #text = "abcdef"
    #seznam = ["a", "b", "c", "d", "e", "f"]

    #index = 0
    #for znak in text:
    #        print(znak)

    #index = 0
    #while index < len(text):
    #    print(text[index])
    #    index += 1 


    print (list((enumerate(["Alice", "Bob", "Eva"], 1 ))))
    print (for_enumerate(["Alice", "Bob", "Eva"], ))
    print (while_enumerate(["Alice", "Bob", "Eva"], ))
