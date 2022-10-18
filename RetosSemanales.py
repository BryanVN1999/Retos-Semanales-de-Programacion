import Anexo as a

# ----------------------------------- RETO #42 -------------------------------------------------
# Enunciado: Crea una función que transforme grados Celsius en Fahrenheit y viceversa.
# - Para que un dato de entrada sea correcto debe poseer un símbolo "°" y su unidad ("C" o "F").
# - En caso contrario retornará un error.

def CtoF(value):
    return (value * 9/5) + 32

def FtoC(value):
    return (value - 32) * 5/9

def CheckInputs(input, errorMessage):
    try:
        value = input.split("º")[0]
        unit = input.split("º")[1]
        if unit != "C" and unit != "F":
            print(errorMessage)
            exit()
        else:
            return [float(value), unit]
    except TypeError:
        print(errorMessage)
        exit()
    except IndexError:
        print(errorMessage)
        exit()
    except ValueError:
        print(errorMessage)
        exit()

def CheckUnit(returned):
    if returned[1] == "C":
        return [CtoF(returned[0]), "ºF"]
    elif returned[1] == "F":
        return [FtoC(returned[0]), "ºC"]

def ConversorTemperatura():

    value = None
    unit = None
    language = None
    inputUser = None

    language = a.ChooseLanguage()

    if language == "es":
        print("Se va a realizar un intercambio de unidades, de Celsius a Fahrenheit o viceversa.")
        inputUser = input("Introduzca el valor y la unidad que desea convertir (\"ºC\" o \"ºF\"). \nPor ejemplo: 35ºC\n")
        returned = CheckInputs(inputUser, "La unidad o el valor introducido son erróneos. Vuelva a intentarlo otra vez.")
        returned = CheckUnit(returned)
        print("La conversión es: ", "{:.2f}".format(returned[0]), returned[1])
    elif language == "en":
        print("The value will be swapped, from Celsius to Fahrenheit or viceversa.")
        inputUser = input("Write the value and the unit that you want to swap (\"ºC\" o \"ºF\"). \nFor example: 35ºC\n")
        returned = CheckInputs(inputUser, "The value or unit are wrong. Try again.")
        returned = CheckUnit(returned)
        print("The swapping is: ", "{:.2f}".format(returned[0]), returned[1])

    