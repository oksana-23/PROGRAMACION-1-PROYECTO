#va en no se donde

import os
def equipo():
    n = ["Valentini Augusto, Jesus Quijada, Centurion G0nzalo, Leomagno Ernesto, Oksana Bernkhart, Luis Agustin Chen"]
    print(n)
    opcion = int(input("Ingrese opción: "))
    

def main():
    repetir = True
    while repetir:
        os.system("cls")
        print("------------>1. Equipos      .<------------")
        print("------------>2. Inst         .<------------")
        print("------------>3. Ejecutar     .<------------")
        print("------------>4. Juego        .<------------")
        print("------------>5. Salir        .<------------")
        try:
            opcion = int(input("Ingrese opción: "))
            if opcion == 1:
                equipo()
                print("Hola mundo!")
            elif opcion == 2:
                print("Hola mundo!")
            elif opcion == 3:
                print("Hola mundo!")
            elif opcion == 4:
                print("Hola mundo!")
            else:
                print("Chau mundo!")
                opcion = int(input("Ingrese opción: "))
        except:
                print("Error")
                opcion = int(input("Ingrese opción: "))
        

if __name__ == "__main__":
    main()



