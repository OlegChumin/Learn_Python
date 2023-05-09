#string methods and properties
#string are immutable
first_name = "Jake"
print(first_name[2]) #k
#first_name[2] = 'n' #TypeError: 'str' object does not support item assignment
#print(first_name)

first_two_letters = first_name[:2]
print(first_two_letters) #Ja
last_letter = first_name[-1]
print(last_letter)
new_first_name = first_two_letters + 'n' + last_letter
print(new_first_name)

#concatination
greeting = 'Hello'
print(greeting)
greeting = greeting +" Python"
print(greeting)
greeting += "!"
print(greeting)

#