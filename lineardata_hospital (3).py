# -*- coding: utf-8 -*-
"""lineardata_hospital

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NLTNGkS6HvnjaVl_1e_Fw2kYGmgc-zGU
"""

from collections import defaultdict, deque #importing modules
class PatientRecord: #creating a class for patient records
    def __init__(self, first_name, last_name, age, gender, height, weight, phonenumber, email, identifier, admission_date): #defining all the attributes
        self.first_name = first_name #assigning valoues for each of the attributes
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.height = height
        self.weight = weight
        self.phonenumber = phonenumber
        self.email = email
        self.identifier = identifier
        self.admission_date = admission_date
        self.appointments = [] #creating an empty list for appending the appointments
        self.medications = [] ##creating an empty list for appending the medications given to patients

    def add_appointment(self, doctor_name, date, time): #defining a function for adding the appointments in the list
        self.appointments.append((doctor_name, date, time)) #Using the append function to append appointments to the empty list

    def add_medication(self, medication_name): #defining a function for adding the medications in the list
        self.medications.append(medication_name) #Using the append function to append medications to the empty list

    def display_summary(self): #defining a method that would display all the patients record summary
        print("Patient Summary:") #printing the summary
        print(f"Name: {self.first_name} {self.last_name}") #printing all patient details
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Height: {self.height}")
        print(f"Weight: {self.weight}")
        print(f"Phone Number: {self.phonenumber}")
        print(f"Email: {self.email}")
        print(f"Admission Date: {self.admission_date}")

        if self.appointments: #using if statement for any appointments recorded for the patient.
            print("\nAppointments:") #printing the appointment
            for doctor_name, date, time in self.appointments: #for loop if there is any appointment, it would print out these attributes
                print(f"- Doctor: {doctor_name}, Date: {date}, Time: {time}") #printing our doctor's name, date, and time if there is an appointment

        if self.medications: #using if statement for any medication given
            print("\nMedications:") #printing the medication
            for medication in self.medications: #for loop if any mediciation is given to print out its information
                print(f"- {medication}") #printing medicine information

        print("\n") #ensuring there's a gap between all the prints so it's easier to read

class DoctorSchedule: #creating a class for doctor's schedules
    def __init__(self, doctor_name): #defining the attributes
        self.doctor_name = doctor_name #assigning a value
        self.schedule = defaultdict(list)  # Initialize schedule as a defaultdict where each key is a date and the value is a list of available time slots

    def add_slot(self, date, time): #defining a function that adds a slot to the doctor's schedule for a given date and time
        self.schedule[date].append(time) #appending time to doctor's schedule

    def remove_slot(self, date, time): #defining a function that removes a slot to the doctor's schedule for a given date and time
        if time in self.schedule[date]: #if statement for checking if the specified time exists in the list of time slots for the given date
            self.schedule[date].remove(time) #If it exists, it removes the time from the list
            return True #returns true
        else:
            return False #or else it returns false

    def display_schedule(self): #Defining a function for displaying the schedule
        for date, times in self.schedule.items(): #for loop to go over the dates avialable in the schedule
            print(f"Date: {date}") #printing the available dates
            print("Available Slots:")
            for time in times: #for loop to go over the times avialable in the schedule
                print(time) #printing the available time


class Doctor: #creating a class called doctor
    def __init__(self, doctor_name, doctor_schedule): #defining its attributes
        self.doctor_name = doctor_name #assigning values for these attributes
        self.schedule = doctor_schedule

    def book_slot(self, date, time, patient_name, patient_id): #defining a function for booking slots
        if (date, time) in self.schedule.schedule[date]: #if statement to check if the specidied date and time are avialable
            self.schedule.remove_slot(date, time)  # Remove the slot from the doctor's schedule
            self.schedule.booked_slots[(date, time)] = (self.doctor_name, patient_name, patient_id)  # Record the booked slot
            print(f"Slot booked successfully for {date} at {time} with doctor {self.doctor_name} for patient {patient_name} (ID: {patient_id}).") #print the information
        else:
            print("Sorry, that slot is not available.") #or else the slot is not avialable



    def cancel_slot(self, date, time): #defining a function for canceling the slot
        if self.schedule.add_slot(date, time): #if statement to check the specified date and time of the slot
            print(f"Slot cancelled successfully for {date} at {time} with doctor {self.doctor_name}.") #if found then the appointment is canceled at the given date and time
        else:
            print("Slot not found for cancellation.") #if not found then printing else statement

    def display_schedule(self): #defining a function for displaying the doctor's schedule
        self.schedule.display_schedule() #displaying the schedule


