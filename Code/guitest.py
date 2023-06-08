import tkinter as tk

def submit():
    name = name_entry.get()
    vorname = vorname_entry.get()
    adresse = adresse_entry.get()
    telefon = telefon_entry.get()
    geschlecht = geschlecht_var.get()
    geburtsdatum = geburtsdatum_entry.get()
    verheiratet = verheiratet_var.get()

    print("Name:", name)
    print("Vorname:", vorname)
    print("Adresse:", adresse)
    print("Telefon (privat):", telefon)
    print("Geschlecht:", geschlecht)
    print("Geburtsdatum:", geburtsdatum)
    print("Verheiratet:", verheiratet)

window = tk.Tk()
window.title("Personeninformationen")

# Name
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Vorname
vorname_label = tk.Label(window, text="Vorname:")
vorname_label.pack()
vorname_entry = tk.Entry(window)
vorname_entry.pack()

# Adresse
adresse_label = tk.Label(window, text="Adresse:")
adresse_label.pack()
adresse_entry = tk.Entry(window)
adresse_entry.pack()

# Telefon (privat)
telefon_label = tk.Label(window, text="Telefon (privat):")
telefon_label.pack()
telefon_entry = tk.Entry(window)
telefon_entry.pack()

# Geschlecht
geschlecht_label = tk.Label(window, text="Geschlecht:")
geschlecht_label.pack()
geschlecht_var = tk.StringVar()
geschlecht_radiobutton1 = tk.Radiobutton(window, text="Männlich", variable=geschlecht_var, value="männlich")
geschlecht_radiobutton1.pack()
geschlecht_radiobutton2 = tk.Radiobutton(window, text="Weiblich", variable=geschlecht_var, value="weiblich")
geschlecht_radiobutton2.pack()

# Geburtsdatum
geburtsdatum_label = tk.Label(window, text="Geburtsdatum:")
geburtsdatum_label.pack()
geburtsdatum_entry = tk.Entry(window)
geburtsdatum_entry.pack()

# Verheiratet
verheiratet_label = tk.Label(window, text="Verheiratet:")
verheiratet_label.pack()
verheiratet_var = tk.BooleanVar()
verheiratet_checkbox = tk.Checkbutton(window, text="Ja", variable=verheiratet_var)
verheiratet_checkbox.pack()

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()

window.mainloop()
