number_list = [32, 21, 48, 34.56]
print(number_list)

some_list=[12, 35.334, 'hello']
print(len(some_list))
print(some_list)

print(some_list[1])
another_list = some_list[:2]
print(another_list)
print(some_list)
some_list[2] = 'hi'
print(some_list)
new_list = some_list + another_list
print(new_list)

#adding items
new_list.append('new item')
print(new_list)
new_list.insert(0, 'start')
print(new_list)

#removing items
new_list.pop(-1)
print(new_list)
deleted_item = new_list.pop(-2)
print(new_list)
print(deleted_item)

