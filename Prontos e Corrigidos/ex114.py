'''
Crie um código em python que verifique se o site Pudim está acessível pelo computador usado.
'''
from urllib import request, error


try:
    request.urlopen('http://www.pudim.com.br')
except error.URLError:
    print("\033[31mPoxa! O site www.pudim.com.br não está acessível no momento. :(\033[m")

except Exception as erro:
    print("\033[31mExceção não tratada.\033[m")
    print(erro.__class__)
else:
    print("Opa! O site www.pudim.com.br está acessível no momento!")