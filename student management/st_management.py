import json

class Student:
    next_roll_number = 1
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.roll_number = Student.next_roll_number
        Student.next_roll_number += 1

    #ქულის განახლება
    def update_grade(self, new_grade):
        self.grade = new_grade

     #ლექსიკონად ჩაწერაში გვეხმარება
    def to_dict(self):
        return {
            "roll_number": self.roll_number,
            "name": self.name,
            "grade": self.grade
        }

    def __str__(self):
        return f"Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"


class StudentManagementSystem:
    def __init__(self):
        self.students = {}
        self.deleted_roll_numbers = set()

    #სტუდენტების შენახვა
    def save_students(self):
        try:
            with open("students.json", "w") as file:
                json.dump(
                    [student.to_dict() for student in self.students.values()],
                    file,
                    indent=4
                )
            print("Students saved successfully.")
        except Exception as e:
            print(f"Error while saving students: {e}")

    #ფაილის წაკითხვა
    def load_students(self):
        try:
            with open("students.json", "r") as file:
                data = json.load(file)
                self.students = {student["roll_number"]: Student(student["name"], student["grade"]) for student in data}
                
            print("Students loaded successfully.")
        except FileNotFoundError:
            print("No existing data found.")
        except Exception as e:
            print(f"Error while loading students: {e}")

    #სტუდენტის დამატება
    def add_student(self):
        try:
            name = input("Enter student's name: ")

            #მოწმდება ასოებია თუ არა შეყვანილი
            if not name.isalpha():
                raise ValueError("Name must contain only letters.")
            if len(name) < 3:
                raise ValueError("Name must be at least 3 characters long.")
        
            grade = input("Enter grade (A-F): ").upper()
            #ქულები მოცემულისგან განსხვავებული არ უნდა იყოს
            if grade not in 'ABCDEF':
                raise ValueError("Grade must be A-F.")
            
            #შემდეგი roll number-ის დათვლა
            roll_number = max(self.students.keys(), default=0) + 1
            new_student = Student(name, grade)
            new_student.roll_number = roll_number
            self.students[roll_number] = new_student
            self.save_students()
            print("Student added successfully.")
        except ValueError as e:
            print(f'Error: {e}')

    #სტუდენტების ნახვა
    def view_students(self):
        if len(self.students) != 0:
            print(f'{"Roll Number":>5} {"Name":>15} {"Grade":>19}')
            print("=" * 50)
            for student in self.students.values():
                print(f"{student.roll_number :>6}{student.name :>21}{student.grade :>18}")
        else:
            print("There are no students in the system.")

    #სტუდენტის მოძებნა
    def find_student_with_rollNum(self):
        try:   
            roll_number = int(input("Enter the roll number you want to search: "))
            #ჯსონიდან მოგვაქ სტუდენტი
            student = self.students.get(roll_number)
            if student:
                print(f"Student found: {student}")
            else:
                print("Student not found.")
        except ValueError:
            print("Invalid roll number. Please enter a valid integer.")

    #სტუდენტის წაშლა
    def delete_student(self):
        try:
            roll_number = int(input("Enter roll number of the student to delete: "))
            
            #ხდება ლექსიკონში სტუდენტის მოძებნა და მისი წაშლა 
            if roll_number in self.students:
                del self.students[roll_number]  
                #წაშლილის ნამბერს ვინახავთ სეტში
                self.deleted_roll_numbers.add(roll_number)  
                print(f"Student with roll number {roll_number} deleted successfully.")
                self.update_roll_numbers()  
                self.save_students()
            else:
                print("Student not found.")
        except ValueError:
            print("Invalid roll number. Please enter a valid integer.")

    #რიცხვის განახლება
    def update_roll_numbers(self):
        #იქმნება ახალი ლექსიკონი ნამბერი ხდება 1 და ხდება სტუდენტების გადაწერა ახალ ლექსიკონში
        updated_students = {}
        roll_number = 1
        for student in sorted(self.students.values(), key=lambda x: x.roll_number):
            student.roll_number = roll_number  
            updated_students[roll_number] = student
            roll_number += 1
        
        self.students = updated_students 

    #სტუდენტის ქულის განახლება
    def update_student_grade(self):
        try:
            roll_number = int(input("Enter roll number to update grade: "))
            
            #ჯსონიდან სტუდენტის მიღება
            student = self.students.get(roll_number)
            if student:
                new_grade = input("Enter the new grade (A-F): ").strip().upper()
                #მოწმდება მოცემული ქულებიდან სხვა შეყავთ თუ არა
                if new_grade not in "ABCDEF":
                    print("Invalid grade. Grade must be between A and F.")
                    return
                student.update_grade(new_grade)
                self.save_students()
                print("Grade updated successfully.")
                print(f"Updated Student Details: {student}")
            else:
                print("Student not found.")
        except ValueError:
            print("Invalid input. Please enter a valid roll number.")


system = StudentManagementSystem()
system.load_students()

#აპლიკაციის გაშვება
while True:
    print("1. Add New Student")
    print("2. View All Students")
    print("3. Search Student by Roll Number")
    print("4. Update Student Grade")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        system.add_student()
    elif choice == '2':
        system.view_students()
    elif choice == '3':
        system.find_student_with_rollNum()
    elif choice == '4':
        system.update_student_grade()
    elif choice == '5':
        system.delete_student()
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
