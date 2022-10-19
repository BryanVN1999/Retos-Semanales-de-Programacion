import Anexo as a

# ----------------------------------- RETO #41 -------------------------------------------------
# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
# - En caso contrario retornará un error.

def Reto_41():
    try:
        inputUser = input("Introduzca la temperatura. Por ejemplo: 23ºC\n")
        value = float(inputUser.split("º")[0])
        unit = inputUser.split("º")[1]
        if unit == "C":
            print("{:.2f}".format((value * 9/5) + 32) + "º" + "F")
        elif unit == "F":
            print("{:.2f}".format((value - 32) * 5/9) + "º" + "C")
        else:
            print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except TypeError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except IndexError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except ValueError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")

# ----------------------------------- RETO #42 -------------------------------------------------
# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
# - En caso contrario retornará un error.

def Reto_42():
    try:
        inputUser = input("Introduzca la temperatura. Por ejemplo: 23ºC\n")
        value = float(inputUser.split("º")[0])
        unit = inputUser.split("º")[1]
        if unit == "C":
            print("{:.2f}".format((value * 9/5) + 32) + "º" + "F")
        elif unit == "F":
            print("{:.2f}".format((value - 32) * 5/9) + "º" + "C")
        else:
            print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except TypeError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except IndexError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
    except ValueError:
        print("La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")