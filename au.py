class DiseaseDiagnosisSystem:
 def __init__(self):
 self.symptoms = [
 'Flu', 'Yellowish eyes and skin', 'Dark color urine',
 'Pale bowel movement', 'Fatigue', 'Vomitting', 'Fever',
 'Pain in joints', 'Weakness', 'Stomach Pain'
 ]

 self.treatments = {
 'Flu': 'Drink hot water, avoid cold eatables.',
 'Yellowish eyes and skin': 'Put eye drops, have healthy sleep, do not strain your eyes.',
 'Dark color urine': 'Drink lots of water, juices and eat fruits. Avoid alcohol consumption.',
 'Pale bowel movement': 'Drink lots of water and exercise regularly.',
 'Fatigue': 'Drink lots of water, juices and eat fruits.',
 'Vomitting': 'Drink salt and water.',
 'Fever': 'Put hot water cloth on head and take crocin.',
 'Pain in joints': 'Apply pain killer and take crocin.',
 'Weakness': 'Drink salt and water, eat fruits.',
 'Stomach Pain': 'Avoid outside food and eat fruits.'
 }

 self.patient_data = {}
 self.diseases = {
 'hemochromatosis': ['Stomach Pain', 'Pain in joints', 'Weakness', 'Dark color urine', 'Yellowish eyes and skin'],
 'hepatitis_c': ['Pain in joints', 'Fever', 'Fatigue', 'Vomitting', 'Pale bowel movement'],
 'hepatitis_b': ['Pale bowel movement', 'Dark color urine', 'Yellowish eyes and skin'],
 'hepatitis_a': ['Flu', 'Yellowish eyes and skin'],
 'jaundice': ['Yellowish eyes and skin'],
 'flu': ['Flu']
 }

 def collect_symptoms(self):
 print("Please answer the following questions with yes or no:")
 for symptom in self.symptoms:
 answer = input(f"Does the patient have {symptom}? ").lower()
 while answer not in ['yes', 'no']:
 answer = input("Please answer with yes or no: ").lower()
 if answer == 'yes':
 self.patient_data[symptom] = True
 else:
 self.patient_data[symptom] = False

 def diagnose_disease(self):
 possible_diseases = []
 for disease, symptoms in self.diseases.items():
 if all(self.patient_data.get(symptom, False) for symptom in symptoms):
 possible_diseases.append(disease)

 return possible_diseases

 def print_possible_diseases(self, possible_diseases):
 if possible_diseases:
 print("The patient may suffer from:")
 for disease in possible_diseases:
 print(disease)
 else:
 print("No matching diseases found based on symptoms provided.")

 def provide_treatment_advice(self):
 print("\nTreatment advice:")
 for symptom, has_symptom in self.patient_data.items():
 if has_symptom:
 print(f"For {symptom}: {self.treatments.get(symptom)}")
 def start_diagnosis(self):
 self.collect_symptoms()
 possible_diseases = self.diagnose_disease()
 self.print_possible_diseases(possible_diseases)
 self.provide_treatment_advice()
if __name__ == "__main__":
 diagnosis_system = DiseaseDiagnosisSystem()
 diagnosis_system.start_diagnosis(
