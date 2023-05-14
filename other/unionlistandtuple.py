my_list = [1, 2, 3]
my_tuple = (4, 5, 6)

new_list = [*my_list, *my_tuple]

print(new_list) # [1, 2, 3, 4, 5, 6]
