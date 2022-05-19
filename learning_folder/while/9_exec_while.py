total = 0
valor =  float(input('informe o valor dos produtos: '))

while valor !=0:
    if valor <0:
        print('inserir um valor valido')
    else:
        total = total+valor
    valor = float(input('informe o valor do produtos'))
if total > 1000:
    total-=total*0.1
print('o total a pagar é: ', total)

