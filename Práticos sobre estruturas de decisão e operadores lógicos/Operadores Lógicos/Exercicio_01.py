# Questão 1: Múltiplas Condições
# - Enunciado: Verifique se um número é positivo e par. Solicite um número ao usuário e imprima se ele satisfaz ambas as condições.

numero = int(input("Digite um número: "))

if numero >= 0 and numero % 2 == 0:
    print(f"O número {numero} atende por ser positivo e par.")
else:
    print(f"O número {numero} não atende, pois não é positivo e par, simultaneamente.")
