# 1. Vytvoreni pole s 5 stringovymi hodnotami
pole = ["voda", "vzduch", "ohen", "zem", "teplo"]
print("Puvodni pole:", pole)

# 2. Pridani stringu pomoci append
pole.append("vitr")
print("Pole po pridani vitr:", pole)

# 3. Odstraneni druheho prvku pomoci remove
pole.remove(pole[1])  # Druhy prvek je vzduch
print("Pole po odstraneni druheho prvku:", pole)

# 4. Zameneni 5. hodnoty za slunce
pole[4] = "slunce"
print("Pole po zameneni 5. hodnoty za slunce:", pole)

# 5. Pridani 2 stringovych hodnot pomoci extend
pole.extend(["lahev", "zbran"])
print("Pole po pridani lahev a zbran pomoci extend:", pole)