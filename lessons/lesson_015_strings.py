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

