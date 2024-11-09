'распаковка' '*'

def test(a=2,b=True):
    print(a, b)

test ([1, 2] , 3) #-> [1, 2], 3

test (*[1, 2]) #-> 1, 2

def test2(*args, **kwargs):
    print(*args, **kwargs)

test2 ([1, 2], 3, 'Anna', 10, {'Vasia': 45, 'Petia': 46}) #-> [1, 2] 3 Anna 10 {'Vasia': 45, 'Petia': 46}

test2 (*[1, 2], 3, 'Anna', 10, *{'Vasia': 45, 'Petia': 46}) #-> 1 2 3 Anna 10 Vasia Petia

'Конкантинация (склеивание)'
list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
result = str(list_1[0]) + str(list_2[0])
print(result) # -> 14

'Добавление вложенных списков'
matrix = []
matrix.append([])
print(matrix) # ->[[]]
matrix.append([])
print(matrix) # ->[[], []]
element = 5
matrix[0].append(element)
print(matrix) # ->[[5], []]


nums = [2,3,4,5,6,7,8,9]
for i in range(len(nums)):
    print(f'{i}', end='') # -> 01234567 ИНДЕКСЫ !!!

nums = [2,3,4,5,6,7,8,9]
for num in nums:
    print(f'{num}', end='') # -> 23456789 ЭЛЕМЕНТЫ !!!