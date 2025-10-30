muñeco_ahorcado_fases = [
    """
     -----
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    """
     -----
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """
    ]

#funcion para el numero de fallos
def fallos(numero_fallos, palabra_secreta, lista_letras_usadas, contador_letras): 
    """Mensajes por si el usuario falla las letras"""
    if numero_fallos == 1:
        print("Ha fallado! Tenga cuidado, ahora el muñeco tiene una cabeza...\n", muñeco_ahorcado_fases[0])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
    elif numero_fallos == 2:
        print("Ha fallado! Tenga cuidado, ahora el muñeco tiene una tronco...\n", muñeco_ahorcado_fases[1])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
    elif numero_fallos == 3:
        print("Ha fallado! Tenga cuidado, ahora al muñeco le ha salido un brazo...\n", muñeco_ahorcado_fases[2])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
    elif numero_fallos == 4:
        print("Ha fallado! Tenga cuidado, ahora el muñeco tiene un brazo mas...\n", muñeco_ahorcado_fases[3])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
    elif numero_fallos == 5:
        print("Cuidado!! La primera pierna aparece...\n", muñeco_ahorcado_fases[4])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
    elif numero_fallos == 6:
        print("Oh noo!! La segunda pierna...\n", muñeco_ahorcado_fases[5])
        print(f"Le quedan {contador_letras-1} letras por adivinar.")
        print(f"...HA PERDIDO, ha matado a nuestro amigo, la palabra era... '{palabra_secreta}'\n")
    


def ahorcado(palabra_secreta):
    """Juego del ahorcado"""
    numero_fallos = 0
    numero_intentos = 0
    contador_letras = len(palabra_secreta)+1
    progreso = ["_"] * len(palabra_secreta)   #longitud de la palabra secreta -> _ _ _ _ _
    lista_letras_usadas = []

    letras_usadas = set()

    for _ in range(27):
        letra_usuario = input("-----------------------------------------------------\nPrueba suerte!, introduzca una letra en minúscula: ")
        print("-----------------------------------------------------")
        numero_intentos += 1
        lista_signos = ["-", ".", ",", " ", "_", "/", "*", "+", "...", ";", "<", ">", "="]
        
        if letra_usuario in lista_signos:       #si son signos y no letras
            print("Amigo eso no es una LETRA!!")
        
        if letra_usuario in letras_usadas:
            numero_fallos += 1
            lista_letras_usadas.append(letra_usuario)
            print("¡Ya había usado esa letra! Fallo extra!!\n")
            fallos(numero_fallos, palabra_secreta, lista_letras_usadas, contador_letras)
            continue
        letras_usadas.add(letra_usuario)

        if letra_usuario in palabra_secreta:    #si la letra esta en la palabra
            aciertos = 0
            for i, char in enumerate(palabra_secreta):      #para poner la letra en el sitio que va de la palabra 
                if char == letra_usuario:
                    if progreso[i] != letra_usuario:  # solo contar si aún no se había descubierto
                        progreso[i] = letra_usuario
                        aciertos += 1
                    
            contador_letras -= aciertos
            lista_letras_usadas.append(letra_usuario)
            progresando = " ".join(progreso)
            
            if contador_letras == 0:    #si la letra esta en la palabra y has llegado al numero 0 de intentos
                print(f"{progresando}\nSii esta en lo correcto!! La palabra secreta era [{palabra_secreta}]")
                break
            elif contador_letras == 1:
                input("Pulse enter para ver su respuesta completa...")
                print(f"{progresando}\nSii esta en lo correcto!! La palabra secreta era [{palabra_secreta}]")
                break
            
            #si el numero de intentos llega a la mitad de la longitud de la palabra, se le pregunta al usuario si ya adivino
            if contador_letras == len(palabra_secreta)//2:
                print(f"{progresando}\n")
                decision = input(f"Enhorabuena! Ha llegado a su acierto número {numero_intentos}, ¿ha adivinado ya la palabra? (Si/No): ")
                
                while decision not in ["Si", "No"]:     #si la decision es diferente a Si y No, imprime un mensaje como respuesta invalida
                    decision = input("Respuesta no válida. Por favor escriba 'Si' o 'No': ")
                
                if decision == "Si":
                    palabra_usuario = input("Veamos...Escriba su palabra querido usuario (si falla acabará el juego jeje): ")
                    if palabra_usuario == palabra_secreta:
                        print(f"Ha acertado, sí la palabra era [{palabra_secreta}], eres increible!!")
                        break
                    else:
                        print(f"Ha fallado, lo siento, la palabra era [{palabra_secreta}]")
                        break
                elif decision == "No":
                    if contador_letras-1 == 1:
                        print(f"Vale, sigamos jugando..., aun le quedan {contador_letras-1} intento más.")
                        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
                        continue        #salta a preguntar otra letra
                    if contador_letras-1 != 1 and contador_letras-1 > 0:
                        print(f"Vale, sigamos jugando..., aun le quedan {contador_letras-1} intentos más.")
                        print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")
                        continue        #salta a preguntar otra letra
        
            print(f"Enhorabuena! Le quedan por adivinar {contador_letras-1} letras más.\n{progresando}")
            print(f"\nHa usado estas letras, cuidado con repetirlas! -> {lista_letras_usadas}")

        else:
            numero_fallos += 1
            numero_intentos -= 1
            lista_letras_usadas.append(letra_usuario)
            fallos(numero_fallos, palabra_secreta, lista_letras_usadas, contador_letras)
            if numero_fallos == 6:
                break 

    
if __name__ == "__main__":
    ahorcado(palabra_secreta="botella")