# Часть проверки ввода данных, и вывода данных (требуют доработок)

def print_data(data):
    if len(data) > 0:
        print("Фамилия".center(15), "Имя".center(15), "Отчество".center(15), "Дата рождения".center(15), "Телефон".center(15), "Комментарий".center(20), "Дата и Время внесения".center(20))
        print("-"*125)
        for item in data:
            print(item[0].center(15), item[1].center(15), item[2].center(15), item[3].center(15), item[4].center(15), item[5].center(20), item[6].center(20))
    else:
        print("Справочник пуст!")

'''функция проверки на ввод только букв'''
def correct_input(text):
    name = input(f'{text} > ')
    if name == '*':
        return name 
    while not name.isalpha():
        print('не корректный ввод')
        name = input(f'{text} > ')
    return name.upper()    

'''функция проверки номера'''
def correct_number(text):
    number = input(f'{text} > ')
    while True:
        if number[0] == '+' and number[1:].isdigit() and len(number) == 12:
            return number
        print('не корректный ввод')
        number = input(f'{text} > ')

'''функция проверки года рождения'''        
def correct_age(text):
    age = input(f'{text} > ')
    while True:
        if age.isdigit() and len(age) == 4:
            return age
        print('введите правильный год')
        age = input(f'{text} > ')


''' функция получения данных'''        
def data_input(listfields):
    list_fun = [correct_input, correct_input, correct_input, correct_age, correct_number]
    return [fun(text) for text, fun in zip(listfields, list_fun)]  
     