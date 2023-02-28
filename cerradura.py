import os
import sys


def menu(registro):
    opcion = 1

    while opcion >=1 and opcion <=4:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("""
---MENU DE CERRADURAS---
|1-Abrir/Cerrar |
|2-Registrar    |
|3-Cambiar PIN  |
|4-Salir        |
        """)
        if len(registro) == 0:
            opcion= int(input("No hay cerraduras registradas, ingrese para seguir | Opción: "))
            match opcion:
                case 2: registrar(registro)
                case 4: sys.exit()
                case _: opcion = 1
        else:
            opcion = int(input("Ingrese una opción: "))
            match opcion:
                case 1: accionar(registro)
                case 2: registrar(registro)
                case 3: cambiarPin(registro)
                case 4: sys.exit()
                case _: opcion = 1

def leer():
    #Esta función lee los contenidos del documento "cerraduras.txt", que es donde se almacena la información
    registro = [] #se define la lista "registro", que manejará toda la información que necesitemos
    if (os.path.exists("cerraduras.txt") == False): #en caso de que el documento no esté creado, la función open con el comando w, crea el documento
        fp = open("cerraduras.txt", "w")
        menu(registro)
    else:
        with open("cerraduras.txt", "r") as fp: #a raíz de que el documento guarda los identificadores "nombre" y "PIN", hay que guardar los valores de por medio
            numLinea = [1] #este array empezará a guardar valores en 2, lo que obtendrá los valores de las cerraduras (recordando que las lineas de txt también se leen desde 0)
            for i, linea in enumerate(fp):
                if i in numLinea: #se lee de linea por medio empezando en 1
                    registro.append(linea.strip())
                    numLinea.append(i+2)
            menu(registro)


