# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: 
# nome, 
# ano que conheceu o LinkedIn, 
# ano atual e 
# os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica



# 2. Armazene esses dados em um dicionário


# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.

estudante = {
    'nome': input("Digite seu nome: "),
    'ano_conheceu_linkedin': int(input("Digite o ano que conheceu o LinkedIn: ")),
    'ano_atual': int(input("Digite o ano atual: ")),
    #'cursos': [curso.strip() for curso in input("Digite os cursos realizados no LinkedIn Learning separados por vírgula: ").split(",")]
    'cursos': input("Digite os cursos realizados no LinkedIn Learning separados por vírgula: ").split(",")
}

print(f"Nome: {estudante['nome']}")
anos_transcorridos = estudante['ano_atual'] - estudante['ano_conheceu_linkedin']
print(f"Total de anos transcorridos desde que conheceu o LinkedIn: {anos_transcorridos}")
print(f"Total de cursos realizados: {len(estudante['cursos'])}")
print(f"Primeiro curso realizado: {estudante['cursos'][0]}")
print(f"Último curso realizado: {estudante['cursos'][-1]}")