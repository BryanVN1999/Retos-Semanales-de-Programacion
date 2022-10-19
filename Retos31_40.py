# ----------------------------------- RETO #40 -------------------------------------------------
# Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole únicamente el tamaño del lado.

def Reto_40():
    # NUMERO DE ESPACIOS A DEJAR POR FILA: Nº FILA - 1 (' ' * nº filas - 1)
    array = [1]
    try:
        nFilas = int(input("Introduce el número de lados del Triangulo de Pascal\n"))
        for x in range(nFilas - 1,-1,-1):
            print(' ' * x, end="")
            arrayAux = [1]
            for y in range(len(array)):
                if y > 0:
                    arrayAux.append(array[y] + array[y-1])
            if x < nFilas - 1:
                arrayAux.append(1)
            array = arrayAux
            for y in array:
                print(y, end=" ")
            print("")
    except ValueError:
        print("ERROR: Numero de lados invalido") 