def accionar(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
    resp = 1
    while resp == 1:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--ABRIR / CERRAR--\n")
        print("CERRADURAS DISPONIBLES:\n")

        num = 1 #esta variable simplemente enumera las cerraduras
        dato = 0 #esta variable salta de un nombre de cerradura a otra
        nombres = [] #aquí se almacenan únicamente los nombres de las cerraduras para posteriormente usarlas para modificar el PIN de una cerradura específica

        #MUESTRA DE CERRADURAS
        for i in range(len(registro)):
            print(f"{num}- Nombre: {registro[dato]}")
            if registro[dato+1] == '0':
                print("Estado: Cerrado")
            else: 
                print("Estado: Abierto")
            nombres.append(registro[dato])
            dato += 3
            num += 1
            if dato == len(registro): break
        print("\n")



        
        #ELECCIÓN DE CERRADURA
        correct = False
        while correct == False:
            select = int(input("Ingrese el # de la cerradura a modificar: "))
            if select > len(nombres): accionar(registro)
            else:
                correct = True
                for i in range(len(registro)):
                    if (nombres[select-1] == registro[i]):
                        cerradura = i
                        desc = 0
                        while desc != 1 and desc !=2:
                            if registro[i+1] == "0":
                                desc = int(input("La cerradura se encuentra cerrada, desea abrirla? 1-Si 2-No: "))
                            elif registro[i+1] == "1":
                                desc = int(input("La cerradura se encuentra abierta, desea cerrala? 1-Si 2-No: "))
                            if desc != 1 and desc !=2: print("Opción inválida\n")
                
                        
        #VERIFICACIÓN DE PIN
        opt = 0
        if desc == 2: menu(registro)
        else:
            verified = False
            while verified == False and opt != 1: 
                opt = 0
                pin = input("Ingrese el PIN de la cerradura: ") 
                if registro[cerradura+2] == pin: 
                    verified = True
                    if registro[cerradura+1] == "0": #si la cerradura está cerrada, se abrirá cambiando el valor a 1 y viceversa
                        registro[cerradura+1] = "1"
                        print("La cerradura se ha abierto")
                    else: 
                        registro[cerradura+1] = "0"
                        print("La cerradura se ha cerrado")
                else:
                    print("PIN inválido\n")
                    while opt != 1 and opt !=2:
                        opt = int(input("¿Desea salir al menú principal? 1-Si 2-No: ")) #la respuesta debe de ser 1 o 2
                        if opt != 1 and opt != 2: print("Opción no valida\n")


        #ESCRITURA EN TXT FILE
        titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
        with open("cerraduras.txt", "w") as f: #se abre el documento
            for i in range(len(registro)):
                if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                    f.write("Nombre:\n")
                    f.write(registro[i]) 
                    titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
                elif titulo == 1: #si el titulo es 1, se escribirá "Estado"y su dato
                    f.write("Estado:\n")
                    f.write(registro[i]) 
                    titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
                elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                    f.write("PIN:\n")
                    f.write(registro[i]) 
                    titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
                f.write("\n")
        print("\n")
        while resp != 1 or resp != 2: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
            resp = int(input("¿Desea modificar otra cerradura? 1-Si 2-No | Resp: "))
            if resp == 1: break #Si la respuesta es sí, vuelve a comenzar el proceso de registro
            elif resp == 2: menu(registro) #Si es no, se abre el menú
            else: print("Opción no valida") #Cualquier otra opción dará error
        print("Prueba")

#prueba
def registrar(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
    resp = 1
    while resp == 1:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--REGISTRO DE CERRADURA--")
        repetido = False
        if len(registro) > 0: 
            nombre = input("Nombre: ")
            for i in range(len(registro)):
                if nombre.lower() == registro[i].lower(): 
                    repetido = True
                    break
                i+=3
                if i>len(registro):break
            if repetido == True:
                intento = 0
                print("Este nombre ya existe")
                while intento != 1 and intento != 2: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
                    intento = int(input("¿Desea volver a intentar? 1-Si 2-No | Resp: "))
                    if intento == 1: registrar() #Si la respuesta es sí, vuelve a comenzar el proceso de registro
                    elif intento == 2: menu(registro) #Si es no, se abre el menú
                    else: print("Opción no valida\n") #Cualquier otra opción dará error
        else:
            registro.append(input("Nombre: "))
        #COMPROBAR QUE EL NOMBRE NO EXISTA !!!!!!!!!!!

        #VALIDACIÓN DE ESTADO
        estado = "inactive"
        while estado != "1" or estado != "0": #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
            estado = input("Estado 1-Abierto 0-Cerrado: ")
            if estado == "1" or estado == "0": 
                registro.append(estado)
                break
            else:
                print("Opción no valida")

        #VALIDACIÓN DE PIN
        valid = False
        while valid == False: #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
            pin = input("PIN numeral(entre 4 y 6 números): ")
            if len(pin)>=4 and len(pin)<= 6: 
                registro.append(pin)
                break
            else:
                print("Opción no valida")

        titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
        #ESCRITURA EN TXT FILE
        with open("cerraduras.txt", "a") as f: #se abre el documento
            for i in range(3):
                if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                    f.write("Nombre:\n")
                    f.write(registro[len(registro)-3]) #El ante-penúltimo dato de la lista siempre será un nombre de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                    titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
                elif titulo == 1: #si el titulo es 1, se escribirá "PIN" y su dato
                    f.write("Estado:\n")
                    f.write(registro[len(registro)-2]) #El penúltimo dato de la lista siempre será un estado de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                    titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
                elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                    f.write("PIN:\n")
                    f.write(registro[len(registro)-1]) #El último dato de la lista siempre será un PIN de cerradura, por lo que se utiliza ese valor para escribirlo en el .txt
                    titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
                f.write("\n")
        while resp != 1 or resp != 2: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
            resp = int(input("¿Desea guardar otra cerradura? 1-Si 2-No | Resp: "))
            if resp == 1: break #Si la respuesta es sí, vuelve a comenzar el proceso de registro
            elif resp == 2: menu(registro) #Si es no, se abre el menú
            else: print("Opción no valida") #Cualquier otra opción dará error


def cambiarPin(registro):
    os.system('clear' if os.name == 'posix' else 'cls')
    resp = 1
    while resp == 1:
        os.system('clear' if os.name == 'posix' else 'cls')
        print("--CAMBIO DE PIN--\n")
        print("CERRADURAS DISPONIBLES:\n")

        num = 1 #esta variable simplemente enumera las cerraduras
        dato = 0 #esta variable salta de un nombre de cerradura a otra
        nombres = [] #aquí se almacenan únicamente los nombres de las cerraduras para posteriormente usarlas para modificar el PIN de una cerradura específica
        #MUESTRA DE CERRADURAS
        for i in range(len(registro)):
            print(f"{num}- Nombre: {registro[dato]}")
            nombres.append(registro[dato])
            dato += 3
            num += 1
            if dato == len(registro): break
        print("\n")
        #ELECCIÓN DE CERRADURA
        select = int(input("Ingrese el # de la cerradura a modificar: "))
        if select > len(nombres): cambiarPin(registro)
        else:
            for i in range(len(registro)):
                if (nombres[select-1] == registro[i]):
                    oldpin = registro[i+2] #se busca el PIN de la cerradura que se desea modificar para posteriormente verificar que el usuario conoce el PIN actual
                    break

        #VERIFICACIÓN DE PIN
        verified = False
        opt = 0
        while verified == False and opt != 1: #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
            opt = 0
            pin = input("Ingrese el PIN actual: ")
            if oldpin == pin: verified = True
            else:
                print("PIN incorrecto\n")
                while opt != 1 and opt !=2:
                    opt = int(input("¿Desea salir al menú principal? 1-Si 2-No: ")) #la respuesta debe de ser 1 o 2
                    if opt != 1 and opt != 2: print("Opción no valida\n")
                        
        #INGRESO DE NUEVO PIN
        if verified == False: menu() #si se llega a este punto sin haber verificado, se devuelve al usuario al menú principal
        else:
            valid = False
            while valid == False: #el estado tiene que ser tiene que ser 1 o 2, de lo contrario no podrá continuar
                newpin = input("\nIngrese el nuevo PIN numeral(entre 4 y 6 números): ") #se hace la misma validación de PIN que en el registro
                if len(newpin)>=4 and len(newpin)<= 6: 
                    valid = True #el PIN es válido por lo que se cambia a true, después de intercambiar los PIN no volverá a entrar
                    for i in range(len(registro)): #se procede a cambiar el PIN en la lista para posteriormente hacer la modificación del cerraduras.txt
                        if (nombres[select-1] == registro[i]):
                            registro[i+2] = newpin #se intercambia el anterior PIN por el nuevo
                            break
                else:
                    print("PIN no válido")
            print("Logrado")
            

        #ESCRITURA EN TXT FILE
        titulo = 0 #variable que decidirá qué tipo de dato se escribirá en el .txt
        with open("cerraduras.txt", "w") as f: #se abre el documento
            for i in range(len(registro)):
                if titulo == 0: #si el titulo es 0, se escribirá "Nombre" y su dato
                    f.write("Nombre:\n")
                    f.write(registro[i]) 
                    titulo += 1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el estado
                elif titulo == 1: #si el titulo es 1, se escribirá "Estado"y su dato
                    f.write("Estado:\n")
                    f.write(registro[i]) 
                    titulo +=1 #Se aumenta en 1 el titulo para que la siguiente escritura sea para el PIN
                elif titulo == 2: #si el titulo es 1, se escribirá "PIN" y su dato
                    f.write("PIN:\n")
                    f.write(registro[i]) 
                    titulo = 0 #Se devuelve la variable a 0 para que la próxima escritura sea de un Nombre de Cerradura
                f.write("\n")
        print("\n")
        while resp != 1 or resp != 2: #Después de haber guardado la cerradura, se pregunta cuál es la siguiente acción
            resp = int(input("¿Desea modificar otra cerradura? 1-Si 2-No | Resp: "))
            if resp == 1: break #Si la respuesta es sí, vuelve a comenzar el proceso de registro
            elif resp == 2: menu(registro) #Si es no, se abre el menú
            else: print("Opción no valida") #Cualquier otra opción dará error
#leer() #Código empieza con la función leer