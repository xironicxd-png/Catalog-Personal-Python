import math

def valideaza_nota(mesaj):
    """Asigură introducerea unei note valide între 1 și 10."""
    while True:
        try:
            nota = int(input(mesaj))
            if 1 <= nota <= 10:
                return nota
            print("Eroare: Nota trebuie să fie între 1 și 10.")
        except ValueError:
            print("Eroare: Te rog introdu un număr întreg.")

def calculeaza_media_materie(note, nota_teza=None):
    """Calculează media aritmetică sau media cu teză (pondere 3/4)."""
    media_note = sum(note) / len(note)
    
    if nota_teza:
        # Formula oficială: (Media_notelor * 3 + Teza) / 4
        media_finala = (media_note * 3 + nota_teza) / 4
    else:
        media_finala = media_note
        
    # Rotunjire matematică (0.5 merge în sus)
    return math.floor(media_finala + 0.5)

def main():
    print("--- Sistem Gestiune Catalog Școlar ---")
    catalog = {}
    
    numar_materii = int(input("Câte materii dorești să introduci? "))

    for _ in range(numar_materii):
        nume_materie = input("\nNumele materiei: ").strip().capitalize()
        
        # Citirea notelor
        while True:
            note_raw = input(f"Introdu notele la {nume_materie} (separate prin spațiu): ")
            note = [int(n) for n in note_raw.split() if n.isdigit() and 1 <= int(n) <= 10]
            if note:
                break
            print("Eroare: Trebuie să introduci cel puțin o notă validă.")

        # Verificare teză
        are_teza = input("Are această materie teză? (da/nu): ").lower().strip()
        teza = None
        if are_teza == 'da':
            teza = valideaza_nota(f"Nota la teza pentru {nume_materie}: ")

        # Calcul și salvare în catalog
        media_rotunjita = calculeaza_media_materie(note, teza)
        catalog[nume_materie] = {
            "note": note,
            "teza": teza,
            "medie_finala": media_rotunjita
        }

    # Afișare Raport Final
    print("\n" + "="*40)
    print(f"{'MATERIE':<15} | {'NOTE':<15} | {'TEZĂ':<5} | {'MEDIE'}")
    print("-" * 40)
    
    suma_mediilor = 0
    for materie, date in catalog.items():
        teza_str = str(date['teza']) if date['teza'] else "-"
        note_str = str(date['note'])
        print(f"{materie:<15} | {note_str:<15} | {teza_str:<5} | {date['medie_finala']}")
        suma_mediilor += date['medie_finala']

    media_anuala = suma_mediilor / len(catalog)
    print("-" * 40)
    print(f"MEDIA ANUALĂ GENERALĂ: {media_anuala:.2f}")

if __name__ == "__main__":
    main()