class PatientBookingSystem: #creating a class for patient booking
    def __init__(self, doctor_schedule): #defining its attributes
        if isinstance(doctor_schedule, DoctorSchedule): #if statement to check if the doctor_schedule provided is an instance of DoctorSchedule
            self.schedule = doctor_schedule #If it is, it assigns it to the schedule attribute
            self.booked_slots = {}  #initializing an empty dictionary to keep track of booked slots.

        else:
            raise ValueError("doctor_schedule must be an instance of DoctorSchedule") #or else it prints value error

    def book_slot(self, date, time, doctor_name, patient_name, patient_id): #defining a function to book slots with the doctor
        if date in self.schedule.schedule and time in self.schedule.schedule[date]: #is statment to see if the date and time are available in the doctors schedule
            if (date, time) not in self.booked_slots: #using another if statment to check if the date and time are not booked
                self.schedule.remove_slot(date, time)  # Remove the slot from the doctor's schedule
                self.booked_slots[(date, time)] = (doctor_name, patient_name, patient_id)  # Then recording the booked slot
                print(f"Slot booked successfully for {date} at {time} with doctor {doctor_name} for patient {patient_name} (ID: {patient_id}).") #printing the booked slot's information
            else:
                print("Slot already booked for this date and time.") #or else printing that the slot is already booked
        else:
            print("Sorry, that slot is not available.") #if both statments above fail therefore it prints that the slot is not available


class Hospital: #creating a class called hospital
    def __init__(self):
        self.doctors = {} #creating an empty dictionary to store the doctors that are associated with this hospital

    def add_doctor(self, doctor): #defining a function that adds a doctor to the hospital's records.
        self.doctors[doctor.doctor_name] = doctor #storing it in the doctor's dictionary
    def get_doctor_schedule(self, doctor_name): #defining a function that gets the doctors schedule
        doctor = self.doctors.get(doctor_name) # it gets the schedule given their name
        if doctor: #if the doctor schedule is found in the records
            return doctor.schedule #then it is returned
        return None #otherwise there's none

# Create registration system instance
hospital = Hospital()

class ListNode: #creating a class
    def __init__(self, data): #defining its attributes
        self.data = data #assigning values for the attrbutes
        self.next = None

