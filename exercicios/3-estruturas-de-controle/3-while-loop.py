# Crie duas variáveis do tipo numérica, uma sinalizando a fase atual do curso e outra o nível final
# Crie um while loop que imprima na tela o nível atual
# Insira "else" no while loop anterior.

nivel_atual = 3
nivel_final = 5

while nivel_atual <= nivel_final:
    print(f"Nível atual: {nivel_atual}")
    nivel_atual += 1
else:
    print("Você completou o curso!")