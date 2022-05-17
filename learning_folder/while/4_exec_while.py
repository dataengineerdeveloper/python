senha1 = input('coloque a senha: ')
senha2 = input('coloque a mesma senha: ')

contador = 0

while senha1 != senha2:
    #colocar aqui a mensagem de erro,  para o caso de nao conseguir acertar na primeira oportunidade
    print('senha errada, insira novamente')
    #colocar novamente as opções
    senha1 = input('coloque a senha: ')
    senha2 = input('coloque a mesma senha: ')
    print('senha valida!')
    
    