class RegistrationSystem: #defining a class called the registarion system
    def __init__(self): #constructor to initilize multiple attributes
        self.patient_records = {} #doctrionary to store the patient records
        self.admission_dates = [] #list to store admission dates
        self.undo_stack = [] #a stack to keep track of registration actions for undoing.
        self.print_job_queue = deque() #a queue to store patient IDs for printing jobs.
        self.consultation_queue_head = None #the head of a linked list representing a consultation queue.
        self.prescription_stack = {} #a stack to store prescriptions.

    def register_patient(self, first_name, last_name, age, gender, height, weight, phonenumber, email, admission_date=None, identifier=None): #deifning a function for registering a new patient
        if identifier is None: #if there is no identifier
            identifier = len(self.patient_records) + 1 #it is auto-generated based on the number of existing patient records.
        else:
            identifier = int(identifier) #Otherwise the provided identifier is used.

        patient_record = PatientRecord(first_name, last_name, age, gender, height, weight, phonenumber, email, identifier, admission_date) #creating a new object called patient records with these details
        self.patient_records[identifier] = patient_record #adding the patient record to the dictionary with the identifier as the key.
        self.undo_stack.append(('register', identifier)) # recording the registration action in the undo stack
        self.print_job_queue.append(identifier) # adding the patient ID to the print job queue

        # Add the new patient to the consultation queue as a new node in the linked list
        new_node = ListNode(identifier) #createing a new node for the linked list with the patient's identifier as data.
        if self.consultation_queue_head is None: #if the queue is empty
            self.consultation_queue_head = new_node #the new node becomes head in the list of the consultation queue
        else:
            current = self.consultation_queue_head #otherwise the new node becomes the tail
            while current.next: #while loop to traverse through the nodes
                current = current.next #reaching the last node
            current.next = new_node #appending the new node

        print(f"Patient {first_name} {last_name} registered with ID {identifier} on {admission_date}") #printing a confirmation message of the registration.
        self.display_consultation_queue() #displaying the consultation queue


    def sort_patients_by_admission_date(self): #defining a function that sorts patients by their admission date
        sorted_records = sorted(self.patient_records.values(), key=lambda x: x.admission_date) #Using sorted method and extracting the values from patient records from the dictionary and using a lambda function as the key parameter to specify that sorting should be based on the admission date of each patient record
        return sorted_records #returning the sorted records

    def discharge_patient(self, identifier): #defining a function that discharges patients
        identifier = input("Enter patient's identifier: ")  #This line defines identifier which asks user to input
        identifier = int(identifier)  # Convert to integer
        del self.patient_records[identifier] #uses del to remove from patient records
        print(f"Patient with ID {identifier} discharged successfully.") #prints a verifiction of removal
        self.print_job_queue.remove(identifier) #uses remove method to remove from print job queue
        print("Patient removed from print job queue") #prints a verifiction of removal
        # Remove from consultation queue
        current = self.consultation_queue_head  # Set the current node to the head of the consultation queue
        prev = None  # Initialize a variable to track the previous node
        while current:  # Iterate through the consultation queue until the end is reached
            if current.data == identifier:  # Check if the current node's data matches the provided identifier
                if prev:  # If the node is not the head
                    prev.next = current.next  # Adjust the previous node's next pointer
                else:  # If the node is the head
                    self.consultation_queue_head = current.next  # Update the head pointer
                print("Patient removed from consultation queue")  # Print a message indicating successful removal
                break  # Exit the loop after removing the patient
            prev = current  # Move to the next node in the consultation queue
            current = current.next

    def undo_registration(self): #defining a function for undoing registration
        if self.undo_stack: #if we are undoing the stack
            action, identifier = self.undo_stack.pop() #it pops the last action
            if action == 'register': #If the action type is register
                del self.patient_records[identifier] #it reverses the registration action by deleting the patient's record
                print(f"Undo registration for patient with ID {identifier}") #printing that undoing the registration has been done
                if identifier in self.print_job_queue: #if the identifier is in the print job queue
                    self.print_job_queue.remove(identifier)  #then it removes them from the queue
                if self.consultation_queue_head: #checking if consultation queue is not empty
                    current = self.consultation_queue_head
                    prev = None
                    while current:
                        if current.data == identifier: #if the patient is found in the consultation queue
                            if prev: #if the node is not the head
                                prev.next = current.next
                            else: #if the node is the head
                                self.consultation_queue_head = current.next
                            break
                        prev = current
                        current = current.next
            else:
                print("Invalid action on undo stack") #otherwise it prints the else statement
        else:
            print("Nothing to undo") #if the statments above fail to work it'll print nothing to undo

    def update_patient_info(self, first_name, last_name, age, gender, height, weight, phonenumber, email, identifier): #defining a function to update patient's info
        patient_record = self.patient_records.get(identifier) #get the patient by their identifiers as the maiin parameter
        if patient_record: #using if statement to update each information
            # Update patient information
            patient_record.first_name = first_name #updating the first name
            patient_record.last_name = last_name #updating the last name
            patient_record.age = age #updating the age
            patient_record.gender = gender #updating the gender
            patient_record.height = height #updating the height
            patient_record.weight = weight #updating the weight
            patient_record.phonenumber = phonenumber #updating the phone number
            patient_record.email = email #updating the email
            self.patient_records[identifier] = patient_record  #retreiving the patient based on their identifier from the patient records
            print("Patient information updated successfully") #if it's successfull then it'll print this message successfully
        else:
            print("Patient not found") #otherwise it'll print that patient is not found

    def process_print_jobs(self):#This function prints the registered patients
        while self.print_job_queue: #This line uses a while loop that iterates over the print job queue
            identifier = self.print_job_queue.popleft() #This line deques the  leftmost item from the print jobs deque
            patient_record = self.patient_records.get(identifier) #This line retrieves the value associated with the identifier
            if patient_record: #This line checks if patient record exists
                # Update patient information before processing print job for all the attribtues
                self.update_patient_info(patient_record.first_name, patient_record.last_name, patient_record.age,
                                         patient_record.gender, patient_record.height, patient_record.weight,
                                         patient_record.phonenumber, patient_record.email, identifier)
                print(f"Printing patient record for {patient_record.first_name} {patient_record.last_name}")
                patient_record.display_summary()  # This line uses the display function to display patient summary
            else:
                print(f"Patient with ID {identifier} not found") #This line prints the specific pateint not found based on the identifier

    def retrieve_patient_info(self, identifier):#This function retrieve the patient's information
        identifier = int(identifier)  # This line converts identifier to integer
        patient_record = self.patient_records.get(identifier) #This line retrieves the value associated with the identifier
        if patient_record:#This line checks if patient record exists
            # This line updates patient information before retrieving
            self.update_patient_info(patient_record.first_name, patient_record.last_name, patient_record.age,
                                     patient_record.gender, patient_record.height, patient_record.weight,
                                     patient_record.phonenumber, patient_record.email, identifier)
            print("Patient found!") #This line prints patient found
            print("Patient Information:") #This line prints the header Patient Information
            patient_record.display_summary()  # This line uses the display function to display patient summary
        else:#if patient does not exists
            print("Patient not found") #This line prints patient not found
    def display_consultation_queue(self): #This function displays the consultation queue
        print("Consultation Queue:") #This line prints the header consultation queue
        current = self.consultation_queue_head #This line traverses the consultation queue starting from the head
        while current: #This line iterates through the consultation queue until current becomes None
            patient_id = current.data #This line extracts patient ID from the current node
            patient_record = self.patient_records.get(patient_id) #This line retrieves patient record from patient_records dictionary using patient_id
            if patient_record:#This line checks if patient record exists
                print(f"Patient ID: {patient_id}, Name: {patient_record.first_name} {patient_record.last_name}") #This line prints the patient ID and full name
            else:#if patient does not exists
                print(f"Patient with ID {patient_id} not found")#This line prints a message indicating the patient ID was not found
            current = current.next #This line moves to the next node in the consultation queue

    def schedule_appointment(self, identifier, doctor_name, date, time):  #This function schedules appointments to the patients
        if identifier in self.patient_records:  #This line checks if the patient exists
            self.consultation_queue[identifier] = (date, time)  #This line stores the scheduled appointment date and time for the given patient identifier in the consultation queue
            print(f"Scheduled appointment for patient ID {identifier} with Dr. {doctor_name} on {date} at {time}") #This line prints a confirmation message of the appointment
        else:#if the patient does not exist
            print("Patient not found") #This line prints patient not found
    def issue_prescription(self, identifier, medication_name): #This function issues prescriptions for the patients
        identifier = int(identifier) #This line converts it to an integer
        patient_record = self.patient_records.get(identifier) #This line retrieves the patient record from the patient records dictionary using the identifier
        if patient_record: #This line checks if the patient exists
            if identifier not in self.prescription_stack:#This line checks if the patient identifier is not already in the prescription stack
                self.prescription_stack[identifier] = [] #This line creates an empty list to store the prescrptions
            self.prescription_stack[identifier].append(medication_name) #This line appends the medication name to the prescription stack for the patient identifier
            print(f"Prescription issued for {medication_name} to patient ID {identifier}") #This line prints the prescirption issued and the patient ID
        else: #if the patient does not exist
            print("Patient not found") #This line prints patient not found

    def display_prescriptions(self, identifier): #This function displays the prescriptions of the specific patient
        identifier = int(identifier) #This line converts it to an integer
        if identifier in self.prescription_stack: #This line checks if prescriptions exist for the given patient identifier in the prescription stack
            print(f"Prescriptions for patient ID {identifier}:") #This line prints the prescription for the specific ID
            for prescription in self.prescription_stack[identifier]:#This line iterates over each prescription for the patient and print them
                print("- ", prescription) #This line prints the prescription
        else: #if the patient does not exist
            print("No prescriptions found for the patient") #This line prints no prescription found for the patient

    def process_prescriptions(self): #This function processes the prescriptions of all the patients
        for identifier, prescriptions in self.prescription_stack.items(): #This line iterates over each patient identifier and their corresponding prescriptions in the prescription stack
            patient_record = self.patient_records.get(identifier) #This line retrieve the patient record from the patient records dictionary using the identifier
            if patient_record:#This line checks if the patient record exists
                print(f"Issuing prescriptions for {patient_record.first_name} {patient_record.last_name}:") #This line prints the issued prescprtions for all pateints
                for prescription in prescriptions:#This line iterates over each prescription for the patient
                    print("- ", prescription) #This line prints the prescriptions
                print("\n")
            else: #if the patient does not exist
                print(f"Patient with ID {identifier} not found") #This prints that the specif patient is not found

    def display_prescriptions_option(self): #This function displays the prespction option for patient
        identifier = input("Enter patient's identifier: ") #This line asks the patient to enter the identifeir
        self.display_prescriptions(identifier) #This line calls the display_prescriptions method with the entered identifier


