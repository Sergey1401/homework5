#Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = (1,"Sergey",True,[1,2])
print(immutable_var)
#immutable_var[1] = "Ira"
#В строке "4" ошибка, которая требовалась по заданию, поэтому я оформил ее как коментарий
#Кортеж не поддерживает обращение по элементам.
mutable_list = [1,"Sergey",True,"apple"]
print(mutable_list)
mutable_list.append("work")
print(mutable_list)
mutable_list.extend([5,"windows"])
print(mutable_list)
mutable_list.remove("work")
print(mutable_list)
mutable_list[1]="Ira"
print(mutable_list)
