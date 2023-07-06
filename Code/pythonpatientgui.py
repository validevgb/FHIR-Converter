import tkinter as tk
import requests
#Bsp-IDs
#10914028 Patient_Id
#10914118 Patient Id2
#10914120 Patient Id3
#63486-5 LOINC Nussallergie
#10914029 Observation-Id

api_url = "http://hapi.fhir.org/baseR4/Patient/"
api_url_observation = "http://hapi.fhir.org/baseR4/Observation/"

def fetch():
    id = id_entry.get()
    response = requests.get(api_url+id)    
    print(response.json())
    data = response.json()

    namepart = data['name']    
    name = namepart[0]['family']
    firstname = namepart[0]['given']
    name_value.set(name)
    firstname_value.set(firstname)

    addresspart = data['address'] 
    address = addresspart[0]['line'][0]    
    address_value.set(address)

    phonepart = data['telecom']
    phonenumber = phonepart[1]['value']
    phone_value.set(phonenumber)

    gender_value.set(data['gender'])

    birthdate_value.set(data['birthDate'])

    maritalstatus_part = data['maritalStatus']
    status = maritalstatus_part['coding'][0]['code']
    if(status == "M"):
        marital_value.set(True)
    else:
        marital_value.set(False)
    
    observation_id= "10914029"
    observationres = requests.get(api_url_observation+observation_id)    
    print(observationres.json())
    data = observationres.json()
    loinc_part = data['code']
    loinc_value.set(loinc_part['coding'][0]['code'])
    loinc2_value.set(loinc_part['text'])

def submit_data():
    patient = GenerateJson()
    response = requests.post(api_url, json=patient)
    data = response.json()
    print(data)
    id = data['id']
    if(loinc_entry.get() != ""):
        observation = GenerateObservationJson(loinc_entry.get(), loinc2_entry.get(), id)
        response2 = requests.post(api_url_observation, json=observation)
        print(response2.json())
        observationdata = response2.json()
        global observation_id
        observation_id = observationdata['id']
    
    id_value.set(id)    

def update_data():
    id = id_entry.get()
    response = requests.put(api_url+id, json=GenerateJson())
    print(response.json())

# Create the main window
window = tk.Tk()
window.title("FHIR Patient")

# Create the header row
header_frame = tk.Frame(window)
header_frame.pack()
header_button = tk.Button(header_frame, text="Fetch", command=fetch)
header_button.pack()

header_label = tk.Label(header_frame, text="Enter Patient ID:")
header_label.pack()

# Create the left column
left_frame = tk.Frame(window)
left_frame.pack(side=tk.LEFT)

id_label = tk.Label(left_frame, text="ID:")
id_label.pack()
id_value = tk.StringVar()
id_entry = tk.Entry(left_frame, textvariable=id_value)
id_entry.pack()

name_label = tk.Label(left_frame, text="Name:")
name_label.pack()
name_value = tk.StringVar()
name_entry = tk.Entry(left_frame, textvariable=name_value)
name_entry.pack()

first_name_label = tk.Label(left_frame, text="First Name:")
first_name_label.pack()
firstname_value = tk.StringVar()
first_name_entry = tk.Entry(left_frame, textvariable=firstname_value)
first_name_entry.pack()

address_label = tk.Label(left_frame, text="Address:")
address_label.pack()
address_value = tk.StringVar()
address_entry = tk.Entry(left_frame, textvariable=address_value)
address_entry.pack()

phone_label = tk.Label(left_frame, text="Phone:")
phone_label.pack()
phone_value = tk.StringVar()
phone_entry = tk.Entry(left_frame, textvariable=phone_value)
phone_entry.pack()

gender_label = tk.Label(left_frame, text="Gender:")
gender_label.pack()
gender_value = tk.StringVar()
gender_value.set("Male")
gender_rb1 = tk.Radiobutton(left_frame, text="Male", variable=gender_value, value="male")
gender_rb1.pack()
gender_rb2 = tk. Radiobutton(left_frame, text="Female", variable=gender_value, value="female")
gender_rb2.pack()

# Create the right column
right_frame = tk.Frame(window)
right_frame.pack(side=tk.LEFT)


marital_status_label = tk.Label(right_frame, text="Marital Status:")
marital_status_label.pack()
marital_value = tk.BooleanVar()
marital_status_checkbox = tk.Checkbutton(right_frame, text="Married", variable=marital_value)
marital_status_checkbox.pack()

birthdate_label = tk.Label(right_frame, text="Birthdate: (yyyy-mm-dd)")
birthdate_label.pack()
birthdate_value = tk.StringVar()
birthdate_entry = tk.Entry(right_frame, textvariable=birthdate_value)
birthdate_entry.pack()

right_left_frame = tk.Frame(right_frame)
right_left_frame.pack(side=tk.LEFT)

