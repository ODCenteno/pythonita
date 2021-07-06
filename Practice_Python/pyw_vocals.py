"""
Desarrolla un programa que nos permita conocer todas las vocales que existen dentro de un string.

El programa deberá cumplir con los siguiente requerimientos.

El usuario podrá ingresar, vía teclado, una palabra o frase de su interés.
El programa deberá mostrar en consola todas las vocales presentes en el string ingresado.
En caso el string ingresado no posea vocales, el programa no deberá imprimir nada.
"""

VOCALS = ["a", "i", "e", "o", "u", "á", "é", "í", "ó", "ú"]
vocals_in_phrase = []
vocal_count = {
    "a": 0,
    "e": 0,
    "i": 0,
    "o": 0,
    "u": 0,
}


def run():
    """Function that count the number of vowels in a string"""
    global vocals_in_phrase
    ux_phrase = input("Enter a word or a phrase: ").strip()

    for letter in ux_phrase:
        if letter in VOCALS[5:]:
            accent_vocal = VOCALS.index(letter)
            vocals_in_phrase.append(VOCALS[accent_vocal - 5])
        elif letter in VOCALS[:5]:
            vocals_in_phrase.append(letter)

    for vocal in vocals_in_phrase:
        vocal_count[vocal] += 1

    if vocals_in_phrase == None:
        return None
    elif vocals_in_phrase:
        vocals_in_phrase = set(vocals_in_phrase)
        print(f"Las vocales son:\n{''.join(vocal for vocal in vocals_in_phrase)}")
        print(f"Las vocales son:\na:{vocal_count['a']}\ne:{vocal_count['e']}\ni:{vocal_count['i']}\no:{vocal_count['o']}\nu:{vocal_count['u']}")


if __name__ == '__main__':
    run()
