class Symptom:
    def __init__(self, name):
        self.name = name

class Disease:
    def __init__(self, name, symptoms):
        self.name = name
        self.symptoms = symptoms

    def matches(self, patient_symptoms):
        return any(symptom.lower() in patient_symptoms for symptom in self.symptoms)

class Patient:
    def __init__(self):
        self.symptoms = []

    def add_symptom(self, symptom):
        self.symptoms.append(symptom.lower())  


diseases = [
    Disease("Common Cold", ["runny or stuffy nose", "sneezing", "sore throat", "cough", "mild fever", "fatigue"]),
    Disease("Influenza (Flu)", ["high fever", "chills", "muscle aches", "cough", "fatigue", "sore throat", "headache"]),
    Disease("Dengue Fever", ["high fever", "severe headache", "joint and muscle pain", "rash", "nausea", "bleeding gums"]),
    Disease("Malaria", ["high fever", "chills", "sweating", "headache", "vomiting", "muscle pain", "fatigue"]),
    Disease("Typhoid", ["prolonged fever", "abdominal pain", "headache", "constipation or diarrhea", "fatigue"]),
    Disease("Diabetes", ["increased thirst", "frequent urination", "fatigue", "blurred vision", "slow wound healing"]),
    Disease("Hypertension", ["often asymptomatic", "headaches", "dizziness", "shortness of breath", "nosebleeds (in severe cases)"]),
    Disease("Tuberculosis (TB)", ["persistent cough (sometimes with blood)", "fever", "night sweats", "weight loss", "fatigue"]),
    Disease("Pneumonia", ["cough with phlegm", "fever", "chills", "shortness of breath", "chest pain", "fatigue"]),
    Disease("Asthma", ["wheezing", "shortness of breath", "chest tightness", "coughing (especially at night)"]),
    Disease("Cholera", ["severe diarrhea", "dehydration", "vomiting", "muscle cramps"]),
    Disease("COVID-19", ["fever", "cough", "difficulty breathing", "loss of taste or smell", "fatigue", "body aches"]),
    Disease("Jaundice", ["yellowing of the skin and eyes", "dark urine", "fatigue", "abdominal pain", "nausea"]),
    Disease("Hepatitis A", ["fever", "fatigue", "abdominal pain", "dark urine", "jaundice", "loss of appetite"]),
    Disease("Chickenpox", ["itchy rash", "fever", "fatigue", "headache", "loss of appetite"]),
    Disease("Measles", ["high fever", "cough", "runny nose", "red eyes", "rash that spreads across the body", "fever"]),
    Disease("Polio", ["fever", "headache", "muscle weakness", "paralysis (in severe cases)"]),
    Disease("Scabies", ["intense itching (especially at night)", "rash", "thin burrow tracks on the skin"]),
    Disease("Anemia", ["fatigue", "pale skin", "dizziness", "shortness of breath", "cold hands and feet"]),
]


patient = Patient()
while True:
    symptom = input("Enter a symptom (or 'done' to finish): ")
    if symptom.lower() == 'done':
        break
    patient.add_symptom(symptom)


possible_diseases = [disease.name for disease in diseases if disease.matches(patient.symptoms)]

if possible_diseases:
    print("Possible diseases:", possible_diseases)
else:
    print("No possible diseases found for the given symptoms.")