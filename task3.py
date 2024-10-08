#Задание 3

f = open('text_file.txt', 'r', encoding='utf-8')
res = 0
for line in f: 
    res = res + len(line.replace('— ','' ).split(' '))

print(res)    