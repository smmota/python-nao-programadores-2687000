# Nesse desafio você verificará dentro de uma lista se o item estar contido nela, caso verdadeiro deverá imprimir na tela essa informação, além disso deverá solicitar avaliação para o item e armazená-la em um dicionário.
# 1. Crie uma lista com 5 diferentes cursos do LinkedIn Learning
# 2. Crie 3 variáveis do tipo string e associe 1 curso a cada uma delas
# 3. Crie um dicionário vazio para armazenar a nota do curso
# 4. Crie uma estrutura condicional para verificar se cada variável está contida na lista
# 5. Se o curso estiver na lista, solicite uma nota para avaliação
# 6. Armazene essa nota no dicionário, sendo a chave o título do curso e o valor a nota

lista_cursos = ['Python para Iniciantes', 'JavaScript Essencial', 'Excel Avançado', 'Marketing Digital', 'Gestão de Projetos']
curso1 = 'Python para Iniciantes'
curso2 = 'JavaScript Essencial'
curso3 = 'Excel Avançado'
avaliacoes = {}

if curso1 in lista_cursos:
    nota1 = float(input(f"Digite a nota para o curso '{curso1}': "))
    avaliacoes[curso1] = nota1
elif curso2 in lista_cursos:
    nota2 = float(input(f"Digite a nota para o curso '{curso2}': "))
    avaliacoes[curso2] = nota2
elif curso3 in lista_cursos:
    nota3 = float(input(f"Digite a nota para o curso '{curso3}': "))
    avaliacoes[curso3] = nota3
else:
    print("Nenhum dos cursos informados está na lista.")

if len(avaliacoes) > 0:
  print(avaliacoes)
# for curso, nota in avaliacoes.items():
#     print(f"{curso}: {nota}")