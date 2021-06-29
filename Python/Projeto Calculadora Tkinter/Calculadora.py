# -*- coding: UTF-8 -*- 

import sys


#Menu Inicial

def menu():
    print("")
    print("Seja Bem Vindo")
    print("")
    var = int (input('''Para calcular digite a tecla correspondente:
     ---------------------------
    | < 1 > Para SOMA           |
    | < 2 > Para SUBTRAÇÃO      |
    | < 3 > Para MULTIPLICAÇÃO  |
    | < 4 > Para DIVISÃO        |
    | < 5 > Para RAIZ QUADRADA  |
    | < 6 > Para RAIZ CÚBICA    |
    | < 7 > Para EQUAÇÕES       |
    | < 0 > SAIR                |
     ---------------------------

     '''))

    if var == 1:
        soma()

    elif var == 2:
        subtracao()

    elif var == 3:
        multiplicacao()

    elif var == 4:
        divisao()
        
    elif var == 5:
        raiz_quadrada()
        
    elif var == 6:
        raiz_cubica()
        
    elif var == 7:
        equacao()
        
    elif var > 7:
        import sys
        try:
            var > 7
            print("Opção invalida por favor reinicie a aplicação")
        except ValuerError:
            sys.exit(3)
    else:
        import sys
        try:
            var == 0
            print("Obrigado, até a próxima")
        except ValuerError:
            sys.exit(0)

#SOMA
def soma():
    print("Iniciando...")
    num1 = float (input("Por favor, entre com o primeiro número: "))
    print("")
    num2 = float (input("Por favor, entre com o segundo número: "))
    print("")
    som = (num1 + num2)
    print("")
    print("O resultado da soma é:", +som)
    var= float (input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        soma()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)
        
#SUBTRAÇÃO
def subtracao():
    print("Iniciando...")
    num1 = float (input("Por favor, entre com o primeiro número: "))
    print("")
    num2 = float (input("Por favor, entre com o segundo número: "))
    print("")
    subt = (num1 - num2)
    print("")
    print("O resultado da subtração é:", +subt)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        subtracao()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)
                       
#MULTIPLICAÇÃO
def multiplicacao():
    print("Iniciando...")
    num1 = float (input("Por favor, entre com o primeiro número: "))
    print("")
    num2 = float (input("Por favor, entre com o segundo número: "))
    print("")
    multi = (num1 * num2)
    print("")
    print("O resultado da multiplicação é:", +multi)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        multiplicacao()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)

#DIVISÃO
def divisao():
    print("Iniciando...")
    num1 = float (input("Por favor, entre com o primeiro número: "))
    print("")
    num2 = float (input("Por favor, entre com o segundo número: "))
    print("")
    divi = (num1 / num2)
    print("")
    print("O resultado da divisão é:", +divi)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        divisao()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)
            
#RAIZ QUADRADA
def raiz_quadrada():
    print("")
    num1 = float (input("Por favor, entre com o primeiro numero: "))
    rq = (num1 ** (1/2))
    print("")
    print ("A raiz quadrada é: ", +rq)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        raiz_quadrada()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)

#RAIZ CUBICA
def raiz_cubica():
    print("")
    num1 = float (input("Por favor, entre com o primeiro numero: "))
    rc = (num1 ** (1/3))
    print("")
    print ("A raiz cúbica é: ", +rc)
    var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        raiz_cubica()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)

def equacao():
    
    A = float (input("Entre com o valor de A: "))
    B = float (input("Entre com o valor de B: "))
    C = float (input("Entre com o valor de C: "))

    if A == 0:
        
        X = -((C)/B)
        print ("Equação de primeiro grau, raiz: ", +X)
    else:
        
        Delta = ((B ** 2) - 4*A*C)
        print ("Delta igual a:", +Delta)
        if Delta < 0:
            
            print ("Equação não tem solução no conjunto dos reais")
        elif Delta == 0:
            
            print ("Equação só possui uma raíz real")
            X= (-B /(2*A))
            print ("Raiz da equação: ", X)
        elif Delta > 0:
            
            X1= (-B+ (Delta)**(1/2))/(2*A)
            X2= (-B- (Delta)**(1/2))/(2*A)
            print ("Equação possui duas raízes reais, são elas:")
            
            print ("X1: ", +X1) 
            print ("X2: ", +X2)
            var= int(input('''

    Para calcular novamente tecle: 1
    Para voltar ao menu principal: tecle 2
    Para sair: tecle 0 



    '''))

    if var == 1:
        equacao()
    else:
        if var == 2:
            menu()
        else:
            if var >= 2:
                try:
                    var >2
                    print("Opção invalida por favor reinicie a aplicação")
                except ValuerError:
                    
                    sys.exit(0)
            else:
                if var == 0:
                   import sys
                   try:
                       var == 0
                       print("Obrigado, até a próxima")
                   except ValuerError:
                       
                       sys.exit(0)

if __name__ == '__main__':
    menu()

