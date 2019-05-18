nome = input("Digite seu nome: ")
print("olá {}".format(nome))
media = input("Sua media? ")
valor = float(media)

if valor >= 7.:
    print("Você esta aprovado")
else:
    print("Você esta reprovado")