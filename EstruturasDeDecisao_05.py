# Faça um programa para a leitura de duas notas parciais de um aluno.
# O programa deve calcular a média alcançada por aluno e apresentar:
# A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
# A mensagem "Reprovado", se a média for menor do que sete;
# A mensagem "Aprovado com Distinção", se a média for igual a dez.

def estrutura_decisao_05():
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    m = ((n1+n2)/2)
    if m == 10:
        print('Sua média foi {} e você foi Aprovado com Distinção.'.format(m))
    elif 7 <= m <= 9.9:
        print('Sua média foi {} e você foi Aprovado.'.format(m))
    else:
        print('Sua média foi {} e você foi Reprovado.'.format(m))
estrutura_decisao_05()