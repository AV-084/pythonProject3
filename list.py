'распаковка' '*'

def test(a=2,b=True):
    print(a, b)

test ([1, 2] , 3) #-> [1, 2], 3

test (*[1, 2]) #-> 1, 2

def test2(*args, **kwargs):
    print(*args, **kwargs)

test2 ([1, 2], 3, 'Anna', 10, {'Vasia': 45, 'Petia': 46}) #-> [1, 2] 3 Anna 10 {'Vasia': 45, 'Petia': 46}

test2 (*[1, 2], 3, 'Anna', 10, *{'Vasia': 45, 'Petia': 46}) #-> 1 2 3 Anna 10 Vasia Petia