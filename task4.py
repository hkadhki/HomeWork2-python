#Задание 4

l = list()
input = open('input.txt', 'r')
for line in input:
    l.append(line.strip())
s = set(l)  

uniq = open('unique_output.txt', 'w')  
for line in s:
    uniq.write(line + '\n')        


