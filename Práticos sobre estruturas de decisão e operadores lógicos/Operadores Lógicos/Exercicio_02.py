# Questão 2: Condições Composta
# - Enunciado: Pergunte ao usuário dois valores: Sua idade e se ele possui permissão dos pais (sim/não). Se o usuário tiver menos de 18 anos e não tiver permissão dos pais, ele não pode participar da viagem. Use operadores lógicos  para avaliar as condições.

idade = int(input("Digite sua idade: "))
permissao = input("Você tem permissão dos pais? (s/n): ")

if idade > 17:
    print(f"Você está liberado para participar da viagem.")
elif permissao == "s":
    print(f"Você está liberado para participar da viagem, por conta da permissão dos pais.")
else:
    print(f"Infelizmente não poderá seguir conosco na viagem.")