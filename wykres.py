import matplotlib.pyplot as plt
import pandas as pd

# Wczytanie danych z pliku CSV
data = pd.read_csv("wykres.csv")

# Wyodrębnienie kolumn z danymi
atrakcyjnosc_rynku = data["Atrakcyjność rynku"]
pozycja_konkurencyjna = data["Pozycja konkurencyjna"]

# Ustawienie wartości początkowej osi X
wartosc_poczatkowa_osi_x = 500

# Wygenerowanie wykresu
plt.figure(figsize=(10, 6))
plt.plot(pozycja_konkurencyjna, atrakcyjnosc_rynku, marker='o', linestyle='-')

# Ustawienie etykiet osi
plt.xlabel("Pozycja konkurencyjna")
plt.ylabel("Atrakcyjność rynku")

# Ustawienie zakresu osi Y od 0 wzwyż
plt.ylim(bottom=0)

# Ustawienie wartości początkowej osi X
plt.xlim(left=wartosc_poczatkowa_osi_x)

# Dodanie tytułu wykresu
plt.title("Atrakcyjność rynku w zależności od pozycji konkurencyjnej")

# Wyświetlenie wykresu
plt.grid(True)
plt.show()
