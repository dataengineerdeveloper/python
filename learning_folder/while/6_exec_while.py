maior =-1
nr_digitado = int(input('inseriro um valor positivo: '))

while nr_digitado >=0:
    if nr_digitado>maior:
        maior=nr_digitado
        nr_digitado= int(input('inserir um novo numero positivo: '))
print('o valor', maior, 'é o maior valor digitados')
