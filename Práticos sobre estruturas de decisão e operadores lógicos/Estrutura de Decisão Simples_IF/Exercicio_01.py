# Questão 1: Verificar Positividade
# - Enuciado: Escreva um programa que peça ao usuário para digitar um número. Use a estrutura de decisão simples para verificar se o número é positivo. Se for, imprima "O número é positivo".

numero = float(input("Digite um número: "))

resposta = "O número é positivo" if numero >=0 else ""

print(resposta)
