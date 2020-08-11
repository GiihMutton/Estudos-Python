from random import randint
from time import sleep
itens = ('PEDRA', 'PAPEL', 'TESOURA')
comp = randint(0, 2)
print('''\033[1;35mEscolha uma opção:\033[30m 
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input("\033[1;35mQual a sua jogada?\033[m "))
print("\033[1;30mJO")
sleep(0.5)
print("KEN")
sleep(0.5)
print("PO!\033[m")
sleep(0.5)
if jogador == 0 and comp == 1:
    print('\033[1m*=\033[m' * 9)
    print("♣ \033[1;31m VOCÊ PERDEU! \033[m ♣")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))
elif jogador == 0 and comp == 2:
    print('\033[1m*=\033[m' * 9)
    print("♥ \033[1;32m VOCÊ VENCEU! \033[m ♥")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))

elif jogador == 1 and comp == 0:
    print('\033[1m*=\033[m' * 9)
    print("♥ \033[1;32m VOCÊ VENCEU! \033[m ♥")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))
elif jogador == 1 and comp == 2:
    print('\033[1m*=\033[m' * 9)
    print("♣ \033[1;31m VOCÊ PERDEU! \033[m ♣")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))

elif jogador == 2 and comp == 0:
    print('\033[1m*=\033[m' * 9)
    print("♣ \033[1;31m VOCÊ PERDEU! \033[m ♣")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))
elif jogador == 2 and comp == 1:
    print('\033[1m*=\033[m' * 9)
    print("♥ \033[1;32m VOCÊ VENCEU! \033[m ♥")
    print('\033[1m*=\033[m' * 9)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))

elif jogador == comp:
    print('\033[1m*=\033[m' * 11)
    print("♦ \033[1;34m VOCÊS EMPATARAM! \033[m ♦")
    print('\033[1m*=\033[m' * 11)
    print('''\033[36mVocê escolheu \033[1m{}\033[m
\033[36mO computador também escolheu \033[1m{}\033[m'''.format(itens[jogador], itens[comp]))
else:
    print("\033[1;7;30mOPORA! JOGADA INVÁLIDA\033[m")