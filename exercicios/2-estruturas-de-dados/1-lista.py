# Crie uma lista apenas com elementos numéricos
listaNumerica = [0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Crie uma lista contendo todos os tipos e estrutura de dados que você aprendeu até agora
listaVazia = []
numeros = [1, 2, 3, 4, 5]
nomes = ["Alice", "Bob", "Charlie"]
salarios = [2500.50, 3000.75, 4000.00]
listaMista = [1, "Alice", 2500.50, True, None]

# Imprima na tela apenas os 5 primeiros elementos da lista
print(listaNumerica[:5])

# Crie um slice na lista para que imprima na tela os elementos de índice par
print(listaNumerica[::2])
print(listaNumerica[0:-1:2])

# Remova da lista o último item
print(listaNumerica.pop())

# Insira na lista um novo item
listaNumerica.append(10)
listaNumerica.extend([11])
print(listaNumerica)

# Remova da lista um item específico
print(numeros)
numeros.remove(2)
print(numeros)