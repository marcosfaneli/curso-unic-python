from exercicio06 import obter_nome_do_aluno
from exercicio06 import obter_notas_do_aluno
from exercicio06 import calcular_media_das_notas
from exercicio06 import exibir_resultado_do_aluno

def executar():
    nome_do_aluno = obter_nome_do_aluno()
    notas = obter_notas_do_aluno()
    media = calcular_media_das_notas(notas)
    exibir_resultado_do_aluno(nome_do_aluno, media)

executar()