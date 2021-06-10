# Variables
a = []
b = []
c = []
filas = 0
columnas = 0
filas2 = 0
columnas2 = 0
incorrectof = True
incorrectoc = True
incorrectof2 = True
incorrectoc2 = True


print("\n<<   MULTIPLICACIÓN DE MATRICES   >>")
print("DIMENSIONES DE LAS MATRICES")

print("MATRIZ 1:")
while incorrectof:
    filas=int(input("Número de Filas: "))
    if filas <= 0:
        incorrectof = True
    else:
        incorrectof = False
while incorrectoc:
    columnas = int(input("Número de Columnas: "))
    if columnas <= 0:
        incorrectoc = True
    else:
        incorrectoc = False

# Pedir al usuario que llene la matriz:
for i in range(filas):
    a.append([])
    for j in range(columnas):
        valor = int(input("Fila {} , Columna {}  : ".format(i+1, j+1)))
        a[i].append(valor)

print("\nMATRIZ 2:")
while incorrectof2:
    filas2=int(input("Número de Filas: "))
    if filas2 <= 0:
        incorrectof2 = True
    else:
        incorrectof2= False
while incorrectoc2:
    columnas2 = int(input("Número de Columnas: "))
    if columnas2 <= 0:
        incorrectoc2 = True
    else:
        incorrectoc2 = False
while incorrectof2:
    filas2=int(input("Filas: "))
    if filas2 <= 0:
        incorrectof2 = True
    else:
        incorrectof = False
while incorrectoc2:
    columnas2 = int(input("Columnas: "))
    if columnas2 <= 0:
        incorrectoc2 = True
    else:
        incorrectoc2 = False

# Pedir al usuario que llene la matriz:
for i in range(filas2):
    b.append([])
    for j in range(columnas2):
        valor = int(input("Fila {} , Columna {}  : ".format(i+1, j+1)))
        b[i].append(valor)

# Imprimir matriz 1
print()
print("MATRIZ 1")
for filas in a:
    print("[", end="\t")
    for elemento in filas:
        print("{}".format(elemento), end="\t")
    print("]")
print()

# Imprimir matriz 2
print("MATRIZ 2")
for filas2 in b:
    print("[", end="\t")
    for elemento in filas2:
        print("{}".format(elemento), end="\t")
    print("]")

def multiplicar_matrices(m1,m2):
    # vVerificamos matrices
    if len(m1[0]) == len(m2):
        m3 = []
        for i in range(len(m1)):
            m3.append([])
            for j in range(len(m2[0])):
                m3[i].append(0)

        #Multiplicación
        for i in range(len(m1)):
            for j in range (len(m2[0])):
                for k in range(len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        return m3
    else:
        return None


d = multiplicar_matrices(a,b)
if d == None:
    print("Las matrices dadas, no se pueden multiplicar")
else:
    print("\nMATRIZ RESULTANTE:")
    for fila in d:
        print("[", end="\t")
        for elemento in fila:
            print(elemento, end="\t")
        print("]")





