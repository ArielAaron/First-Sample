import random 

def generar_contrasena():
    MAYUS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
    MINUS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    NUMS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    CHARS = ['*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"']
    
    caracteres=MAYUS+MINUS+NUMS+CHARS
    contrasena=[]

    for i in range (10):
        caracter_random=random.choice(caracteres)          #Elige un caracter al azar de la lista()
        contrasena.append(caracter_random)

    contrasena="".join(contrasena)                         #Convertir en string
    return contrasena                                      #Retorna la contraseña


def run():
    password=generar_contrasena()
    print('Tu nueva contraseña es:' + password)

if __name__ == '__main__':
    run()
