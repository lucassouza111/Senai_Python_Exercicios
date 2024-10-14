# Questão 2: Par ou Ímpar
# Enunciado: Solicite um número do usuário e use 'if-else' para determinar se o número é par ou ímpar. Imprima o resultado apropriado.

idade = int(input("Digite um número: "))

if idade % 2 == 0:
    print(f"O número {idade} é par.")
else:
    print(f"O número {idade} é ímpar.")
