# Simulador de Dados Financeiros
# Objetivo: Solicite ao usuário um saldo inicial, a taxa de juros anual e o número de anos. Use um loop 'while' para simular o aumento do saldo com juros compostos ao longo dos anos e imprima o saldo final após o período especificado.

inicial = float(input("Informe o saldo inicial desejado: "))
taxaAno = float(input("Informe a taxa de juros anual, a ser aplicado (sem '%'): "))/100
periodo = int(input("Informe quantos anos, ficará investido: "))
final = inicial
i = 1

while i <= periodo:
    final += (final * taxaAno)
    i += 1

print(f'Saldo Final: {final: .2f}')
