print('t\ --sequencia de fibonnaci--')

n = int(input('inserir a sequencia de numeros: '))

num1,num2 = 0,1
contador = 0

while contador < n:
     num3 = num1 + num2
     
     num1 = num2
     num2 = num3
     contador +=1
     
     print(num1)