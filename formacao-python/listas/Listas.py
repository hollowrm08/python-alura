def printarMensagem(mensagem):
    print("\n", mensagem.center(100, "-"))


printarMensagem("Extendendo lista")
lista = [12, 82, 78]
lista.extend([13, 83, 79])
print(f'lista extendida: {lista}')


printarMensagem("Exemplos de ListComprehension")
novaLista = [item + 1 for item in lista]
print(f'Nova Lista Criada: {novaLista}')
listaFiltrada = [item for item in novaLista if item > 30]
print(f'Lista filtrada: {listaFiltrada}')

printarMensagem("Arrays puros")
import array as arr

meuArray = arr.array('d', [1, 4.2, 8.0])
print(f'Array puro criado: {meuArray}')


printarMensagem("Enumerate")
print("Printando valores do enumerate:")
for valor in enumerate([2, 3, 5]):
    print(valor)

print("\nPrintando posicao e valores do enumerate")
for posicao, valor in enumerate([2, 3, 5]):
    print(f'Valor da posicao {posicao}: {valor}')


printarMensagem("Unpacking For")
pessoas = [
    ("Rodrigo Mello", 18, "M"),
    ("Luis Felipe K", 19, "M"),
    ("Debora Petry", 19, "F")
]
for nome, idade, sexo in pessoas:
    print(f'Nome: {nome} - Idade: {idade} - Sexo: {sexo}')

