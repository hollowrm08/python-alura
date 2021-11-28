import adivinhacao

print("Jogos disponíveis:")
print("(1) Adivinhacao")

opcao = int(input("Qual jogo deseja jogar? "))

if opcao == 1:
    print("Iniciando jogo de adivinhação")
    adivinhacao.jogar()
