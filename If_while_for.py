
login = 'ssi'
type_os = 'Mac'

if login == 'ssi' and type_os == 'Mac':
    print('Добро пожаловать,', login, type_os)
elif login == 'vba':
    print('Добро пожаловать,', login)
else:
    print('Привет незнакомец')

'Или аналогичный вариант:'

match login:
    case 'ssi':
        print('Добро пожаловать, ssi')
    case 'vba':
        print('Добро пожаловать, vba')




# current_pas = 'Python'
# ent_pass = ''
# while ent_pass != current_pas:
#     ent_pass = input('Введите пароль: ')
#     if ent_pass != current_pas:
#         print('Неверный пароль')
# print('Добро пожаловать!')
#
# #___________________________________
# fruits = ['apple','banana', 'cherry']
# for fruit in fruits:
#     print(fruit)
# # => apple
# # => banana
# # => cherry
# # ___________________________________
# for f in 'fruit':
#     print(f)
# # => f
# # => r
# # => u
# # => i
# # => t
#
# # ___________________________________
# my_dict = {'apple': 10, 'banana': 'not_enough'}
# for i in my_dict:
#     print(i)
# for i in my_dict.values():
#     print(i)
# for i in my_dict.items():
#     print(i)
#
# => apple
# => banana
# => 10
# => not_enough
# => ('apple', 10)
# => ('banana', 'not_enough')
#
# # _________________________________
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for row in matrix:
#     for item in row:
#         print(item, end=' ')
#     print()
# => 1 2 3
# => 4 5 6
# => 7 8 9
#
# #____________________________________
# for i in range(7):
#     if i == 4:
#         continue
#     if i == 6:
#         break
#     print(i)
# else: print('без прерывания')
# => 0
# => 1
# => 2
# => 3
# => 5
#
#  # _______________________________
# # получить индекс элемента и элемент
# fruits = ['apple','banana', 'cherry']
# for index, element in enumerate (fruits):
#     print(index, element)
# # => 0 apple
# # => 1 banana
# # => 2 cherry
# #
# #  ________________________________
# fr = {'apple','banana'}
# ag = (22, 33, 44)
# for frs, ags in zip (fr, ag):
#     print(frs, ags)
#
# => apple 22
# => banana 33
#  ________________________________
#
# numbers = [11, 23, 2, 5, 8, 12, 22]
# even_c = 0
# odd_c = 0
# for num in numbers:
#     if num % 2 == 0:
#         even_c +=1
#     else:
#         odd_c +=1
# print(even_c)
# print(odd_c)
#
# => 4
# => 3
#
# # _____________________________
#
