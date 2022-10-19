from re import A
import retos41_50 as rs4

def SelectChallenge():
    try:
        option = int(input())
        print(f'----------------- RETO {option} ---------------------')
        if option == 41:
            rs4.Reto_41()
        if option == 42:
            rs4.Reto_42()
        else:
            print("Opción no disponible")
    except ValueError:
        print("Opción no disponible")

SelectChallenge()
