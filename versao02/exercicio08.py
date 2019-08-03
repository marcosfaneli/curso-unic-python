from calculo_de_notas import executar

def executar_ate_parar():
    executar()

    resposta = input('Deseja calcular a situação de um aluno?(S/N)')

    if resposta.upper() == 'S':
        executar_ate_parar()


if __name__ == '__main__':
    executar_ate_parar()