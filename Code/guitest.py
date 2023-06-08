import tkinter as tk
import requests
#10466180
#10713510
api_url = "http://hapi.fhir.org/baseR4/Patient/"

def fetch():
    id = id_entry.get()
    response = requests.get(api_url+id)    
    print(response.json())

    data = response.json()
    namepart = data['name']
    addresspart = data['address']
    print(addresspart)
    name = namepart[0]['family']
    address = addresspart[0]['line']
    firstname = namepart[0]['given']
    print(name)
    print(firstname)
    print(address)
    
    eingabefeld_wert.set(name)
    vorname_wert.set(firstname)
    adresse_wert.set(address)


def update():
    name = name_entry.get()
    vorname = vorname_entry.get()
    adresse = adresse_entry.get()
    telefon = telefon_entry.get()
    geschlecht = geschlecht_var.get()
    geburtsdatum = geburtsdatum_entry.get()
    verheiratet = verheiratet_var.get()

    #add put command here

def submit():
    #id = id_entry.get()
    name = name_entry.get()
    vorname = vorname_entry.get()
    adresse = adresse_entry.get()
    telefon = telefon_entry.get()
    geschlecht = geschlecht_var.get()
    geburtsdatum = geburtsdatum_entry.get()
    verheiratet = verheiratet_var.get()

    # add post command here
    patient = {
    "resourceType": "Patient",
    "meta": {
        "versionId": "1",
        "lastUpdated": "2023-05-04T16:06:50.008+00:00",
        "source": "#ofXCNx1CpjLE6oAW"
    },
    "text": {
        "status": "generated",
     },
    "name": [
        {
            "text": vorname+name,
            "family": name,
            "given": [
                vorname
            ]
        }
    ],
    "address": [
        {
            "text": adresse+" in Musterstadt",
            "line": [
                adresse
            ],
            "city": "Musterstadt",
            "postalCode": "12345"
        }
    ]
}
    response = requests.post(api_url, json=patient)
    data = response.json()
    id = data['id']
    id_wert.set(id)
    print("ID:", id)
    print("Name:", name)
    print("Vorname:", vorname)
    print("Adresse:", adresse)
    print("Telefon (privat):", telefon)
    print("Geschlecht:", geschlecht)
    print("Geburtsdatum:", geburtsdatum)
    print("Verheiratet:", verheiratet)

window = tk.Tk()
window.title("Personeninformationen")

fetch_button = tk.Button(window, text="Fetch patient", command=fetch)
fetch_button.pack()
# ID
id_label = tk.Label(window, text="ID:")
id_label.pack()
id_wert=tk.StringVar()
id_entry = tk.Entry(window, textvariable=id_wert)
id_entry.pack()

# Name
name_label = tk.Label(window, text="Name:")
name_label.pack()
eingabefeld_wert=tk.StringVar()
name_entry = tk.Entry(window, textvariable=eingabefeld_wert)
name_entry.pack()

# Vorname
vorname_label = tk.Label(window, text="Vorname:")
vorname_label.pack()
vorname_wert =tk.StringVar()
vorname_entry = tk.Entry(window, textvariable=vorname_wert)
vorname_entry.pack()

# Adresse
adresse_label = tk.Label(window, text="Adresse:")
adresse_label.pack()
adresse_wert = tk.StringVar()
adresse_entry = tk.Entry(window, textvariable=adresse_wert)
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

update_button = tk.Button(window, text="Update", command=update)
update_button.pack()

window.mainloop()
