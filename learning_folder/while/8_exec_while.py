print('inserir os seus valor. Digite 0 para sair: ')

contador = 0
soma = 0.0
num = 1

while num !=0:
    num = int(input(""))
    soma = soma + num
    contador +=1
if contador == 0:
    print('digite alguns numeros')
else:
    print('media = ' , soma/(contador-1))
    print('soma dos numeros ', soma)
    