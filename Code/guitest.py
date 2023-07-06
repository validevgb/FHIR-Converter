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
    #geschlecht = geschlecht_var.get()
    geburtsdatum = geburtsdatum_entry.get()
    verheiratet = verheiratet_var.get()

    #add put command here

def submit():
    #id = id_entry.get()
    name = name_entry.get()
    vorname = vorname_entry.get()
    adresse = adresse_entry.get()
    telefon = telefon_entry.get()
    geschlecht = geschlecht_wert.get()
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
window.title("Patientendaten")


# ID
id_label = tk.Label(window, text="ID:")
id_label.pack()
id_wert=tk.StringVar()
id_entry = tk.Entry(window, textvariable=id_wert)
id_entry.pack()

fetch_button = tk.Button(window, text="Patient abrufen", command=fetch)
fetch_button.pack()
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
geschlecht_wert = tk.StringVar()
geschlecht_wert.set("männlich")
geschlecht_radiobutton1 = tk.Radiobutton(window, text="Männlich", variable=geschlecht_wert, value="männlich")
geschlecht_radiobutton1.pack()
geschlecht_radiobutton2 = tk.Radiobutton(window, text="Weiblich", variable=geschlecht_wert, value="weiblich")
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





#ICD, OPS, SNOMED CT,LOINC
codes_label = tk.Label(window, text="Fields for ICD, OPS, SNOMED and LOINC Codes (2 Diagnosis max.)")
codes_label.pack()
# Create the left column
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

icd1_label = tk.Label(left_frame, text="ICD1")
icd1_label.pack()
icd1_var = tk.StringVar()
icd1_entry = tk.Entry(left_frame, textvariable=icd1_var)
icd1_entry.pack()

ops1_label = tk.Label(left_frame, text="OPS1")
ops1_label.pack()
ops1_var = tk.StringVar()
ops1_entry = tk.Entry(left_frame, textvariable=ops1_var)
ops1_entry.pack()

snomed1_label = tk.Label(left_frame, text="SNOMED1")
snomed1_label.pack()
snomed1_var = tk.StringVar()
snomed1_entry = tk.Entry(left_frame, textvariable=snomed1_var)
snomed1_entry.pack()

loinc1_label = tk.Label(left_frame, text="LOINC1")
loinc1_label.pack()
loinc1_var = tk.StringVar()
loinc1_entry = tk.Entry(left_frame, textvariable=loinc1_var)
loinc1_entry.pack()

# Create the right column
right_frame = tk.Frame(window)
right_frame.pack(side=tk.RIGHT)

icd2_label = tk.Label(right_frame, text="ICD2")
icd2_label.pack()
icd2_var = tk.StringVar()
icd2_entry = tk.Entry(right_frame, textvariable=icd2_var)
icd2_entry.pack()

ops2_label = tk.Label(right_frame, text="OPS2")
ops2_label.pack()
ops2_var = tk.StringVar()
ops2_entry = tk.Entry(right_frame, textvariable=ops2_var)
ops2_entry.pack()

snomed2_label = tk.Label(right_frame, text="SNOMED2")
snomed2_label.pack()
snomed2_var = tk.StringVar()
snomed2_entry = tk.Entry(right_frame, textvariable=snomed2_var)
snomed2_entry.pack()

loinc2_label = tk.Label(right_frame, text="LOINC2")
loinc2_label.pack()
loinc2_var = tk.StringVar()
loinc2_entry = tk.Entry(right_frame, textvariable=loinc2_var)
loinc2_entry.pack()

# Create the bottom row
bottom_frame = tk.Frame(window)
bottom_frame.pack(side=tk.BOTTOM)

submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack(side=tk.LEFT)

update_button = tk.Button(window, text="Update", command=update)
update_button.pack(side=tk.LEFT)

window.mainloop()
