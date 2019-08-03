nome = input("Digite seu nome: ")
print("olá {}".format(nome))

contador = 0
notas = []

# while contador < 4:
for i in (0,4):
    valor = input("Insira a nota {}: ".format(contador + 1))
    notas.append(float(valor))
    #contador += 1

soma = 0

for nota in notas:
    print(nota)
    soma += nota

media = soma / 4

print("Sua média é: {}".format(media))

if media >= 7.:
    print("Você esta aprovado")
else:
    print("Você esta reprovado")