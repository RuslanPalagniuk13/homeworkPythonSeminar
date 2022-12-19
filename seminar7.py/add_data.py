import csv

# открытие, запись и закрытие файла
def savedata(word, data):
    with open("phone.csv", "w", encoding='utf-8') as f:
        f.write("".join(word, data))



