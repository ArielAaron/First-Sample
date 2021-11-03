import random                                         

def run():
    numero_aleatorio = random.randint(1, 100)   # Números pseudoaleatorio enteros randint()
    menu=""""
    Bienvenido a adivina el número

    1 - facil (20 intentos)
    2 - normal (10 intentos)
    3 - dificil (5 intentos)
    4 - tryhard (2 intentos)

    Elige una opción:
    """
## Implementación del sistema de vidas         
    opcion=int(input(menu))
    if opcion == 1:                      
        vidas = 20
        pista_menor ="Elige un número más pequeño"
        pista_mayor ="Elige un número más grande"
    elif opcion == 2:
        vidas = 10
        pista_menor ="Elige un número más pequeño"
        pista_mayor ="Elige un número más grande"    
    elif opcion == 3:
        vidas = 5
        pista_menor = "No hay pista :C"
        pista_mayor = "No hay pista :C"
    elif opcion == 4:
        print("Si ganas, hoy es tu día aprovecha y juega la lotería")
        vidas = 2   
        pista_menor = "No hay pista :C"
        pista_mayor = "No hay pista :C"
    else:
        print('Ingresa una opción correcta')    
## Implementación de entrada del número elegido
    numeroelegido = int(input("Introduce un numero del 1 al 100 "))
    while numero_aleatorio != numeroelegido :             # != Desigualdad 

        if numero_aleatorio < numeroelegido : 
             print(pista_menor)
             vidas -= 1                                       # -= Disminuye el valor eq n=n-1
        elif numero_aleatorio > numeroelegido : 
             print(pista_mayor)            
             vidas -= 1
        if vidas == 0 :
            print("GAME OVER")
            print("El número aleatorio era " + str(numero_aleatorio) )
            break
        print("Tienes", vidas, "vidas")                      # Otra manera print("Tienes" +str(vidas)+ "vidas")
        numeroelegido = int(input("Introduce otro número: "))
        
    if numero_aleatorio == numeroelegido : 
        print("FELICIDADES GANASTE")


# defrun():
#     numero_aleatorio = random.randint(1,100)

#     menu = """
#     Bienvenido a adivina el número

#     1 - facil (20 intentos)
#     2 - normal (10 intentos)
#     3 - dificil (5 intentos)

#     Elige una opción: """

#     opcion = int(input(menu))

#     if opcion == 1:
#         vidas = 20
#     elif opcion == 2:
#         vidas = 10
#     elif opcion == 3:
#         vidas = 5
#     else:
#         print('Ingresa una opción correcta')
    
#     numero_elegido = int(input('Elige un número del 1 al 100: '))
#     while numero_elegido != numero_aleatorio:
#         vidas -= 1
#         if numero_elegido < numero_aleatorio:
#             print('Busca un número más grande')
#         else:
#             print('Busca un número más pequeño')
#         if vidas == 0:
#             print('Lo siento, perdiste')
#             break
#         print('Tienes ' + str(vidas) + ' vidas')
#         numero_elegido = int(input('Elige otro número: '))
#     print('¡Ganaste!')


# import random

# defrun():
#     numero_pensado= random.randint(1,100)
#     vida= 5
#     numero = int(input("Eligue un numero del 1 al 100:\n"))
#     while numero != numero_pensado:
#         if vida == 0:
#             print("""GAME OVER
#             El numero que pensé era """ + str(numero_pensado) )
#             perdio = True
#             break
#         if numero < numero_pensado:
#             vida -=1
#             print("VIDAS RESTANTES "+ str(vida))
#             numero = int(input("Busca un numero mas grande:\n"))

#         elif numero > numero_pensado:
#             vida -=1
#             print("VIDAS RESTANTES "+ str(vida))
#             numero = int(input("Busca un numero mas pequeño:\n"))
#     ifnot perdio:
#         print("Ganaste!")


# import random

# def run():
#     numero_aleatorio = random.randint(1,20)
#     numero_usuario_1 = int(input(f'Jugador 1 escoge un número del 1 al 20: '))
#     numero_usuario_2 = int(input(f'Jugador 2 escoge un número del 1 al 20: '))

#     while numero_usuario_1 != numero_aleatorio or numero_usuario_2 != numero_aleatorio:
#         if numero_usuario_1 != numero_aleatorio:
#             print('Jugador 1 No has ganado')
#         if numero_usuario_2 != numero_aleatorio:
#             print('Jugador 2 No has ganado')  
#         if numero_usuario_1 == numero_aleatorio:
#             print('¡Jugador #1 es el ganador!')
#             break
#         if numero_usuario_2 == numero_aleatorio:
#             print('¡Jugador #2 es el ganador!')
#             break 
#         numero_usuario_1 = int(input(f'Jugador 1 escoger otro número: '))
#         numero_usuario_2 = int(input(f'Jugador 2 escoger otro número: '))   
#     else: 
#         print(f'Empate técnico, vuelvan a jugar')    
#     print('Se acabo el juego')

if __name__ == "__main__" : 
    run()