loinc_label = tk.Label(right_left_frame, text="LOINC:")
loinc_label.pack()
loinc_value = tk.StringVar()
loinc_entry = tk.Entry(right_left_frame, textvariable=loinc_value)
loinc_entry.pack()

icd_label = tk.Label(right_left_frame, text="ICD:")
icd_label.pack()
icd_entry = tk.Entry(right_left_frame)
icd_entry.pack()

ops_label = tk.Label(right_left_frame, text="OPS:")
ops_label.pack()
ops_entry = tk.Entry(right_left_frame)
ops_entry.pack()

snomed_label = tk.Label(right_left_frame, text="SNOMED:")
snomed_label.pack()
snomed_entry = tk.Entry(right_left_frame)
snomed_entry.pack()


right_right_frame = tk.Frame(right_frame)
right_right_frame.pack(side=tk.RIGHT)

loinc2_label = tk.Label(right_right_frame, text="LOINC Text:")
loinc2_label.pack()
loinc2_value = tk.StringVar()
loinc2_entry = tk.Entry(right_right_frame, textvariable=loinc2_value)
loinc2_entry.pack()

icd2_label = tk.Label(right_right_frame, text="ICD Text:")
icd2_label.pack()
icd2_entry = tk.Entry(right_right_frame)
icd2_entry.pack()

ops2_label = tk.Label(right_right_frame, text="OPS Text:")
ops2_label.pack()
ops2_entry = tk.Entry(right_right_frame)
ops2_entry.pack()

snomed2_label = tk.Label(right_right_frame, text="SNOMED Text:")
snomed2_label.pack()
snomed2_entry = tk.Entry(right_right_frame)
snomed2_entry.pack()


# Create the footer row
footer_frame = tk.Frame(right_left_frame)
footer_frame.pack(side=tk.BOTTOM)

footer_button1 = tk.Button(footer_frame, text="Update", command=update_data)
footer_button1.pack(side=tk.LEFT)

footer_frame2 = tk.Frame(right_right_frame)
footer_frame2.pack(side=tk.BOTTOM)

footer_button2 = tk.Button(footer_frame2, text="Save", command=submit_data)
footer_button2.pack(side=tk.LEFT)

def GenerateJson():
    id_val = id_entry.get()
    name_val = name_entry.get()
    first_name_val = first_name_entry.get()
    address_val = address_entry.get()
    phone_val = phone_entry.get()
    gender_val = gender_value.get()
    birthdate_val = birthdate_entry.get()
    marital_status_val = marital_value.get()
    if(marital_status_val == True):
        marital_status_val = "M"
    else:
        marital_status_val = "U"
    icd_val = icd_entry.get()
    ops_val = ops_entry.get()
    snomed_val = snomed_entry.get()
    loinc_val = loinc_entry.get()
    icd2_val = icd2_entry.get()
    ops2_val = ops2_entry.get()
    snomed2_val = snomed2_entry.get()
    loinc2_val = loinc2_entry.get()

    print(f"ID: {id_val}")
    print(f"Name: {name_val}")
    print(f"First Name: {first_name_val}")
    print(f"Address: {address_val}")
    print(f"Phone: {phone_val}")
    print(f"Gender: {gender_val}")
    print(f"Birthdate: {birthdate_val}")
    print(f"Marital Status: {marital_status_val}")
    print(f"ICD: {icd_val}")
    print(f"OPS: {ops_val}")
    print(f"SNOMED: {snomed_val}")
    print(f"LOINC: {loinc_val}")
    print(f"ICDText: {loinc2_val}")

    
    patient = {
    "resourceType": "Patient",
    "id": id_val,
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
            "text": first_name_val+name_val,
            "family": name_val,
            "given": [
                first_name_val
            ]
        }
    ],
    "telecom" : [{
      "use" : "home"
    },
    {
      "system" : "phone",
      "value" : phone_val
    }
    ],
    "gender" : gender_val,
    "birthDate" : birthdate_val,
    "address": [
        {
            "text": address_val+" in Musterstadt",
            "line": [
                address_val
            ],
            "city": "Musterstadt",
            "postalCode": "12345"
        }
    ],
    "maritalStatus": {
        "coding":[{
            "system":"http://terminology.hl7.org/CodeSSystem/v3-MaritalStatus",
            "code":marital_status_val
        }],
        "text": "example"
    }
}
    return patient

def GenerateObservationJson(loinc_val, loinc2_val, id_val):
    observation = {
    "resourceType": "Observation",
    "id": "example",    
    "code": {
      "coding": [
        {
          "system": "http://loinc.org",
          "code": loinc_val
        }
      ],
      "text": loinc2_val
    },
    "subject": {
      "reference": "Patient/"+id_val
    }
  }
    return observation

window.mainloop()