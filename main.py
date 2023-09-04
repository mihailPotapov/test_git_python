x= int(input("ведите число"))
b= input("ведите строку")
print('число получено, начинаю постройку масива...')
print('...')
masiv=[i for i in range(x)]
print(masiv)
print('генерация нового масива')
for i in range(len(masiv)):
    if masiv[i] % 2 == 0:
        masiv[i] = b
print(masiv,'новый масив!')