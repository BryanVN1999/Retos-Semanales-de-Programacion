from re import A
import Retos31_40 as rs3
import Retos41_50 as rs4

def SelectChallenge():
    try:
        option = int(input())
        print(f'----------------- RETO {option} ---------------------')
        if option == 40:
            rs3.Reto_40()
        elif option == 41:
            rs4.Reto_41()
        elif option == 42:
            rs4.Reto_42()
        else:
            print("Opción no disponible")
    except ValueError:
        print("Opción no disponible")

SelectChallenge()