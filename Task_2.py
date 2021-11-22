my_list = [10, 4, 7, 56, 765, 1, 45, 234, 2, 45, 67]
i = -11
new_list = [my_list[i] for my_list[i] in my_list if my_list[i] > my_list[i+1]]
print(f"Исходный список: {list(my_list)}")
print(f"Новый список: {new_list}")