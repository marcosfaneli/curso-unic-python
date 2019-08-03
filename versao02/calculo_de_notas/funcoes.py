def obter_nome_do_aluno():
    nome = input('Digite o nome do aluno: ')
    return nome


def obter_notas_do_aluno():
    notas = []
    quantidade_de_notas = 2

    i = 0
    while i < quantidade_de_notas:
        nota = float(input('Digite sua nota:'))
        notas.append(nota)
        i += 1

    return notas


#print('Notas do aluno {}:'.format(nome))
#for nota in notas:
#    print('Nota: {}'.format(nota))

def calcular_media_das_notas(notas):
    quantidade_de_notas = len(notas)
    soma = 0
    for nota in notas:
        soma += nota

    print('Total de pontos alcançados: {}'.format(soma))

    media = soma / quantidade_de_notas

    print('Média obtida: {}'.format(media))

    return media


def exibir_resultado_do_aluno(nome, media):
    if media >= 7:
        print('Aluno {} aprovado'.format(nome))
    else:
        print('Aluno {} reprovado'.format(nome))


