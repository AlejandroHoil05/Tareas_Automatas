#Jose Alejandro Castillo Hoil

"""Maquina de estado Finito Determinista"""

class MaquinaAFD:

    def __init__(self):
        """Inicializacion del MSFD"""
        self.CONJUNTO_ESTADOS_AUTOMATA = self.definir_estados() #Q1, Q2 ,Q3
        self.ALFABETO_AUTOMATA = self.definir_alfabeto() #A B C
        self.FUNCIONES_TRANSICION_AUTOMATA = self.definir_funcion_Transicion() # {Q1:{Q1:A,Q1:B,Q1:C:} , Q2:{Q2:A,Q2:B,Q2:C:}}
        self.ESTADO_INICIAL_AUTOMATA, self.ESTADO_ACEPTACION_AUTOMATA = self.set_start_accept()
        self.ESTADO_ACTUAL_AUTOMATA = None


    def set_start_accept(self):
        """Pedir al usuario el Estado Inicial y el Estado de Aceptacion,
        y verificar si es un estado valido del MSFD(el estado pertenece a Q)"""
        while (True):
            estado_inicial_ingresado = input("Ingresa el Estado Inicial: ")
            estado_aceptacion_ingresado = input("Ingresa el Estado de Aceptación: ").split()
            # Making sure that start and accept are both in Q
            if (estado_inicial_ingresado in self.CONJUNTO_ESTADOS_AUTOMATA) and (set(estado_aceptacion_ingresado).issubset(set(self.CONJUNTO_ESTADOS_AUTOMATA))):
                return estado_inicial_ingresado, estado_aceptacion_ingresado
            else:
                print(
                    "Por favor, ingresa el ESTADO_INICIAL y los ESTADOS_DE_ACEPTACIÓN que están en el Conjunto de estados: {}. \n Los estados de aceptación deben ser un subconjunto válido del conjunto de estados \n".format(
                        self.CONJUNTO_ESTADOS_AUTOMATA))

    def definir_estados(self):
        """Pedir al usuario el conjunto de estado (Q)"""
        conjunto_estados_ingresados = input("Ingresa el conjunto de estados separado por espacios: ").split()
        print("Conjunto de estados : {}".format(conjunto_estados_ingresados))
        return conjunto_estados_ingresados

    def definir_alfabeto(self):
        """Pedir al usuario el alfabeto del MSFD"""
        alfabeto_ingresado = input("Ingresa el alfabeto separado por espacios: ").split()
        print("Alfabeto : {}".format(alfabeto_ingresado))
        return alfabeto_ingresado

    def definir_funcion_Transicion(self):
        """Crear las funciones de trabsicion Q X SIGMA -> Q"""
        # Inicializamos el diccionario principal trans_dict
        funciones_transicion = {}

        # Iteramos sobre cada estado en self.Q
        for estado in self.CONJUNTO_ESTADOS_AUTOMATA: # {Q1,Q2,Q3}
            # Creamos un diccionario vacío para el estado actual
            diccionario_simbolos = {}

            # Iteramos sobre cada símbolo en self.SIGMA
            for simbolo in self.ALFABETO_AUTOMATA:
                # Para cada símbolo, asignamos el valor "NM" al símbolo en el diccionario
                diccionario_simbolos[simbolo] = "NM"

            # Asignamos el diccionario de símbolos (simbolos_dict) al estado correspondiente en trans_dict
            funciones_transicion[estado] = diccionario_simbolos

        for key, dic_val in funciones_transicion.items():
            print("Ingresa los estados de transicion {}. Si no esta definido, usa NM".format(self.CONJUNTO_ESTADOS_AUTOMATA))
            for simbolo, movimiento in dic_val.items():
                funciones_transicion[key][simbolo] = input("Estado actual: {}\tSimbolo de entrada:{}\tEstado siguiente:".format(key, simbolo))

        print("Función de transición EstadoActual × SimboloEntrada → EstadoSiguiente")
        print("ESTADO ACTUAL \tALFABETO DE ENTRADA\tESTADO SIGUIENTE")
        for key, dic_val in funciones_transicion.items():
            for simbolo, movimiento in dic_val.items():
                print("\t{}\t\t:{}\t{}".format(key, simbolo, movimiento))

        return funciones_transicion

    def val_state_alphabet(self, simbolo):
        """Recibe el estado actual y pasa al siguiente estado basado en el símbolo de entrada"""
        self.ESTADO_ACTUAL_AUTOMATA = self.FUNCIONES_TRANSICION_AUTOMATA[self.ESTADO_ACTUAL_AUTOMATA][simbolo]
        #Aqui se busca  con la llave que es estado actual (Q1) y el valor que es el simbolo(A)
        # en el diccionario de las funciones de transicion -> {q1:{A:Q1,B:Q2},q2:{A:Q2,B:Q1} y se guardara
        #el valor en estado actual que sera  (q1)
    def val_final_state(self):
        """Verifica si el estado actual es uno de los estados de aceptación"""
        if self.ESTADO_ACTUAL_AUTOMATA in self.ESTADO_ACEPTACION_AUTOMATA:
            return True
        else:
            return False

    def run_automata(self, cadena):
        """Validate the string (cadena) input"""
        self.ESTADO_ACTUAL_AUTOMATA = self.ESTADO_INICIAL_AUTOMATA
        for simbolo in cadena: #se itera la cadena
            val_sim = self.val_state_alphabet(simbolo) # se envia al metodo el simbolo A y guardo el resultado en val_sim
            # check if new state is not NM
            if (val_sim == 'NM'): # si val sim es NM cortamons el for y returnamos falso y por ende no se acepta la cadena
                return False
        return self.val_final_state() # al final se activa este metodo

