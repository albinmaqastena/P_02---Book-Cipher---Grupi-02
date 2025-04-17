import string 

def pastro_tekstin(tekst):
    return tekst.translate(str.maketrans('', '', string.punctuation)).lower()


def lexo_dhe_pastro_librin(path):
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

def dekripto(pozitat, libri_path):
    content = lexo_dhe_pastro_librin(libri_path)
    if not content:
        return "Gabim gjatë leximit të librit."

    fjalet = []
    for poz in pozitat.split():
        if poz.isdigit():
            index = int(poz) - 1  # -1 sepse lista është 0-based
            if 0 <= index < len(content):
                fjalet.append(content[index])
            else:
                fjalet.append('?')  # Pozitë jashtë kufijve
        else:
            fjalet.append('?')  # Pozitë jo-valide

    return ' '.join(fjalet)


if __name__ == "__main__":
    print("Zgjidhni një veprim:")
    print("1 - Enkripto mesazhin")
    print("2 - Dekripto mesazhin")
    zgjedhja = input("Zgjedhja juaj (1/2): ").strip()

    path_librit = input("Jep rrugën e librit (p.sh. book.txt): ").strip()

    if zgjedhja == '1':
        mesazhi = input("Shkruani mesazhin për enkriptim: ")
        koduar = enkripto(mesazhi, path_librit)
        print("Mesazhi i koduar :", koduar)
    elif zgjedhja == '2':
        pozitat = input("Shkruani pozitat për dekriptim (p.sh. 1 2 3): ")
        dekoduar = dekripto(pozitat, path_librit)
        print("Mesazhi i dekriptuar:", dekoduar)
    else:
        print("Zgjedhje e pavlefshme.")










