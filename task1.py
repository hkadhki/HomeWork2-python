#Задание 1

with open('source.txt', 'r') as source:
    with open('destination.txt', 'w') as dest:
        for line in source:
            dest.write(line)