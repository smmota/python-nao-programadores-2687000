# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
nome = input("Digite seu nome: ")

# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
total_dias = int(input("Digite o total de dias dedicados ao estudo por semana: "))

# 3. Crie uma variável chamada "total_horas" e, usando o método input(), solicite a média de horas estudada por dia;
total_horas = float(input("Digite a média de horas estudadas por dia: "))

# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
curso = input("Digite o título do curso desejado: ")

# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
print(f"Estudante: {nome}")
print(f"Total de dias dedicados ao estudo por semana: {total_dias}")
print(f"Total de horas estudadas por dia: {total_horas}")
print(f"Título do curso desejado: {curso}")
print(f"Total de horas estudadas por semana: {total_dias * total_horas}")

print(f"Olá {nome}, você costuma estudar {total_dias} dias por semana, durante {total_horas} horas por dia. Você estuda em média {total_dias * total_horas} por semana para o curso {curso}.")