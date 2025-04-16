import string 

def pastro_tekstin(tekst):
    return tekst.translate(str.maketrans('', '', string.punctuation)).lower()


def lexo_pastro_librin(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            content = file.read()
            return pastro_tekstin(content).split()
    except FileNotFoundError:
        print("Gabim: Libri nuk u gjet në këtë rrugë.")
        return[]











