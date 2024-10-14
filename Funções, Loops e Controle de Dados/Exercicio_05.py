# Programa de Mensgens com Loop Infinito
# Objetivo: Desenvolver um programa que permita ao usuário enviar mensagens repetidamente até decidir sair.
# - Descrição: implemente um loop infinito que peça ao usuário para digitar uma mensagem. Após cada mensagem, pergunte se o usuário deseja continuar ou sair. Use a palavra-chave 'sair' para quebrar o loop. Cada mensagem, juntamente com uma confirmação de recebimento, deve ser exibida na tela.

mensagem = ""
i = "1"

while i != "SAIR":
    print (str(input("Escreva a sua mensagem: ")).upper())
    i = str(input("Deseja escrever outra mensagem? Escreva 'sim', para continuar, ou 'sair' para finalizar. ")).upper()
print("Finalizado!")
