# Función que devuelve un string: "es" si ha elegido español o "en" si ha elegido ingles.
def ChooseLanguage():
    language = None
    
    print("Selecciona el idioma/Select the language: \n- Write \"en\" for English. \n- Escribe \"es\" para Español.")
    language = input()

    while(language != "es" and language != "en"):
        language = input("- Valor erróneo, vuelva a introducir el valor correctamente \n- Error value, write the value again.\n")

    return language