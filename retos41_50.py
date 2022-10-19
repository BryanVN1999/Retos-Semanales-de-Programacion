import Anexo as a

# ----------------------------------- RETO #41 -------------------------------------------------
# Enunciado: Crea una función que calcule el valor del parámetro perdido correspondiente a la ley de Ohm.
# - Enviaremos a la función 2 de los 3 parámetros (V, R, I), y retornará el valor del tercero (redondeado a 2 decimales).
# - Si los parámetros son incorrectos o insuficientes, la función retornará la cadena de texto "Invalid values".

def Reto_41():
    print("Introduzca tres valores numéricos separados por comas, excepto el valor a calcular, en ese caso deje un espacio.")
    print("Por ejemplo: 41, ,42.3 (V,R,I)")
    try:
        values = input().split(",")
        V = values[0]
        R = values[1]
        I = values[2]
        if V == " ":
            print("V = ", "{:.2f}".format(float(R) * float(I)), "V")
        elif R == " ":
            print("R = ", "{:.2f}".format(float(V) / float(I)), "\u03A9")
        elif I == " ":
            print("I = ", "{:.2f}".format(float(V) / float(R)), "A")
        else:
            print("Valores invalidos")
    except TypeError:
        print("Valores invalidos")
    except IndexError:
        print("Valores invalidos")
    except ValueError:
        print("Valores invalidos")
        
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