if __name__ == "__main__":
    def leerArchivo():
        # abro el txt y lo guardo en archivo
        archivo = open("automata.txt")
        # utilizo el metodo readlines para guardar en una lista el contenido de archivo y guardarlo en lista
        lista_sin_formato = archivo.readlines()
        # print(f"esta es la lista sin formato: {lista_sin_formato}")
        archivo.close()
        # declaro variables para guardar las quintuplas del automata
        estado_inicial = ""
        estado_final = ""
        funciones_transicion = {}

        # recorro la lista buscando los estados iniciales y finales para guardarlos en sus variables
        # quito el salto de linea \n que se incluyo automaticamente con read lines al convertirlo en lista y los guardo en otra lista
        # Tambien remplazo el simbolo * y + por "" para eliminarlos
        lista = []
        for linea in lista_sin_formato:
            if "+" in linea and "*" not in linea[1]:
                estado_inicial = linea[1:linea.find(
                    ",")]  # aqui le paso el valor de que hay en la posicion 1 hasta donde se encuentre una coma
            elif "+*" in linea:
                estado_inicial = linea[2:linea.find(
                    ",")]  # aqui le paso el valor de que hay en la posicion 1 hasta donde se encuentre una coma
                estado_final = linea[2:linea.find(",")]
            elif "*+" in linea:
                estado_inicial = linea[2:linea.find(
                    ",")]  # aqui le paso el valor de que hay en la posicion 1 hasta donde se encuentre una coma
                estado_final = linea[2:linea.find(",")]
            elif "*" in linea and "+" not in linea[1]:
                estado_final = linea[1:linea.find(
                    ",")]  # aqui le paso el valor de que hay en la posicion 1 hasta donde se encuentre una coma
            lista.append(linea.strip().replace("+", "").replace("*", "").split(","))
        # como el alfabeto siempre estara en la primera linea, le paso el primer elemento de la nueva lista a alfabeto
        alfabeto = lista[0]

        # creamos la variable conjunto de estados como set asi evitaremos que se duplican valores
        conjunto_de_estados = set()
        # recorremos todos las cadenas de la lista desde la posicion 1 hasta el final
        # recorremos cada caracter de cada cadena y lo agregamos al set de conjunto de datos
        for cadena in lista[1:]:
            for caracter in cadena:
                conjunto_de_estados.add(caracter)

        # transformamos a lista el conjunto de estados , paera tener el metodo de ordenar  y se lo aplicamos
        conjunto_de_estados = list(conjunto_de_estados)
        conjunto_de_estados.sort()  # ordenamos el conjunto de estados

        # Llenamos el diccionario donde estaran las funciones de transicion
        for cadena in lista[1:]:  # recorremos las cadenas de la lista ecepto la primera por que ahi esta el alfabeto
            llave = cadena[
                0]  # aki le estoy pasando el valor de la cadena que esta en la posicion 0 a la llave del diccionario
            funciones_transicion[
                llave] = {}  # aki estoy agregando un nuevo diccionario con su llave al diccionario funciones_transicion
            # Recorremos el alfabeto y los elementos de cadena[1:] al mismo tiempo usando zip
            for letra, estado in zip(alfabeto, cadena[1:]):
                # Asignamos a la llave actual una letra del alfabeto y su correspondiente transición
                funciones_transicion[llave][letra] = estado

        # print(f"esta es la lista con formato: {lista}")
        print("estado inicial =" + estado_inicial)
        print("estado final =" + estado_final)
        print(f"alfabeto ={alfabeto}")
        print(f"conjunto de estados = {conjunto_de_estados}")
        print(f"funciones de transicion{funciones_transicion}")
        print(type(estado_final))

        def verificar_cadena(cadena):  # aki de ejmplo cadena es 111
            estado_actual = estado_inicial  # aki le paso el valor de estado incial a la variable estado actual q0
            print(f"Estado inicial: {estado_actual}")

            for simbolo in cadena:  # aki recorro cad simbolo que hay en la cadena que pase de argumento
                if simbolo in funciones_transicion[estado_actual]:  # si el simbolo 1  esta en {q0{0:q0,1:q1}
                    # Obtener el siguiente estado según la función de transición                                                                 !
                    estado_actual = funciones_transicion[estado_actual][
                        simbolo]  # aki a estado actual le paso q1 que es el valor de {q0:{0:q0,1:Q1}}
                    print(f"Transición: {estado_actual} con símbolo: {simbolo}")
                else:
                    print(
                        f"Símbolo {simbolo} no reconocido en estado {estado_actual}. Cadena rechazada.")  # si el simbolo no existe en el diccionario se rechaza
                    return False  # Si el símbolo no es reconocido, la cadena es rechazada

            # Verificar si el estado final es el estado aceptado
            if estado_actual == estado_final:
                print("Cadena aceptada.")
                return True
            else:
                print("Cadena rechazada.")
                return False

        while True:
            print("\n=== MENÚ ===")
            print("1. Ingresar cadena a validar manualmente")
            print("2. Ingresar cadena a validar desde archivo")
            print("3. Regresar al menú anterior")
            print("4. Terminar")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                # Validar cadena manualmente
                cadena = list(input("Dame la cadena a validar: "))
                verificar_cadena(cadena)
            elif opcion == "2":
                # Leer cadena desde archivo y validarla
                archivo = open("cadena.txt")
                cadena = archivo.readline()
                verificar_cadena(cadena)

            elif opcion == "3":
                # Regresar a la otra clase MaquinaAFD
                break
            elif opcion == "4":
                # Terminar el programa
                exit()
            else:
                print("Opción no válida, intenta de nuevo.")


    def menu():
        """Despliega el menú de opciones para la máquina AFD"""
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Ingresar el autómata manualmente")
        print("2. Ingresar el autómata desde archivo")
        print("3. Terminar")
        return input("Elige una opción: ")


    def submenu(nuevo_automata):
        """Despliega el submenú una vez que el autómata ha sido ingresado"""
        while True:
            print("\n=== SUBMENÚ ===")
            print("1. Ingresar cadena a validar manualmente")
            print("2. Ingresar cadena a validar desde archivo")
            print("3. Regresar al menú anterior")
            print("4. Terminar")
            opcion = input("Elige una opción: ")

            if opcion == "1":
                # Validar cadena manualmente
                cadena = list(input("Dame la cadena a validar: "))
                print("ACCEPTED" if nuevo_automata.run_automata(cadena) else "REJECTED")
            elif opcion == "2":
                # Leer cadena desde archivo y validarla
                archivo = open("cadena.txt")
                cadena= archivo.readline()
                print("ACCEPTED" if nuevo_automata.run_automata(cadena) else "REJECTED")

            elif opcion == "3":
                # Regresar al menú principal
                break
            elif opcion == "4":
                # Terminar el programa
                exit()
            else:
                print("Opción no válida, intenta de nuevo.")


    while True:
        opcion = menu()

        if opcion == "1":
            # Ingresar el autómata manualmente
            nuevo_automata = MaquinaAFD()  #creo el objeto Maquina para activar todos sus metodos
            submenu(nuevo_automata) # llamo el metodo submenu y le paso de argumento al automata creado
        elif opcion == "2":
            #Opción del autómata desde archivo (no implementada aún)
            print("estas son las quintuplas del archivo: ")
            leerArchivo()

        elif opcion == "3":
            # Terminar el programa
            print("Terminando el programa.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")


    #maquinax= MaquinaAFD()
    #cadena=list(input("Dame la cadena a validar: "))
    #print("ACCEPTED" if maquinax.run_automata(cadena) else "REJECTED")
    #********************************************************************
    # MENU
    #Ingresa una opcion
    #Ingresar el Automata Manualmente
    #Ingresar el automata desde Archivo
    #Terminar
    #Despues de ingresar el automata las opciones seran las siguientes
    #Ingresar cadena a validar manualmente
    #ingresar cadena a validar desde archivo
    #Regresar al menu anterior
    #Terminar
    #**********************************************************************



