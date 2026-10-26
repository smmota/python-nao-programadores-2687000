# Crie uma função para selecionar o curso desejado em uma trilha profissional
# Crie uma função para percorrer todos os níveis de um curso e imprimir na tela a informação do nível atual
# Execute as funções

def selecionar_curso():
  curso = int(input("Digite o código do curso desejado: 1 - Python, 2 - Java, 3 - JavaScript: "))
  return curso

def curso_selecionado(curso):
  trilha = {1: {'titulo': 'Python', 'total_niveis': 3}, 
            2: {'titulo': 'Java', 'total_niveis': 5}, 
            3: {'titulo': 'JavaScript', 'total_niveis': 7}}
  # return trilha.get(curso, "Curso não encontrado")
  curso_atual = trilha[curso]['titulo']
  curso_nivel_atual = 1
  curso_total_niveis = trilha[curso]['total_niveis']

  print(f'Bem vindo ao curso de {curso_atual}! Você está iniciando o nível {curso_nivel_atual} de {curso_total_niveis}.\n......')

  while curso_nivel_atual <= curso_total_niveis:
    print(f'Parabéns! Você concluiu o nível {curso_nivel_atual} de {curso_total_niveis} do curso de {curso_atual}.')
    curso_nivel_atual += 1
  else:
    print(f'Parabéns! Você concluiu o curso de {curso_atual} com sucesso!')

curso = selecionar_curso()
curso_selecionado(curso)