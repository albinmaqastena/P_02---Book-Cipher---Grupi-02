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


def enkripto(mesazh, libri_path):
    content = lexo_dhe_pastro_librin(libri_path)
    if not content:
        return "Gabim gjatë leximit të librit."

    fjale_ne_mesazh = pastro_tekstin(mesazh).split()
    pozitat = []

    for fjala in fjale_ne_mesazh:
        try:
            index = content.index(fjala) + 1
            pozitat.append(str(index))
        except ValueError:
            pozitat.append('?')

    return ' '.join(pozitat)










