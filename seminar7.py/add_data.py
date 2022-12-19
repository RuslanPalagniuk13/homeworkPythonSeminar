import csv

# открытие файла, чтение, закрытие
with open("phone.csv", "r", encoding='utf-8') as f:
    data = f.readlines()

# удаление строк, для которых выполнено условие
data = filter(lambda line: "стоп_слово" not in line, data)

# более сложные условия редактирования стоит вынести в отдельную функцию   
def transformation(line):
    if "слово_маркер" in line:
        return "замещающая строка\n"
    return line.replace("что_заменить", "на_что")

# редактирование строк файла
data = map(transformation, data)

    
def del_memb(data):
    ''' удаление по имени и фамилии'''
    member = ' '.join(map(str.lower, [input('Фамилия > '), input('Имя > '), input('Отчество > ')]))
    for i,obj in enumerate(data):
        if obj.identifier() == member:
            data.pop(i)
            savedata(data,name) # перезаписываем файл c новыми данными
            print('удалено')
            return

# открытие, запись и закрытие файла
with open("phone.csv", "w", encoding='utf-8') as f:
    f.write("".join(data))