import random

def seleccionar_palabra(dificultad):
    if dificultad == "facil":
        palabras = ["python", "programacion", "codigo", "variable"]
    elif dificultad == "intermedio":
        palabras = ["algoritmo", "diccionario", "bucle", "funcion"]
    elif dificultad == "dificil":
        palabras = ["machinelearning", "interfazgrafica", "recursividad", "optimizacion"]
    else:
        print("Dificultad no válida. Elige entre fácil, intermedio o difícil.")
        return None

    return random.choice(palabras)

def jugar_adivinanza():
    print("Bienvenido al juego de adivinar la palabra.")
    dificultad = input("Elige la dificultad (fácil, intermedio, difícil): ").lower()

    palabra_secreta = seleccionar_palabra(dificultad)

    if palabra_secreta is not None:
        intentos = 3 if dificultad == "facil" else 5 if dificultad == "intermedio" else 7
        letras_adivinadas = []
        intento_actual = 0

        while intento_actual < intentos:
            adivinanza_actual = "".join(letra if letra in letras_adivinadas else "_" for letra in palabra_secreta)
            print(f"Adivinanza actual: {adivinanza_actual}")

            intento_usuario = input("Introduce una letra: ").lower()

            if len(intento_usuario) == 1 and intento_usuario.isalpha():
                if intento_usuario in letras_adivinadas:
                    print("Ya has intentado esa letra. ¡Intenta con otra!")
                elif intento_usuario in palabra_secreta:
                    print("¡Correcto! Has adivinado una letra.")
                    letras_adivinadas.append(intento_usuario)
                else:
                    print("Incorrecto. Inténtalo de nuevo.")
                    intento_actual += 1
            else:
                print("Entrada no válida. Introduce una sola letra.")

            if set(letras_adivinadas) == set(palabra_secreta):
                print("¡Felicidades! Has adivinado la palabra.")
                break

        if intento_actual == intentos:
            print(f"Agotaste tus intentos. La palabra era: {palabra_secreta}")

if __name__ == "__main__":
    jugar_adivinanza()
