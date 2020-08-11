soma = 0
media = 0
homemidade = 0
homemnome = ''
mulhermenor = 0
for p in range(1, 5):
    print('------{}° PESSOA------'.format(p))
    nome = str(input('Qual o seu nome? ')).strip().title()
    idade = int(input('Qual a sua idade? '))
    sexo = str(input('Qual o seu sexo? [M/F] ')).strip().upper()
    soma += idade
    if p == 1 and sexo == 'M': #poderia colocar sexo IN 'Mn' se não tivesse colocar o .upper lá em cima
        homemidade = idade
        homemnome = nome
    if sexo == 'M' and idade > homemidade:
        homemidade = idade
        homemnome = nome
    if sexo == 'F' and idade < 20:
        mulhermenor += 1
media = soma / 4
print('A média da idade desse grupo é {}'.format(media))
print('O homem mais velho do grupo tem {} anos e se chama {}'.format(homemidade, homemnome))
print('Ao todo, {} mulher(es) do grupo, tem menos de 20 anos'.format(mulhermenor))
