def printarMensagem(mensagem):
    print("\n", mensagem.center(100, "-"))


printarMensagem("Instanciando e Manipulando Conjuntos (set)")
conjuntoA = {2, 6, 8, 10, 12}
print(f'Conjunto A: {conjuntoA}')

conjuntoB = {3, 6, 9, 12}
print(f'Conjunto B: {conjuntoB}')

conjuntoC = conjuntoA | conjuntoB
print(f'Presentes em A ou B: {conjuntoC}')

conjuntoD = conjuntoA & conjuntoB
print(f'Presentes em A e B: {conjuntoD}')

conjuntoE = conjuntoA - conjuntoB
print(f'Presente somente em A: {conjuntoE}')

conjuntoF = conjuntoA ^ conjuntoB
print(f'Presente em A ou B mas não em ambos: {conjuntoF}')

conjuntoImutavel = frozenset(conjuntoA)
print(f'Conjunto imutável: {conjuntoImutavel}')
