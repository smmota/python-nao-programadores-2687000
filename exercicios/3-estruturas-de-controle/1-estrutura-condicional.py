# Declare 4 variáveis do tipo numérica
a = 2
b = 8
c = 5
d = 10

# Crie uma estrutura condicional para comparar dois números
# Se a condição for verdadeira, imprima na tela uma mensagem informando que a condição foi cumprida e informando o número de maior valor
# Se a condição não for cumprida, imprima na tela uma mensagem informando que a condição é negativa e informe o número de maior valor
# Insira outras condições na estrutura condicional usando o elif
# Incremente a estrutura condicional já existente com expressões lógicas utilizando "and" ou "or"
# Crie uma estrutura condicional onde mais de uma condição seja verdadeira, e use apenas a palavra reservada "if"

print('Primeiro teste de estrutura condicional')
if (a > b):
  print(f"A condição é verdadeira: {a} é maior que {b}")
else:
  print(f"A condição é negativa: {b} é maior que {a}")

print('Segundo teste de estrutura condicional')
if (a > b):
  print(f"A condição é verdadeira: {a} é maior que {b}")
elif (d >= (a+b)):
  print(f"A condição é verdadeira: {d} é maior ou igual que {a+b}")
else:
  print(f"A condição é negativa: {b} é maior que {a}")  

print('Terceiro teste de estrutura condicional')
if (d > a and d > b):
  print(f"A condição é verdadeira: {d} é maior que {a} e {b}")

print('Quarto teste de estrutura condicional')
if (a < b):
  print(f"A condição é verdadeira: {a} é menor que {b}")
if (d >= (a+b)):
  print(f"A condição é verdadeira: {d} é maior ou igual que {a+b}")
if (d > a and d > b):
  print(f"A condição é verdadeira: {d} é maior que {a} e {b}")  