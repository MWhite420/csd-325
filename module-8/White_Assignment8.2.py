#Mark White
#CSD325
#Assignment8.2


import json


# Define the Student class
class Student:

    def __init__(self, F_Name, L_Name, Student_ID, Email):
        self.F_Name = F_Name
        self.L_Name = L_Name
        self.Student_ID = Student_ID
        self.Email = Email

    def __repr__(self):
        return f"{self.F_Name} , {self.L_Name} : ID = {self.Student_ID} , Email = {self.Email}"


# Function to load students from a JSON file
def load_students(filename):
    try:

        with open(filename, 'r') as file:
            data = json.load(file)
            return [Student(**student) for student in data]
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []


# Function to print the list of students
def print_students(students, message):
    print(message)
    for student in students:
        print(student)


# Function to save updated student list to JSON file
def save_students(students, filename):
    with open(filename, 'w') as file:
        # Convert Student objects to dictionaries
        json.dump([student.__dict__ for student in students], file, indent=4)


def main():
    filename = 'student.json'
    # Load the original list of students
    students = load_students(filename)

    # Print the original student list
    print_students(students, "Original Student List:")

    # Add a new student
    new_student = Student(F_Name='Mark',
                          L_Name='White',
                          Student_ID=21083,
                          Email='m_white@fictional.com')
    students.append(new_student)

    # Print the updated student list
    print_students(students, "\nUpdated Student List:")

    # Save the updated list back to the JSON file
    save_students(students, filename)
    print("The JSON file has been updated.")


if __name__ == "__main__":
    main()


#References:
    #https://www.geeksforgeeks.org/file-handling-python/
    #https://howtodoinjava.com/python-json/append-json-to-file/
    #https://oxylabs.io/blog/python-parse-json