def main():
    # Create a doctor's schedule
    doctor_name = "Dr. Andrew" #This line creates a docotr name
    doctor_schedule = DoctorSchedule(doctor_name) #This line creates a doctor schedule object
    hospital.add_doctor(Doctor(doctor_name, doctor_schedule))
    doctor_schedule.add_slot("2024-03-27", "09:00") #This line adds a data and time to the doctor's schedule by .add_slot
    doctor_schedule.add_slot("2024-03-27", "10:00") #This line adds a data and time to the doctor's schedule by .add_slot
    doctor_schedule.add_slot("2024-03-27", "11:00") #This line adds a data and time to the doctor's schedule by .add_slot
    doctor_schedule.add_slot("2024-03-28", "09:00") #This line adds a data and time to the doctor's schedule by .add_slot
    doctor_schedule.add_slot("2024-03-28", "10:00") #This line adds a data and time to the doctor's schedule by .add_slot

    # Initialize the registration system
    registration_system = RegistrationSystem() #This line creates a registration system object

    # Initialize the patient booking system
    booking_system = PatientBookingSystem(doctor_schedule) #This line creates a patient booking system
    identifier = len(registration_system.patient_records) + 1 #This line gets the next patient identifier

    registration_system = RegistrationSystem() #This line creates a new registration system object

    while True: #The main program loop to repeatedly display the menu and handle user input
        print("\nWelcome to the Patient Registration System Menu:") #This line prints a welcoming meesage to display the registration menu
        print("1. Register Patient") #This line prints the register patient option
        print("2. Sort Patients by Admission Date") #This line prints the Sort Patients by Admission Date option
        print("3. Undo Last Registration") #This line prints the Undo last registration option
        print("4. Process Print Jobs") #This line prints the process Print Jobs option
        print("5. Retrieve Patient Information") #This line prints the retrieve patient info option
        print("6. Update Patient Information") #This line prints the update patient info option
        print("7. Cancel Patient Registration") #This line prints the cancel patient registrtion option
        print("8. Display Doctor's Schedule") #This line prints the display doctor schedule option
        print("9. Book a Slot") #This line prints the book a slot option
        print("10. Display Consultation Queue") #This line prints the display consulation queue option
        print("11. Issue Prescription") #This line prints the issue prescription option
        print("12. Display Prescriptions") #This line prints the display prescprition option
        print("13. Process Prescriptions") #This line prints the process prescrition option
        print("14. Exit") #This line prints the exit option
        choice = input("Enter your choice: ") #This line defines a variable choice which asks the use to input their choice

        if choice == "1": #if the user chooses the 1 choice
            first_name = input("Enter patient's first name: ") #This line asks the patient for the first name
            last_name = input("Enter patient's last name: ") #This line asks the patient for the last name
            age = input("Enter patient's age: ") #This line asks the patient for the age
            gender = input("Enter patient's gender: ") #This line asks the patient for the gender
            height = input("Enter patient's height: ") #This line asks the patient for the height
            weight = input("Enter patient's weight: ") #This line asks the patient for the weight
            phonenumber = input("Enter patient's Phone number: ") #This line asks the patient for the phone number
            email = input("Enter patient's email: ") #This line asks the patient for the email
            admission_date = input("Enter admission date (YYYY-MM-DD): ") #This line asks the patient for the admission date
            registration_system.register_patient(first_name, last_name, age, gender, height, weight, phonenumber, email, admission_date) #This line registers a new patient with provided details

        elif choice == "2":# else if the user chooses the 2 choice
            sorted_patients = registration_system.sort_patients_by_admission_date() #This line sorts patients by admission date bu using sort_patients_by_admission_date() method
            print("\nPatients sorted by admission date:") #This line prints Patients sorted by admission date:
            for patient in sorted_patients:#This line iterates over the sorted patients
                print(f"{patient.first_name} {patient.last_name} (Admission Date: {patient.admission_date})") #This line prints the sorted patients with their admission dates

        elif choice == "3":#else if the user chooses the 3 choice
            registration_system.undo_registration() #This line undos the last patient registration by using undo_registration() method

        elif choice == "4":#else if the user chooses the 4 choice
            registration_system.process_print_jobs() #This line processes print jobs by using process_print_jobs() method

        elif choice == "5": #else if the user chooses the 5 choice
            identifier = input("Enter patient's identifier: ") #This line asks the user to enter patient's identifier
            registration_system.retrieve_patient_info(identifier) #This line retrieves the patient informaiton by using retrieve_patient_info(identifier) method

        elif choice == "6":#else if the user chooses the 6 choice
            identifier = input("Enter patient's identifier: ") #This line asks the user for the identifier
            first_name = input("Enter updated first name: ") #This line asks the user for the updated first name
            last_name = input("Enter updated last name: ") #This line asks the user for the updated last name
            age = input("Enter updated patient's age: ") #This line asks the user for the updated age
            gender=input("Enter updated patient's gender: ") #This line asks the user for the updated gender
            height = input("Enter updated patient's height: ") #This line asks the user for the updated height
            weight = input("Enter updated patient's weight: ") #This line asks the user for the updated weight
            phonenumber = input("Enter updated patient's Phone number: ") #This line asks the user for the updated phone number
            email = input("Enter updated patient's email: ") #This line asks the user for the updated email
            registration_system.update_patient_info(first_name, last_name, age, gender, height, weight, phonenumber, email, identifier) #This line updates the patient information

        elif choice == "7":#else if the user chooses the 7 choice
            registration_system.discharge_patient(identifier)  # Call the method to discharge the patient

        elif choice == "8":#else if the user chooses the 8 choice
           doctor_schedule.display_schedule() #This line displays the schedule of the chosne docotor
        elif choice == "9":#else if the user chooses the 9 choice
            doctor_name = input("Enter doctor's name: ") #This line asks the user for the doctor name
            if doctor_name in hospital.doctors:#This line checks if the doctor name is in the hospital
                date = input("Enter the date (YYYY-MM-DD): ") #This line asks the user to input the date of appointment
                time = input("Enter the time (HH:MM): ") #This line asks the user to input the time of appointment
                patient_name = input("Enter patient's name: ") #This line asks the user for the name
                patient_id = input("Enter patient's ID: ") #This line asks the user for the ID
                booking_system.book_slot(date, time, doctor_name, patient_name, patient_id)#This line uses book_slot method and books the slot based on the inputs
            else:#if the doctor does not exist
                print("Doctor not found.")#This line prints doctor not found

        elif choice == "10":#else if the user chooses the 10 choice
            registration_system.display_consultation_queue() #This line displays the consulation queue by using display_consultation_queue() method

        elif choice == "11":#else if the user chooses the 11 choice
                identifier = input("Enter patient's identifier: ") #This line asks the user for the identiifer
                medication_name = input("Enter medication name: ") #This line asks the user for the medication name
                registration_system.issue_prescription(identifier, medication_name) #This line issues the prescprition by using issue_prescription(identifier, medication_name) method

        elif choice == "12":#else if the user chooses 12 choice
            registration_system.display_prescriptions_option() #This line displays the prescritpion for the chosen patient
        elif choice == "13":#else if the user chooses 13 choice
            registration_system.process_prescriptions() #This line processes the prescritpion for all patietns by using process_prescriptions()
        elif choice == "14":#else if the user chooses the 14 choice
            print("Exiting program. Goodbye!")#This line prints a goodbye message to exit the progoram
            break#This line stops by using break

        else:#else the user chooses none of these
            print("Invalid choice. Please enter a valid option.")#this line prints invalid choice

if __name__ == "__main__": #This line checks if the current script is being run directly
    main() #This line calls the main function to start the program