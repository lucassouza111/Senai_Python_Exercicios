# Questão 2: Classificação por Faixa Etária
# - Enunciado: Escreva um programa que peça a nota final de um aluno e o classifique em 'Excelente', 'Bom', 'Satisfatório', 'Insuficiente', usando uma estrutura de decisão encadeada.

nota = float(input("Digite a nota do aluno: "))

if nota < 4:
    print(f"A nota {nota} está na classificação Insuficiente.")
elif nota < 7:
    print(f"A nota {nota} está na classificação Satisfatório.")
elif nota < 9:
    print(f"A nota {nota} está na classificação Bom.")
else:
    print(f"A nota {nota} está na classificação Excelente.")
