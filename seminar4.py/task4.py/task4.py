# Задача 4. Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов
# влево или вправо. При расшифровке происходит обратная операция.
# К примеру, слово "абба" можно зашифровать "бввб" - сдвиг на 1 вправо. "вггв" - сдвиг на 2 вправо, 
# "юяяю" - сдвиг на 2 влево.
# Сдвиг часто называют ключом шифрования.
# Ваша задача - написать функцию, которая записывает в файл шифрованный текст, 
# а также функцию, которая спрашивает ключ, считывает текст и дешифровывает его.

#with open('initialtext.txt', 'w', encoding='utf-8') as initial_text:
#    initial_text.write('Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.\n')

#path = 'initialtext.txt'
#initial_text = open(path, 'r', encoding='utf-8')
#for line in initial_text:
#    print(line)
#initial_text.close()

#def crypt(text:str, key:int, decrypt:bool = False):
#    key = -key if decrypt else key
#crypt('Hello', 5, deckrupt=True)    

def get_encript_text(alfabet: str, text: str, key: int) -> str:
    en_text = ''
    alfabet_long = len(alfabet)
    for simbol in text:
        i = 0
        for s in alfabet:
            if simbol == s:
                index = i + key
            i +=1
        if index > alfabet_long:
            index -= alfabet_long
        en_text += alfabet[index]
    return en_text

def get_decript_text(alfabet: str, text: str, key: int) -> str:
    de_text = ''
    alfabet_long = len(alfabet)
    for simbol in text:
        i = 0
        for s in alfabet:
            if simbol == s:
                inex = i - key
            i +=1
        if index < 0:
            index = alfabet_long + index
        if index >= alfabet_long:
            index = index - alfabet_long
        de_text += alfabet[index]
    return de_text

alfabet = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя,.!"№;%:?*()_-=+*/0123456789 ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@#$&<>'
initial_text = 'Шифр Цезаря - это способ шифрования, где каждая буква смещается на определенное количество символов влево или вправо.'
key = 5

en_text = get_encript_text(alfabet, initial_text, key)
file_encript = open('enskript.txt', 'w', encoding='utf-8')
file_encript.write(en_text)
file_encript.close()

print('текст зашифрован см. file "encript.txt"')

file_encript = open('encript.txt', 'r', encoding='utf-8')
ens_text = file_encript.read()
file_encript.close()

de_text = get_decript_text(alfabet, ens_text, key)

file_decript = open ('decript.txt', 'w', encoding='utf-8')
file_decript.write(de_text)
file_decript.close()

print('фашл расшифрован см. file "desript.txt"')
