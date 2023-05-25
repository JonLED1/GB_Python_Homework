glas = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']

stih = list(input('Введите стих: ').split())

if len(set(sum(map(lambda x: x in glas, i)) for i in stih)) < 2:
    print("Парам пам-пам")
else:
    print("Пам парам")