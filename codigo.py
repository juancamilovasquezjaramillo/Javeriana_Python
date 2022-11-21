#!/usr/bin/env python3

"""
En este codigo se encuentran todas las funciones
principales del juego batalla naval,
esta consta de tres funciones las cuales se reparten
las funciones mas importantes
del juego.
"""
u = True
while u is True:
    def mainMenu():

        """En la primera funcion ira el codigo
        que contendra la funcion responsable
        de la interfaz del juego.
        """

        import random
        import pip

        """
        ademas estas tambien usaran librerias para
        mejorar la interactividad del juego.
        """

        agua = 'O'
        nombreJugador = "PJ"
        contadorPJ = 2
        contadorPC = 2
        tablero1 = [[agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ]]

        tablero2 = [[agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ]]

        tableroc = [[agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ],
                    [agua, agua, agua, agua, agua, agua,
                    agua, agua, agua, agua, ]]
        v = True
        while v is True:

            """
            El primer ciclo contiene la interfaz que muestra el menu
            y las opciones de inicio del juego.
            """

            print("-----Aguacate-----")
            print("---Batalla Naval----")
            print("-----Main Menu-----")
            print("1. Introducir nombre del jugador.")
            print("2. Iniciar juego.")
            print("3. Cerrar programa.")
            seleccion = int(input())

            """
            en esta condicional se puede expresar que si el valor
            ingresado en el input "nombrejugador" esta vacio,
            este le asignara un nombre por defecto
            """

            if seleccion == 1:
                nombreJugador = input("Ingrese un nombre: ")
                if not nombreJugador:
                    nombreJugador = "PJ"
                    print("====", "Hola", nombreJugador, "====")
                else:
                    print("====", "Hola", nombreJugador, "====")
            elif seleccion == 3:
                print("Fin del programa.")
            elif seleccion == 2:

                """
                Estos ciclos contienen las matrices conteniendo las listas
                y imprimiendolas en forma de tablero en la pantalla
                junto a sus contadores
                de barcos.
                """

                print("Iniciando juego")
                print(" =====", nombreJugador, "======")
                for j in range(len(tablero2)):
                    for k in range(len(tablero2)):
                        print(tablero2[j][k], end=" ")
                    print()
                print("   ============= ")
                print("  ===== " "PC" " ======")
                for h in range(len(tableroc)):
                    for x in range(len(tableroc)):
                        print(tableroc[h][x], end=" ")
                    print()
                v = False
            else:
                print("ERROR: Selección Inválida")

        """
        En esta funcion se van a establecer la posicion
        de los barcos tanto enemigos como
        los del jugador
        """

        def showBoard(pjBoard, pcBoard):
            print("Por favor ubica tus barcos")
            z = True
            while z is True:
                for n in range(pjBoard):
                    fila = int(input("fila: "))
                    columna = int(input("columna: "))
                    if tablero2[fila][columna] == "O":
                        tablero2[fila][columna] = "B"
                        z = False
                    elif [fila][columna] == [fila][columna]:
                        print("Seleccione otra ubicación")
                        z = True

            """
            esta seccion es la que maneja el codigo con la libreria
            random para que este funcione como si fuera un jugador
            """

            for y in range(pcBoard):
                columna = random.randint(0, 9)
                fila = random.randint(0, 9)
                tablero1[fila][columna] = "B"
            print("numero de barcos: ", contadorPJ)
            print(" =====", nombreJugador, "======")
            for j in range(len(tablero2)):
                for k in range(len(tablero2)):
                    print(tablero2[j][k], end=" ")
                print()
            print("numero de barcos: ", contadorPC)
            print("  ===== " "PC" " ======")
            for h in range(len(tableroc)):
                for x in range(len(tableroc)):
                    print(tableroc[h][x], end=" ")
                print()

            """
            en esta funcion se van a manejar lo que vienen siendo
            los disparos de cada jugador incluyendo la del codigo
            """

            def disparo(pjDisparo, pcDisparo):
                contadorPJ = 2
                contadorPC = 2
                from colorama import Fore, init
                init()

                """
                la funcion comienza con un while para asegurar el limitante
                que vienen siendo los contadores
                """

                j = True
                while j is True:

                    """
                    esta seccion es la que se encarga del disparo del jugador
                    con sus condicionales
                    """

                    print(Fore.GREEN+"seleccione donde va a disparar: ")
                    init(autoreset=True)
                    filaD = int(input("fila:"))
                    columnaD = int(input("columna: "))
                    if tablero1[filaD][columnaD] == "B":
                        contadorPC = contadorPC - 1
                        print(Fore.GREEN + "impacto!!")
                        init(autoreset=True)
                        tablero1[filaD][columnaD] = (Fore.GREEN + "D")
                        init(autoreset=True)
                    elif tablero1[filaD][columnaD] == "O":
                        print("Disparo ", Fore.BLUE + "fallado " ":(")
                        init(autoreset=True)
                        tablero1[filaD][columnaD] = (Fore.BLUE + "X")
                        init(autoreset=True)
                    else:
                        tablero1[filaD][columnaD] != "O" or "B"
                        print("Disparo Invalidado")

                        """
                        esta otre seccion es la que se encarga del disparo
                        que realizara el PC
                        """

                    print(Fore.RED + "Turno del enemigo")
                    init(autoreset=True)
                    filaPCd = random.randint(0, 9)
                    columnaPCd = random.randint(0, 9)
                    if tablero2[filaPCd][columnaPCd] == "B":
                        contadorPJ = contadorPJ - 1
                        print("impacto enemigo")
                        tablero2[filaD][columnaD] = (Fore.RED + "D")
                        init(autoreset=True)
                    elif tablero2[filaPCd][columnaPCd] == "O":
                        print("Disparo Enemigo ", Fore.BLUE + "Fallado")
                        init(autoreset=True)
                        tablero2[filaPCd][columnaPCd] = (Fore.RED + "X")
                        init(autoreset=True)
                    print("numero de barcos: ", contadorPJ)
                    print(" =====", nombreJugador, "======")
                    for j in range(len(tablero2)):
                        for k in range(len(tablero2)):
                            print(tablero2[j][k], end=" ")
                        print()
                    print("   ============= ")
                    print("numero de barcos: ", contadorPC)
                    print("  ===== " "PC" " ======")
                    for h in range(len(tableroc)):
                        for x in range(len(tableroc)):
                            print(tableroc[h][x], end=" ")
                        print()

                        """
                        todo el ciclo parara cuando uno de los contadores
                        llegue a 0
                        """

                    if contadorPC == 0 or contadorPJ == 0:
                        j = False
                        print("<<Juego Terminado>>")
                    else:
                        j = True

                        """
                        esta seccion determinara el ganador
                        """

                if contadorPC == 0:
                    print("   El ganador es: ", nombreJugador)
                else:
                    print("El ganador es: PC >:)")
            disparo(2, 2)

            """
            al haber determinado un ganador el codigo sera empezado
            de nuevo al undir enter
            """

            print(">>>Presione Enter para volver al menú inicial<<<")
            input()
            u = True
        showBoard(2, 2)

    mainMenu()
