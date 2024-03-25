##ПОМЕНЯТЬ НА НЕОБХОДИМУЮ ДИРЕКТОРИЮ

##import os
##os.chdir("c:\\Users\\Лия\\Documents\\it\\pythonuni\\sr_var11\\2")
## считывание инпута

with open("input1.txt", "r") as file:
    lines = file.readlines()

##создание сетов с исходными данными
first_line = set(lines[0].split())
second_line= set(lines[1].split())
third_line= set(lines[2].split())

##создание выводных данных
return_line=""
return_list=[]

##проверка условий, добавление в строку в ответ и в список с подходящими словами
for item in second_line:
    if (item not in first_line)&(item not in third_line):
        return_list.append(item)
        return_line+=item+'-'

##лишние сепараторы в конце строки
return_line=return_line[:-1]

##значение длины рандомного элемента листа для сравнения
min_length=len(return_list[0])

##нахождение минимальной длины элемента
for item in return_list:
    if len(item)<min_length:
        min_length=len(item)

##аутпут
with open("output.txt", "w") as file:
    file.write(return_line+'\n'+str(min_length))
