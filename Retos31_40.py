from numpy import random
from datetime import datetime as dt

# ----------------------------------- RETO #36 -------------------------------------------------
# Enunciado: Enunciado: ¡La Tierra Media está en guerra! En ella lucharán razas leales
# a Sauron contra otras bondadosas que no quieren que el mal reine sobre sus tierras.
# Cada raza tiene asociado un "valor" entre 1 y 5:
# - Razas bondadosas: Pelosos (1), Sureños buenos (2), Enanos (3), Númenóreanos (4), Elfos (5)
# - Razas malvadas: Sureños malos (2), Orcos (2), Goblins (2), Huargos (3), Trolls (5)
# Crea un programa que calcule el resultado de la batalla entre los 2 tipos de ejércitos:
# - El resultado puede ser que gane el bien, el mal, o exista un empate.
# Dependiendo de la suma del valor del ejército y el número de integrantes.
# - Cada ejército puede estar compuesto por un número de integrantes variable de cada raza.
# - Tienes total libertad para modelar los datos del ejercicio.

# ----------------------------------- RETO #37 -------------------------------------------------
# Enunciado: Crea un programa que calcule cuántos años y días hay entre 2 juegos de Zelda
# que tú selecciones.
# - Debes buscar cada uno de los títulos y su día de lanzamiento.

def SelectZelda(a):
    if a == 1:
        return "23/05/2023"
    elif a == 2:
        return "16/07/2021"
    elif a == 3:
        return "20/09/2019"
    elif a == 4:
        return "13/06/2019"
    elif a == 5:
        return "03/03/2017"
    elif a == 6:
        return "01/09/2016"
    elif a == 7:
        return "04/03/2016"
    elif a == 8:
        return "23/10/2015"
    elif a == 9:
        return "13/02/2015"
    elif a == 10:
        return "22/11/2013"
    elif a == 11:
        return "04/10/2013"
    elif a == 12:
        return "30/05/2013"
    elif a == 13:
        return "30/05/2013"
    elif a == 14:
        return "18/11/2011"
    elif a == 15:
        return "28/09/2011"
    elif a == 16:
        return "17/06/2011"
    elif a == 17:
        return "07/06/2011"
    elif a == 18:
        return "11/12/2009"
    elif a == 19:
        return "03/04/2009"
    elif a == 20:
        return "19/10/2007"
    elif a == 21:
        return "09/02/2007"
    elif a == 22:
        return "08/12/2006"
    elif a == 23:
        return "08/12/2006"
    elif a == 24:
        return "07/01/2005"
    elif a == 25:
        return "31/12/2004"
    elif a == 26:
        return "12/11/2004"
    elif a == 27:
        return "03/05/2003"
    elif a == 28:
        return "03/05/2003"
    elif a == 29:
        return "24/03/2003"
    elif a == 30:
        return "17/11/2000"
    elif a == 31:
        return "11/12/1998"
    else:
        print("Opción no disponible")
        exit()
    
def Reto_37():    
    print("Elige dos juegos de Zelda de la siguiente lista, utilizando la siguiente nomenclatura. Ej: 5 y 8.")
    print("-------------------------------------------------------------------------------------------------")
    print("1. The Legend of Zelda: Tears of the Kingdom")
    print("2. The Legend of Zelda Skyward Sword HD")
    print("3. The Legend of Zelda: Link's Awakening")
    print("4. Cadence of Hyrule - Crypt of the NecroDancer Featuring The Legend of Zelda")
    print("5. The Legend of Zelda: Breath of the Wild")
    print("6. The Legend of Zelda: Skyward Sword Wii")
    print("7. The Legend of Zelda: Twilight Princess HD")
    print("8. The Legend of Zelda: Tri Force Heroes")
    print("9. The Legend of Zelda: Majora's Mask 3D")
    print("10. The Legend of Zelda: A Link Between Worlds")
    print("11. The Legend of Zelda: The Wind Waker HD")
    print("12. The Legend of Zelda: Oracle of Ages")
    print("13. The Legend of Zelda: Oracle of Seasons")
    print("14. The Legend of Zelda: Skyward Sword")
    print("15. The Legend of Zelda: Four Swords Anniversary Edition")
    print("16. The Legend of Zelda: Ocarina of Time 3D")
    print("17. The Legend of Zelda: Link's Awakening Game Boy")
    print("18. The Legend of Zelda: Spirit Tracks")
    print("19. The Legend of Zelda: Majora's Mask")
    print("20. The Legend of Zelda: Phantom Hourglass")
    print("21. Zelda II: The Adventure of Link")
    print("22. The Legend of Zelda")
    print("23. The Legend of Zelda: Twilight Princess")
    print("24. Zelda 2 Classics")
    print("25. The Legend of Zelda: Four Swords")
    print("26. The Legend of Zelda: The Minish Cap")
    print("27. The Legend of Zelda: The Wind Waker")
    print("28. The Legend of Zelda: Ocarina of Time Master Quest")
    print("29. The Legend of Zelda: A Link to the Past")
    print("30. Zelda: Majora's Mask")
    print("31. The Legend of Zelda: Ocarina of Time")
    print("-------------------------------------------------------------------------------------------------")
    selected = input().split("y")
    date1 = SelectZelda(int(selected[0]))
    date2 = SelectZelda(int(selected[1]))
    d1 = dt.strptime(date1, "%d/%m/%Y")
    d2 = dt.strptime(date2, "%d/%m/%Y")
    difference = abs(d1 - d2).days
    deltaYear = int(difference/365)
    deltaDays = int(difference%365)
    print(f'Entre estos dos juegos hay {deltaYear} año/s y {deltaDays} día/s de diferencia')

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
