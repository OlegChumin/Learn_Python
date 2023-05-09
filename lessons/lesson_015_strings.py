#indexing and slicing in strings
    #индексы0123456789...
greeting = "Hello Python!!"
greeting_length = len(greeting)
print(greeting_length) #14
print(len(greeting))

print(greeting[0])
print(greeting[len(greeting) - 1])
#print(greeting[len(greeting)]) # IndexError: string index out of range

#индекс с конца строки
print(greeting[-1]) # последний элемент
print(greeting[-4]) # o

#slicing - получение подстрок
print(greeting[2:5]) #llo
print(greeting[6:12]) #Python
#с конца
print(greeting[-5:-2]) #hoh

print(greeting[5]) #пробел
print(greeting[5:]) #вся строка от 5 символа  Python!!
print(greeting[:5]) #вся строка до 5 символа  Hello

print(greeting[:]) #вывод всей строки
print()

print(greeting)
print(greeting[::2]) #вывод всей строки с шагом 2 HloPto!
print(greeting)
print(greeting[::3]) #вывод всей строки с шагом 3 HlPh!

print(greeting)
print(greeting[1::3]) #вывод всей строки с шагом 3 со второго символа eoyo!
print(greeting[2::3]) #вывод всей строки с шагом 3 с третьего символа l tn
print(greeting[0:10:2]) # вывод с 0 по 10 символы с шагом 2 HloPt

# разворот строки
print(greeting[::-1]) # начинаем с конца строки и до начала
print()

str = "Hello Python!"
print(str[3])
print("Hello Python!"[3])
print(str[0:2])
print(str[:-11])
path = "Hello Python" + '!'
print(path)