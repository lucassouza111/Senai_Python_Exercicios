# Controle de Formatação de Números Decimais
# Objetivo: Criar um programa que formate números decimais.
# - Descrição: Peça ao usuário para inserir um número flutuante e o número de casas decimais desejado. Use f-strings para formatar o número com o número de casas decimais especificado e exiba o resultado.

numero = float(input("Escreva um número: "))
casas = int(input("Quantas casas decimais deseja? "))

print(f'O número ajustado é: {numero: .{casas}f}')
