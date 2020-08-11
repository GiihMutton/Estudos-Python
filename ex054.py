from datetime import date
atual = date.today().year
totmai = 0
totmen = 0
for c in range(1, 8):
    ano = int(input('Insira o ano do seu nascimento: '))
    if atual - ano >= 21:
        totmai += 1
    else:
        totmen += 1
print('{} pessoas são maiores de 21 anos\nas outras {} pessoas são menores de idade'.format(totmai, totmen))
