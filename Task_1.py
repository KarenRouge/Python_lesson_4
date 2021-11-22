from sys import argv

Name, Family_name, Hours = argv
print("Имя: ", Name)
print("Фамилия: ", Family_name)
print("Отработанные часы: ", Hours)
salary = (Hours * 1500) + 150000
print("Зарплата за текущий месяц: ", salary)
