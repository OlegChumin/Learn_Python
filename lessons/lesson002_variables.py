import math

x = 5
y = 7
sum = x + y
print('Это переменная x = %d, y = %d, и их сумма sum = %d' % (x, y, sum))
print()

print("Тип переменной x до переназначения = ", type(x)) #демонстрация динамической типизации
x = "Some String"
print("Тип переменной x после переназначения = ", type(x))
x = math.pi
print("Тип переменной x после переназначения math.pi = ", type(x))

car_color = "black" #snake case наименование переменных
#car-color Kebab case pзапрещен в Python
carColor = "white" #CamelCase

"""
Имена переменных следует писать в нижнем регистре, а слова внутри имени разделять символом подчеркивания. 
Например: my_variable.
Имена переменных должны быть описательными, понятными и не слишком длинными. Например, name, age, is_valid - 
хорошие имена переменных.
Избегайте использования однобуквенных имен переменных, таких как x или y, если это не требуется для корректной 
работы программы.
Если переменная содержит значение, которое не должно изменяться, она должна быть именована с использованием 
заглавных букв и символов подчеркивания, например: MY_CONSTANT.
Если имя переменной состоит из нескольких слов, каждое слово должно начинаться с заглавной буквы, кроме первого 
слова. Этот стиль именования переменных называется "CamelCase". Например: firstName, isConnected, totalPrice.
Имена переменных не должны начинаться с цифры.
Избегайте использования зарезервированных слов (например, if, while, for) в качестве имен переменных.
Используйте логические имена для булевских переменных. Например, is_valid, has_error, can_process.
В целом, следуя этим соглашениям по именованию переменных, вы сможете создавать читабельный, понятный и 
легко поддерживаемый код в Python.
В Python имена переменных должны состоять только из букв (a-z, A-Z), цифр (0-9) и символа подчеркивания (_). 
Кроме того, 
имена переменных не могут начинаться с цифры.
Существуют некоторые запрещенные символы, которые не могут использоваться в именах переменных. Эти символы 
включают в себя пробелы, знаки пунктуации, математические символы и другие специальные символы.
Если вы попытаетесь использовать запрещенные символы в имени переменной, вы получите синтаксическую ошибку. 
Чтобы избежать этой ошибки, используйте только разрешенные символы в именах переменных.
Кроме того, есть некоторые ключевые слова (например, if, while, for, and, or), которые не могут использоваться 
в качестве имен переменных, так как они зарезервированы для специальных целей в Python.
"""

