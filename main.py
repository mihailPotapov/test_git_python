print("Степан и Руслан решили решить спор игрой камень ножницы бумага")
print("что же они выберут?")
print("введите: 'камень', 'ножницы', 'бумага'")
s = input("Степан выбирает:")
r = input("Руслан выбирает:")

if s == r:
    print('ничья')
elif s == 'камень' and r == 'ножницы':
    print('победил Степан!')
elif s == 'ножницы' and r == 'бумага':
    print('победил Степан!')
elif s == 'бумага' and r == 'камень':
    print('победил Степан!')
elif s == 'камень' and r == 'бумага':
    print('победил Руслан')
elif s == 'бумага' and r == 'ножницы':
    print('победил Руслан')
elif s == 'ножницы' and r == 'камень':
    print('победил Руслан')
else:
    print('упс ошибка, попробуйте снова')