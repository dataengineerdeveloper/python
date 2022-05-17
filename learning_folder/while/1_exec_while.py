print('\t --jogo dos digitos--')

digitos = int(input('inserir o seu valor e vamos indicar o numero de digitos'))

contador = 0

while digitos !=0:
    digitos //= 10
    contador +=1

print('o numero de digitos é', contador)
