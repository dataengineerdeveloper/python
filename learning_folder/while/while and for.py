#while

a = 0
while a<5:
    print(a)
    a+=1

#for
a=1
for a in range(5):
    print(a)

#a forma como está apresentados o while e o for vai dar o mesmo output.
#neste caso posso ver que a range é a até 5,  mas quero que os valores sejam apresentados em pares,  dai ter o 0,2,5,  o range fosse até 6 ou 7 o proximo valor que eu ia ver seria o 6
for a in range (0,5,2):
    print(a)
    
 #o que isto traduz basicamente é que vamos fazer o começar no -5 até ao 0 e vai ser incremental de 1 em 1   
for a in range( -5,0,1):
    print(a)
    
digitos = int(input('coloque o numero para sabermos o numero de digitos'))

contador = 0

while digitos !=0:
    digitos //=10
    contador+=1
print('total de digitos', contador)




