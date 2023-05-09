import time

greeting = "Hello"
first_name = "Jack"
last_name = 'White'
exclamation_symbol = "!"
white_space = " "
print(greeting + first_name + last_name)
print(greeting + " " + first_name + white_space + last_name + exclamation_symbol)
long_string = "This is long string"
print(long_string)
whole_sentence = greeting + white_space + first_name + " " \
    + last_name + exclamation_symbol
print(whole_sentence)

print("Hello!", end="", flush=True)
time.sleep(1)
print("\rWorld!", end="", flush=True)
print()

#Escaping
some_string = "I'm a programmer"
another_string = 'I want to lear "Python"'
new_string = 'I\'m a programmer'
another_new_string = "I want to lear \"Python\""

print("\"DarkNetXakep! \"")
print("\"DarkNetXakep! \"", end="")
print("\"DarkNetXakep! \"")
print("Hello! \n    My name is \"WHOAMI\"")
print("Hello! \n     \rMy name is \"WHOAMI\"")

numbers = "1234567"
print(numbers)
numbers = "1\t23\t456\t789"
print(numbers)
print("\tHello!    \n\r\tMy name is \r\n\t\"WHOAMI\"")

string_with_triple_quotes = """This is ' text with "triple quotes" """
print(string_with_triple_quotes)
another_string_with_triple_quotes = '''This is ' text with "triple quotes" '''
print(another_string_with_triple_quotes)
string_with_triple_quotes = """This is ' \ntext with "triple quotes" """
print(string_with_triple_quotes)