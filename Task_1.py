from sys import argv

script, Name, Family_name, Hours = argv

print(argv)
print("Имя: ", Name)
print("Фамилия: ", Family_name)
print("Отработанные часы: ", Hours)
salary = (int(Hours) * 1500) + 150000
print("Зарплата за текущий месяц: ", salary)
