# Задача 3. В файле, содержащем фамилии студентов и их оценки, изменить на буквы в верхнем регистре тех студентов, 
# которые имеют средний балл более «4».

#from typing import list

with open('list_stydents.txt', 'w') as file_spisok:
    file_spisok.write('Ангела Меркель 5\n')
    file_spisok.write('Энакин Скайокер 4\n')
    file_spisok.write('Фредди Меркури 3\n')
    file_spisok.write('Гарри Поттер 5\n')
    file_spisok.write('Джон Трамп 3\n')
    file_spisok.write('Александр Пушкин 5\n') 

def change_spisok(spisok: list[str], accept: str) -> str:
    file_spisok = ''
    for name in spisok:
        if name.count(accept):
            name = name.upper()
        string = name + '\n'
        file_spisok += string
    return file_spisok
            
file_spisok = open('list_stydents.txt', 'r') # , encoding='uft-8'
lines_spisok = file_spisok.read().split('\n')
file_spisok.close()

spisok_new = change_spisok(lines_spisok, accept='5')

file_spisok = open('list_stydents_new.txt', 'w') #, encoding='uft-8'
file_spisok.write(spisok_new)
file_spisok.close()

path = 'list_stydents.txt'
file_spisok = open(path, 'r')
for line in file_spisok:
    print(line)
file_spisok.close()

