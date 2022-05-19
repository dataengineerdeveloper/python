#criar um programa que faça  validaçao de uma senha onde respeite um conjunto de factores
import re


senha = input('criar a sua senha: ')

x = True

while x:
    if (len(senha)<6 or len(senha)<12):
        break
    elif not re.search('[a-z]',senha):
        break
    elif not re.search('[0-9]',senha):
        break
    elif not re.search('[A-Z]',senha):
        break
    elif not re.search('[$#@]',senha):
        break
    elif re.search("\s",senha):
        break
    else:
        print("senha valida")
        x=False
        break
if x:
    print("senha invalida")
    