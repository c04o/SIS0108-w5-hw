import models.patient as p

def add_patient(queue, name, age, symptom, priority):
    patient = p.Patient(name, age, symptom, priority)
    queue.append(patient)

def show_queue(queue):
    if not queue:
        print("No patients in queue.")
        return
    print("\nPatient list in arrival order:")
    for idx, patient in enumerate(queue, 1):
        print(f"{idx}. {patient.name} | Age: {patient.age} | Main symptom: {patient.symptom} | priority: {patient.priority}")

# Attend net patient
def attend_patient(queue):
    if not queue:
        print("No patients to attend.")
        return
    patient = queue.pop(0)
    print(f"Attended patient: {patient.name} with main symptom: {patient.symptom}")
