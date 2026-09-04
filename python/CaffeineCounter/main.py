def get_name():
    name = input("Gib deinen Namen ein: ")
    return name

def get_type():
    type_input = input("Gib ein welche Art von Koffein du konsumierst (z.B. Kaffee, Tee, Energy, Koffein-Tabletten, etc.): ")
    return type_input

def get_count():
    count = input("Gib ein wie viel du pro Tag ca. konsumierst: ")
    return count

def check_file_exists(filename):
    try:
        file = open(filename, "r")
        file.close()
        return True
    except FileNotFoundError:
        return False

def create_file(filename):
    file = open(filename, "w")
    file.write("name,type,count\n")
    file.close()

def append_entry(filename, name, type_input, count):
    file = open(filename, "a")
    file.write(name + "," + type_input + "," + count + "\n")
    file.close()

def main():
    filename = "caffeine-count.csv"

    if not check_file_exists(filename):
        create_file(filename)

    print("=" * 60)
    print("Willkommen beim DSI - Koffein-Zähler")
    print("Jede Person kann hier dokumentieren, wie ihr persönlicher Koffein-Konsum aussieht.")
    print("Dazu musst du folgendes eintragen:")
    print("- dein Name (auch Nicknames oder Aliase sind fine)")
    print("- deine Art des Konsum (Tee, Kaffee, Energy-Drink, Tabletten, etc.)")
    print("- die Menge die ungefähr täglich konsumierst")
    print("=" * 60)

    name = get_name()
    print("=" * 60)
    type_input = get_type()
    print("=" * 60)

    count = get_count()
    print("=" * 60)

    append_entry(filename, name, type_input, count)
    print("Danke! Deine Daten wurden gespeichert.")
    print("Du kannst die Dateien nun comitten und pushen und dich und deinen Koffeinkonsum im DSI-Git verewigen.")

main()