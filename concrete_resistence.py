import os
import math
import platform

load = 0
measure = 0
fcj = 0
g = 9.80665
flag1 = False
flag2 = False
f = 0
area = 0

def area_p(p):
    """ Return area based on perimeter of a circunference. """
    math.fabs(p)
    return round((p * p) / (4 * math.pi),2)

def area_d(d):
    """ Return area based on perimeter of a circunference. """
    math.fabs(d)
    return round((math.pi * d * d) / 4,2)

def get_force(load):
    "Return the force in newtons"
    return round(load * g, 2)

def get_fcj(f, a):
    """ Return the concrete resistence. """
    return round(f / a, 2)

def cls():
    " Clear the screen. "
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

while flag1 == False:
    print(" ")
    print("--- COMANDOS ---")
    print(" ")
    print("1 - Novo cálculo.")
    print("2 - Limpar tela.")
    print("3 - Sair.")
    print(" ")
    
    opt = int(input("O que deseja fazer? "))

    if opt == 1:
        print(" ")
        load = float(input("Insira o valor da carga em (kg): "))
        f = get_force(load)
        
        print(" ")
        print("Agora, escolha um método de cálculo...")
        print(" ")
        print("--- MÉTODOS DE CÁLCULO ---")
        print(" ")
        print("4 - Utilizando o perímetro.")
        print("5 - Utilizando o diâmetro.")
        print(" ")

        flag2 = False
        
        while flag2 == False:
            print(" ")
            opt = int(input("Qual método deseja utilizar? "))
        
            if opt == 4:
                print(" ")
                measure = float(input("Insira o valor do perímetro em (mm): "))
                roundarea = area_p(measure)
                fcj = get_fcj(f, area)
                flag2 = True
            elif opt == 5:
                print(" ")
                measure = float(input("Insira o valor do diâmetro em (mm): "))
                area = area_d(measure)
                fcj = get_fcj(f, area)
                flag2 = True
            else:
                print(" ")
                print("Opção inválida...")

        print(" ")
        print("--- RESULTADOS ---")
        print(" ")
        print("Força: ", f, " (N)")
        print("Area: ", area, " (mm²)")
        print("fcj: ", fcj, " (MPa)")   
                     
    elif opt == 2:
        cls()
    elif opt == 3:
        flag1 = True
        os._exit(1)
    else:
        print(" ")
        print("Opcao inválida, selecione outra...")
                      


    
