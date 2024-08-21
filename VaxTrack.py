import datetime
class Child:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        self.vaccination_records = []
    def add_vaccination(self, vaccine_name, date):
        self.vaccination_records.append((vaccine_name, date))
class VaccinationSystem:
    def __init__(self):
        self.children = []
    def add_child(self, name, dob):
        try:
            datetime.datetime.strptime(dob, "%d-%m-%Y")  # Validates the date format
            child = Child(name, dob)
            self.children.append(child)
            print(f"\nChild '{name}' added successfully!")
        except ValueError:
            print("\nInvalid date format! Please enter the date in DD-MM-YYYY format.")
    def book_appointment(self, child_name, vaccine_name, date):
        child = self.find_child(child_name)
        if child:
            try:
                datetime.datetime.strptime(date, "%d-%m-%Y")  # Validates the date format
                child.add_vaccination(vaccine_name, date)
                print(f"\nAppointment booked for {child_name} on {date} for vaccine '{vaccine_name}'")
            except ValueError:
                print("\nInvalid date format! Please enter the date in DD-MM-YYYY format.")
        else:
            print(f"\nChild '{child_name}' not found!")
    def view_appointments(self, child_name):
        child = self.find_child(child_name)
        if child:
            print(f"\nAppointments for {child.name}:")
            if child.vaccination_records:
                for record in child.vaccination_records:
                    print(f"Vaccine: {record[0]}, Date: {record[1]}")
            else:
                print("No appointments found.")
        else:
            print(f"\nChild '{child_name}' not found!")
    def view_reminders(self):
        today = datetime.date.today()
        print("\nUpcoming Vaccination Reminders:")
        found_reminder = False
        for child in self.children:
            for record in child.vaccination_records:
                vaccine_date = datetime.datetime.strptime(record[1], "%d-%m-%Y").date()
                days_difference = (vaccine_date - today).days
                if 0 <= days_difference <= 7:
                    print(f"Reminder: {child.name} - {record[0]} on {record[1]}")
                    found_reminder = True
        if not found_reminder:
            print("No reminders for the upcoming 7 days.")
    def find_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None
def main():
    print("Welcome to VaxTrack - Your Child Vaccination Management System")
    system = VaccinationSystem()
    while True:
        print("\n1. Add Child")
        print("2. Book Appointment")
        print("3. View Appointments")
        print("4. View Reminders")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            name = input('Enter child’s name: ')
            dob = input("Enter date of birth (DD-MM-YYYY): ")
            system.add_child(name, dob)
        elif choice == '2':
            name = input('Enter child’s name: ')
            vaccine = input("Enter vaccine name: ")
            date = input("Enter appointment date (DD-MM-YYYY): ")
            system.book_appointment(name, vaccine, date)
        elif choice == '3':
            name = input('Enter child’s name: ')
            system.view_appointments(name)
        elif choice == '4':
            system.view_reminders()
        elif choice == '5':
            print("\nThank you for using VaxTrack. Stay safe and healthy!")
            break
        else:
            print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()
