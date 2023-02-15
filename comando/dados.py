import random

def play():
    user = input("Qual é a sua escolha? 'a' para pedra, 's' para papel, 'd' para tesoura\n")
    computer = random.choice(['a', 's', 'd'])

    if user == computer:
        return 'Deu empate'

    if is_win(user, computer):
        return 'Você ganhou!'

    if is_win(computer, user):
        return 'Você Perdeu!'

def is_win(player, oponente):
    if (player == 'a' and oponente == 'd') or (player == 's' and oponente == 'a') or (player == 'd' and oponente == 's'):
        return True

print(play())
