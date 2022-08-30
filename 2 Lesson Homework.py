"""1 Задание Напишите программу, которая принимает на вход вещественное число 
 и показывает сумму его цифр 
"""
    
# num = input('Введите число:')
 
# suma = 0
 
# for digit in num:
#     if digit.isdigit():
#         suma += int(digit)
       
# print("Сумма равна:", suma)

# num = input('Введите число:')

# str_num = str (num) 

# str_num = str_num.replace('.', '')

# lst_str = list(str_num)
# lst_nmbs = map(int, lst_str)

# s = sum(lst_nmbs)
# print(s)

"""2 Задание Напишите программу, которая принимает на вход число N
и выдает набор произведений чисел от 1 до N."""

# n = int(input("введите число "))
# num_lst = list(range(1,n+1))
# p = 1

# mult_lst = []
# for i in num_lst:
#     mult_lst.append(i*p)
#     p=p*i
# print(mult_lst)


"""3 Задание Реализуйте алгоритм перемешивания списка.
"""
# 1 пример
# sortList = ['bbb', 'a', 'cc']

# sortList.sort ()

# print(sortList)

# 2 пример

sortList = ['bbb', 'a', 'cc']

print(sorted(sortList, key=len))

