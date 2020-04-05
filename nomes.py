'''
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
'''
nome = input('Digite seu nome: ')

tamanho = len(nome)

if tamanho <= 4:
    print(f'nome: {nome}, tamaho {tamanho}, seu nome é pequeno')
elif tamanho <= 6:
    print(f'nome: {nome}, tamanho {tamanho} seu nome é normal')
else:
    print(f'seu nome: {nome}, tamanho {tamanho}, seu nome é muito grande')
