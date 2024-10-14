# Questão 1: Classificação por Faixa Etária
# -Enunciado: Peça a idade do usuário e classifique-o em categorias ('Criança', 'Adolescente', 'Adulto', 'Idoso') usando "if-elif-else".

idade = int(input("Digite sua idade: "))

if idade < 13:
    print(f"A idade {idade} está na categoria Criança.")
elif idade < 18:
    print(f"A idade {idade} está na categoria Adolescente.")
elif idade < 63:
    print(f"A idade {idade} está na categoria Adulto.")
else:
    print(f"A idade {idade} está na categoria Idoso.")
