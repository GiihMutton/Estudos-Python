from time import sleep

num = int(input('Escolha um número: '))
print('A tabuada do {} é: '.format(num))
sleep(0.5)
print('-' *12)
for n in range(0, 11):
    print('{} x {} = {}'.format(num, n, (num * n)))
print('-' *12)
