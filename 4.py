#Пам-парам


a = ['а', 'е', 'и', 'о', 'у', 'э', 'ю', 'я']
text = input().split()
count = [sum(i in a for i in line) for line in text]
if len(set(count)) == 1:
    print('Парам пам-пам')
else:
    print('Пам парам')