'''
Criando mini perguntados em aula
'''

print('-'*30,'Um pequeno perguntados bíblicos','-'*30)
print('Para responde apenas digite '
      '\na letra que está entre parênteses'
      '\nexemplo: Digite a resposta: A')
print('-'*43,'INICIO','-'*43)


respostas_certas = 0
perguuntas = {
    'Pergunta 1': {
        'pergunta': 'Quem caminhou sobre as águas até Jesus Cristo ?',
        'respostas': {

            'A': 'João',
            'B': 'Tiago',
            'C': 'Jonas',
            'D': 'Moisés',
            'E': 'Pedro',
        },

        'respota_certa':'E'

    },

    'Pergunta 2': {
        'pergunta': 'Qual é o novo nome de Saulo ?',
        'respostas': {

            'A': 'João',
            'B': 'Tiago',
            'C': 'Paulo',
            'D': 'Moisés',
            'E': 'Pedro',
        },

        'respota_certa':'C'

    },

    'Pergunta 3': {
        'pergunta': 'Jesus Cristo tránsformou água em ?',
        'respostas': {

            'A': 'Suco',
            'B': 'Vinho',
            'C': 'Limonada',
            'D': 'Refrigerante',
            'E': 'Suco de maçâ',
        },

        'respota_certa':'B'
    },
}

# pk = chave e pv = valor
print()
for  pk, pv in perguuntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')
    print()
    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_user = input('Sua resposta: ')
    print()

    if resposta_user.upper() == pv['respota_certa']:
        print(f'EEHHHHHH!!! Você acertou ! A resposta ')
        respostas_certas += 1
    else:
        print('Lmento você errou')
    print()

qtd_perguntas = len(perguuntas)
porcentagem_de_acerto = respostas_certas / qtd_perguntas * 100

if  respostas_certas > 0:
    print(f'Você acertou {respostas_certas} perguntas')

else :
    print('Você não acertou nenhuma pergunta')


print(f'Sua porcentagem de acerto e de {porcentagem_de_acerto}%')
