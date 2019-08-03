def calcularMedia(notas):
    soma = 0
    
    for nota in notas:
        print(nota)
        soma += nota

    return soma / len(notas)


def obterNotas():
    contador = 0

    notas = []

    while contador < 4:
        valor = input("Insira a nota {}: ".format(contador + 1))
        notas.append(float(valor))
        contador += 1

    return notas


def exibirResultado(media):
    print("Sua média é: {}".format(media))

    if media >= 7.:
        print("Você esta aprovado")
    else:
        print("Você esta reprovado")


def run():
    nome = input("Digite seu nome: ")
    print("olá {}".format(nome))

    notas = obterNotas()

    media = calcularMedia(notas)

    exibirResultado(media)


if __name__ == '__main__':
    run()