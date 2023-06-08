import hl7apy.parser
from fhir.resources.bundle import Bundle
from fhir.resources.patient import Patient
from fhir.resources.observation import Observation

def convert_hl7v2_to_fhir(hl7v2_message):
    # Parse HL7v2 message
    hl7_message = hl7apy.parser.parse_message(hl7v2_message)
    
    # Extract relevant data from the HL7v2 message
    patient_name = hl7_message.PID.PID_3.PID_3_2.value
    patient_gender = hl7_message.PID.PID_8.value
    observation_value = hl7_message.OBX.OBX_5.value
    
    # Create FHIR resources
    bundle = Bundle()
    
    patient = Patient()
    patient.name = [{"family": patient_name}]
    patient.gender = patient_gender
    
    observation = Observation()
    observation.valueQuantity = {"value": float(observation_value)}
    
    # Add resources to the bundle
    bundle.entry = [
        {"resource": patient},
        {"resource": observation}
    ]
    
    return bundle

# Example usage
hl7v2_message = "MSH|^~\&|MCC|MCC|Fremdsystem||20230522133440||ORM^O01^ORM_O01|5|P|2.5|||AL|NE|||||PID||122600|122600||Schorsten^Inge||19550201|W|||Bahnhofstr. 34^^Kempten^^87437^DE||555-6666|||||||||||||||||||PV1||S|ST-11^^^FA-ACH|11||||||NP|||||||||0000701854|||||NP|||||||||||||||C1A|||||20230522131600|||||||||ORC|NW||||||^^^20230522000000^^ROUTINE||20230522133430||NAE^Nagel^Ernst^^^Dr.|RADA^Radiologe^Test|ST-11^Station 11|||Kopfverletzung||RAD||OBR|1|||SCH^Schädel^^RAD|||20230522000000|20230522133430||||||||||Kopfverletzung||||||||||||0||||||||||||||OBX|1|ST|KMA^Kontrastmittelallergie||N||||||F||||||||OBX|2|SI|GEW^Gewicht||90||||||F||||||||IN1|1|0005000374|9116769|AOK Kempten|Postfach 1240^^Kempten^^0||||||||||M|||||||1||||||||||||||||||||||||||||"
fhir_bundle = convert_hl7v2_to_fhir(hl7v2_message)
print(fhir_bundle.json())
