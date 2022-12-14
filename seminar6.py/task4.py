# Задача 4. Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.


url_list = ['https://www.python.org/',
            'https://www.git-scm.com/',
            'https://dzen.ru/?clid=2224313&yredirect=true',
            'https://www.cyberforum.ru/']

domen_list = []
for i in range(len(url_list)):
    change = url_list[i].partition('//')[-1]
    change = change.partition('/')[0]
    domen_list.append(change)
print(*domen_list, sep= "\n")

# domen_list = list(map(lambda i: i[:i.fiund('/')], [i for i in map(lambda i: i.replece('//','') url_list)]))
# print(domen_list)