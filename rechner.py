#Taschenrechner für Billy
import tkinter as tk
import string

# Hauptfenster
root = tk.Tk()
root.title("Who get's the Weed? 🍃")
root.geometry("600x400")
root.configure(bg="#2e2e2e")  # dunkler Hintergrund


# Listen für Eingaben und Ergebnisse
personen = []
ergebnisse = []
personen_index = 2 

# Frame für Gesamtmenge
frame_gesamt = tk.Frame(root, bg="#2e2e2e")
frame_gesamt.pack(pady=15)

label_essen = tk.Label(frame_gesamt, text="Gesamtmenge (g):", fg="white", bg="#2e2e2e", font=("Arial", 12))
label_essen.grid(row=0, column=0, padx=5)

feld_essen = tk.Entry(frame_gesamt, justify="center", font=("Arial", 12))
feld_essen.grid(row=0, column=1, padx=5)

# Frame für Personen
frame_personen = tk.Frame(root, bg="#2e2e2e")
frame_personen.pack(pady=10)

# Billy
labelA = tk.Label(frame_personen, text="Kiffer Nr. 1 (Billy) zahlt:", fg="white", bg="#2e2e2e", font=("Arial", 12))
labelA.grid(row=0, column=0, padx=5, pady=3)

feld1 = tk.Entry(frame_personen, justify="center", font=("Arial", 12))
feld1.grid(row=0, column=1, padx=5, pady=3)
personen.append(feld1)

ergebnisA = tk.Label(frame_personen, text="0 g", fg="lightgreen", bg="#2e2e2e", font=("Arial", 12, "bold"))
ergebnisA.grid(row=0, column=2, padx=5, pady=3)
ergebnisse.append(ergebnisA)

# Funktion: neue Person hinzufügen
def person_hinzufuegen():
    global personen_index

    row = len(personen)  # 🔥 WICHTIG: nächste freie Zeile

    label = tk.Label(
        frame_personen,
        text=f"Kiffer Nr. {personen_index} zahlt:",
        fg="white",
        bg="#2e2e2e",
        font=("Arial", 12)
    )
    label.grid(row=row, column=0, padx=5, pady=3)

    feld = tk.Entry(frame_personen, justify="center", font=("Arial", 12))
    feld.grid(row=row, column=1, padx=5, pady=3)
    personen.append(feld)

    ergebnis = tk.Label(
        frame_personen,
        text="0 g",
        fg="lightgreen",
        bg="#2e2e2e",
        font=("Arial", 12, "bold")
    )
    ergebnis.grid(row=row, column=2, padx=5, pady=3)
    ergebnisse.append(ergebnis)

    personen_index += 1

# Frame für Buttons
frame_buttons = tk.Frame(root, bg="#2e2e2e")
frame_buttons.pack(pady=20)

add_button = tk.Button(frame_buttons, text="Person hinzufügen", command=person_hinzufuegen,
                       bg="#1a5f3f", fg="white", font=("Arial", 12), width=15)
add_button.grid(row=0, column=0, padx=10)

def rechnen():
    try:
        gesamt_essen = float(feld_essen.get())
        betraege = []
        for feld in personen:
            wert = feld.get()
            if wert.strip() == "":
                wert = "0"
            betraege.append(float(wert))
        gesamtbetrag = sum(betraege)
        if gesamtbetrag == 0:
            for e in ergebnisse:
                e.config(text="0 g")
            return
        anteile = [(betrag / gesamtbetrag) * gesamt_essen for betrag in betraege]
        for i, wert in enumerate(anteile):
            ergebnisse[i].config(text=f"{wert:.1f} g")
    except ValueError:
        print("Bitte nur Zahlen eingeben!")

rechnen_button = tk.Button(frame_buttons, text="Berechnen", command=rechnen,
                           bg="#229e64", fg="white", font=("Arial", 12), width=15)
rechnen_button.grid(row=0, column=1, padx=10)

root.mainloop()
