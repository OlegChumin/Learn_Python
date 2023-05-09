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

print("Hello!", end="", flush=True)
time.sleep(1)
print("\rWorld!", end="", flush=True)
print()

