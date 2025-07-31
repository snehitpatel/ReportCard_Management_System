from tabulate import tabulate  # Import the tabulate library

class StudentReportCardSystem:
    def __init__(self):
        self.students = {}  # Dictionary to store student records

    def add_student(self):
        """Add a new student record."""
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                print(f"Error: Student ID {student_id} already exists.")
            else:
                name = input("Enter Student Name: ")
                self.students[student_id] = {"name": name, "subjects": {}, "marks": {}}
                print(f"Student {name} added successfully.")
        except ValueError:
            print("Error: Invalid input. Student ID must be a number.")

    def update_student(self):
        """Update a student's name."""
        try:
            student_id = int(input("Enter Student ID to update: "))
            if student_id in self.students:
                new_name = input("Enter New Name: ")
                self.students[student_id]["name"] = new_name
                print(f"Student ID {student_id} updated to {new_name}.")
            else:
                print(f"Error: Student ID {student_id} not found.")
        except ValueError:
            print("Error: Invalid input. Student ID must be a number.")

    def delete_student(self):
        """Delete a student record."""
        try:
            student_id = int(input("Enter Student ID to delete: "))
            if student_id in self.students:
                del self.students[student_id]
                print(f"Student ID {student_id} deleted successfully.")
            else:
                print(f"Error: Student ID {student_id} not found.")
        except ValueError:
            print("Error: Invalid input. Student ID must be a number.")

    def assign_subject(self):
        """Assign a subject to a student."""
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                subject = input("Enter Subject Name: ")
                self.students[student_id]["subjects"][subject] = None
                print(f"Subject {subject} assigned to Student ID {student_id}.")
            else:
                print(f"Error: Student ID {student_id} not found.")
        except ValueError:
            print("Error: Invalid input. Student ID must be a number.")

    def input_marks(self):
        """Input marks for a subject."""
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                subject = input("Enter Subject Name: ")
                if subject in self.students[student_id]["subjects"]:
                    marks = float(input(f"Enter Marks for {subject}: "))
                    if 0 <= marks <= 100:
                        self.students[student_id]["marks"][subject] = marks
                        print(f"Marks for {subject} added to Student ID {student_id}.")
                    else:
                        print("Error: Marks must be between 0 and 100.")
                else:
                    print(f"Error: Subject {subject} not assigned to Student ID {student_id}.")
            else:
                print(f"Error: Student ID {student_id} not found.")
        except ValueError:
            print("Error: Invalid input. Marks must be a number.")

    def calculate_grade(self, marks):
        """Calculate grade based on marks."""
        if marks >= 90:
            return "A+"
        elif marks >= 80:
            return "A"
        elif marks >= 70:
            return "B"
        elif marks >= 60:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    def generate_report_card(self):
        """Generate a report card for a student in tabular form."""
        try:
            student_id = int(input("Enter Student ID: "))
            if student_id in self.students:
                student = self.students[student_id]
                print("\n--- Report Card ---")
                print(f"Student ID: {student_id}")
                print(f"Name: {student['name']}")

                # Prepare data for the table
                table_data = []
                total_marks = 0
                for subject, marks in student["marks"].items():
                    grade = self.calculate_grade(marks)
                    table_data.append([subject, marks, grade])
                    total_marks += marks

                # Display the table using tabulate
                headers = ["Subject", "Marks", "Grade"]
                print(tabulate(table_data, headers=headers, tablefmt="grid"))

                if student["marks"]:
                    print(f"\nTotal Marks: {total_marks}")
                    print(f"Overall Grade: {self.calculate_grade(total_marks / len(student['marks']))}")
                else:
                    print("No marks available.")
                print("-------------------\n")
            else:
                print(f"Error: Student ID {student_id} not found.")
        except ValueError:
            print("Error: Invalid input. Student ID must be a number.")

    def view_class_performance(self):
        """View overall class performance."""
        if not self.students:
            print("No students found.")
            return

        print("\n--- Class Performance ---")
        for student_id, student in self.students.items():
            total_marks = sum(student["marks"].values())
            avg_marks = total_marks / len(student["marks"]) if student["marks"] else 0
            print(f"Student ID: {student_id}, Name: {student['name']}, Average Marks: {avg_marks:.2f}, Overall Grade: {self.calculate_grade(avg_marks)}")
        print("-------------------------\n")


# Main Menu
def main_menu():
    system = StudentReportCardSystem()
    while True:
        print("\n--- Student Report Card System ---")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. Assign Subject")
        print("5. Input Marks")
        print("6. Generate Report Card")
        print("7. View Class Performance")
        print("8. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.update_student()
        elif choice == "3":
            system.delete_student()
        elif choice == "4":
            system.assign_subject()
        elif choice == "5":
            system.input_marks()
        elif choice == "6":
            system.generate_report_card()
        elif choice == "7":
            system.view_class_performance()
        elif choice == "8":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main_menu()