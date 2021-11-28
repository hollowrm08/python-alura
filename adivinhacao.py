def jogar():
    import random

    tentativas_max = 4
    numero_a_advinhar = random.randint(1, 20)

    print('------------------Advinhação------------------')
    print(f'Você tem {tentativas_max} tentativas')

    for rodada in range(0, tentativas_max):
        print(f'\nTentativa {rodada + 1} de {tentativas_max}:')

        variavel_input = int(input("Digite um número de 1 a 20: "))
        print(f'Você Digitou: {variavel_input}')

        if variavel_input == numero_a_advinhar:
            print("Você acertou!")
            break
        elif variavel_input > numero_a_advinhar:
            print("Você Errou! Chute um numero menor")
        else:
            print("Você Errou! Chute um numero maior")

    print(f'\nO número era: {numero_a_advinhar}')
    print("Fim de jogo")


if __name__ == "__main__":
    jogar()
