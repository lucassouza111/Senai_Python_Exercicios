# Loop de Números Primos
# Objetivo: Escrever um script que identifique números primos em um intervalo.
# - Descrição: Use um loop 'for' para interar de 2 até um número (N) fornecido pelo usuário e dentro do loop, use outro loop para verificar se o número atual é primo. Imprima cada número primo encontrado.

numero = int(input("Informe um número, positivo maior que um, e verifique quais são os número primo: "))

for i in range(2, numero):
    div = 0
    for x in range(1,i+1):
       if i % x == 0:
           div += 1
    if div ==2:
        print(f"{i}, ", end='')
