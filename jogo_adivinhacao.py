import random 

def adivinhacao():
  print('=' * 40)
  print('          BEM-VINDO AO JOGO DA ADIVINHAÇÃO        ')
  print('=' * 40)
  print('Tente adivinhar o número secreto entre 1 e 99!\n')


numero = random.randint(1, 99)
tentativas = 0

while True:
    try:
        palpite = int(input('Digite seu palpite (1 - 99): '))

    except ValueError:
        print('Entrada inválida! Por favor, digite apenas números inteiros entre 1 e 99.\n')
        continue

    if palpite < 1 or palpite > 99:
      print('Atenção: Digite um número inteiro entre 1 e 99.\n')
      continue
      
    tentativas += 1

    if palpite < numero:
      print('Muito baixo! Tente um valor maior.\n')

    elif palpite > numero:
      print('Muito alto! Tenta um número menor.\n')
    else:
      print('=' * 40)
      print(f'PARABÉNS!!! VOCÊ ACERTOU O NÚMERO {numero}!!!')
      print(f'Total de tentativas: {tentativas}')
      print('=' * 40)
      break


if __name__ =="__main__":
  adivinhacao()
