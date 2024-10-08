#Задание 2

f = open('prices.txt', 'r', encoding='utf-8')
res = 0
for line in f:
    buffer = line.split('\t')
    res = res + int(buffer[1]) * int(buffer[2])

print("Сумма заказа: " + str(res))