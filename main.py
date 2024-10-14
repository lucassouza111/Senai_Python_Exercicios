# Escreva um programa que verifique se um número é par ou ímpar.
numero = float(input("Escreva um número e verifique se é par ou impar."))

def calculo(digito):
    if digito % 2 == 0:
        return "Par"
    else:
        return "Ímpar"

print(f"O número digitado é {calculo(numero)}")

#desenvolva um algoritmo que peça ao usuário sua idade e retorno se ele pode votar ou não.
idade = int(input("Escreva a sua idade atual."))

def minimaIdade(situacao):
    if situacao >= 16:
        return True
    return False

resposta = "permite" if minimaIdade(idade) else "não permite"
print(f"A sua idade {resposta} você de votar.")
