from numpy import random

# ----------------------------------- RETO #38 -------------------------------------------------
# Enunciado: Crea un programa se encargue de transformar un número binario a decimal sin utilizar funciones 
# propias del lenguaje que lo hagan directamente.

def Reto_38():
    num = 0
    exp = 0
    binary = input("Introduce el número binario sin espacios. \n")
    for i in range(len(binary) - 1, -1, -1):
        if int(binary[i]) == 1:
            num += 2**exp
        exp += 1
    print("El numero decimal es: ", num)

# ----------------------------------- RETO #39 -------------------------------------------------
# Enunciado: Implementa uno de los algoritmos de ordenación más famosos: el "Quick Sort", creado por C.A.R. Hoare.

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low,high):
        if array[j] <= pivot:
            i += 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array, low, high)
        quicksort(array, low, pivot - 1)
        quicksort(array, pivot + 1, high)

def Reto_39():
    sizeList = int(input("Introduce la cantidad total de numeros a ordenar.\n"))
    nums = random.randint(100, size=(sizeList))
    print("Lista de numeros desordenados: \n", nums)
    quicksort(nums, 0, len(nums) - 1)
    print("Lista de numeros ordenados en orden ascendente: \n", nums)

# ----------------------------------- RETO #40 -------------------------------------------------
# Enunciado: Crea una función que sea capaz de dibujar el "Triángulo de Pascal" indicándole únicamente el tamaño del lado.

def Reto_40():
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
