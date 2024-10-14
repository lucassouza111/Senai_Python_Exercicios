# Função de Cálculo do Fatorial
# Objetivo: Criar uma função que calcule o fatorial de um número dado.
# - Descrição: Peça ao usuário para inserir um número e use uma função para calcular e retornar o fatorial desse número. O fatorial de um número não negativo (n), denotado por (n!), é o produto de todos os números positivos menores ou iguais a (n).

from math import factorial

numero = int(input("Informe um número, positivo maior que zero, que deseja calcular o fatorial: "))

print (factorial(numero))

# ou, por repetição

def calcularFatorial(num):
    saida = 1
    for x in range(1,num+1):
        saida *= x
    return saida

resposta = calcularFatorial(numero)

print(resposta)
