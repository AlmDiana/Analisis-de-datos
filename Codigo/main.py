print("<<  NUMERO DE OCURRENCIAS DE PALABRAS DE UN TEXTO  >>")
# Variable
opc=0
# Función para Leer Archivo txt:
def contarOcurrencias(i):
    if i == 1:
        try:
            with open("Julio Cortazar - Continuidad de los parques.txt") as obj:
                contenido = obj.read()
                r= str(input("\n ¿Desea ver el contenido del libro? (s/n) : "))
                if (r =='s'):
                    print("\n-------------> INICIO DEL LIBRO\n")
                    print(contenido)
                    print("\n-------------> FIN DEL LIBRO")
        except FileNotFoundError:
            mensaje = ("No se puede abrir el archivo")
            print(mensaje)
        else:
            palabras = contenido.split()
            numPalabras = len(palabras)
            print("\nEl archivo contiene "+ str(numPalabras)+ " palabras")
            print("\n<<  OCURRENCIAS DE CADA PALABRA  >> \n")
            ocurrencia = [palabras.count(p) for p in palabras]
            print(str(list(zip(palabras, ocurrencia))))
    if i == 2:
        try:
            with open("Edgar Allan - El barril amontillado.txt") as obj:
                contenido = obj.read()
                r = str(input("\n ¿Desea ver el contenido del libro? (s/n) : "))
                if (r == 's'):
                    print("\n-------------> INICIO DEL LIBRO\n")
                    print(contenido)
                    print("\n-------------> FIN DEL LIBRO")
        except FileNotFoundError:
            mensaje = ("No se puede abrir el archivo")
            print(mensaje)
        else:
            palabras = contenido.split()
            numPalabras = len(palabras)
            print("\nEl archivo contiene " + str(numPalabras) + " palabras")
            print("\n<<  OCURRENCIAS DE CADA PALABRA  >> \n")
            ocurrencia = [palabras.count(p) for p in palabras]
            print(str(list(zip(palabras, ocurrencia))))
    if i == 3:
        try:
            with open("Oscar Wilde - El principe feliz.txt") as obj:
                contenido = obj.read()
                r = str(input("\n ¿Desea ver el contenido del libro? (s/n) : "))
                if (r == 's'):
                    print("\n-------------> INICIO DEL LIBRO\n")
                    print(contenido)
                    print("\n-------------> FIN DEL LIBRO")
        except FileNotFoundError:
            mensaje = ("No se puede abrir el archivo")
            print(mensaje)
        else:
            palabras = contenido.split()
            numPalabras = len(palabras)
            print("\nEl archivo contiene " + str(numPalabras) + " palabras")
            print("\n<<  OCURRENCIAS DE CADA PALABRA  >> \n")
            ocurrencia = [palabras.count(p) for p in palabras]
            print(str(list(zip(palabras, ocurrencia))))

# Menu
while opc < 1 or opc > 3:
    print("\nLIBROS DISPONIBLES")
    print("1. Julio Cortazar - Continuidad de los parques")
    print("2. Edgar Allan - El barril amontillado")
    print("3. Oscar Wilde - El principe feliz")
    opc = int(input("Opción: "))
    contarOcurrencias(opc)