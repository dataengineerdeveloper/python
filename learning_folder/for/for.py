#break and contniue


#aqui mesmo o qvalor chegue a a 3 os valor vai continuar,  neste caso a range é de 5,  mas o valor começar o 0, portatanto começar  contar do 0,  
#logo a contagem vai apaneas até ao 4,.
for i in range(5):
    if i == 3:
        continue
    print(i)

# no momento que o ciclo chegar ao 3 o ciclo vai parar, ou seja vai fazer o break, apresentando apenas dados de 0,1,2...
for i in range(5):
    if i == 3:
        break
    print(i)
