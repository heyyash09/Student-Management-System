import json
import os

DATA_FILE = os.path.join("data", "students.json")


def load_students():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        return []


def save_students(students):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)
    print("\nData saved successfully.")


def get_marks():
    marks = []
    subjects = ["Subject 1", "Subject 2", "Subject 3", "Subject 4", "Subject 5"]

    for subject in subjects:
        while True:
            try:
                mark = float(input(f"Enter marks for {subject} (0-100): "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
    return marks


def calculate_result(marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"

    status = "Pass" if average >= 40 else "Fail"
    return total, average, grade, status


def find_student(students, student_id):
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def add_student(students):
    print("\n--- Add Student ---")
    student_id = input("Enter Student ID: ").strip()

    if find_student(students, student_id):
        print("A student with this ID already exists.")
        return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    course = input("Enter Course: ").strip()
    marks = get_marks()

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.")


def display_student(student):
    total, average, grade, status = calculate_result(student["marks"])

    print("\n------------------------------")
    print(f"ID       : {student['id']}")
    print(f"Name     : {student['name']}")
    print(f"Age      : {student['age']}")
    print(f"Course   : {student['course']}")
    print(f"Marks    : {student['marks']}")
    print(f"Total    : {total:.2f}")
    print(f"Average  : {average:.2f}")
    print(f"Grade    : {grade}")
    print(f"Status   : {status}")
    print("------------------------------")


def view_students(students):
    print("\n--- All Students ---")
    if not students:
        print("No student records found.")
        return

    for student in students:
        display_student(student)


def search_student(students):
    print("\n--- Search Student ---")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if student:
        display_student(student)
    else:
        print("Student not found.")


def update_student(students):
    print("\n--- Update Student ---")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    print("Press Enter to keep the existing value.")
    name = input(f"Name [{student['name']}]: ").strip()
    age = input(f"Age [{student['age']}]: ").strip()
    course = input(f"Course [{student['course']}]: ").strip()

    if name:
        student["name"] = name
    if age:
        student["age"] = age
    if course:
        student["course"] = course

    change_marks = input("Do you want to update marks? (y/n): ").strip().lower()
    if change_marks == "y":
        student["marks"] = get_marks()

    save_students(students)
    print("Student updated successfully.")


def delete_student(students):
    print("\n--- Delete Student ---")
    student_id = input("Enter Student ID: ").strip()
    student = find_student(students, student_id)

    if not student:
        print("Student not found.")
        return

    students.remove(student)
    save_students(students)
    print("Student deleted successfully.")


def show_top_student(students):
    if not students:
        print("\nNo student records found.")
        return

    top = max(students, key=lambda student: calculate_result(student["marks"])[1])
    print("\n--- Student with Highest Average ---")
    display_student(top)


def show_lowest_student(students):
    if not students:
        print("\nNo student records found.")
        return

    lowest = min(students, key=lambda student: calculate_result(student["marks"])[1])
    print("\n--- Student with Lowest Average ---")
    display_student(lowest)


def main():
    students = load_students()

    while True:
        print("\n====================================")
        print("      STUDENT MANAGEMENT SYSTEM")
        print("====================================")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Find Top Student")
        print("7. Find Lowest Student")
        print("8. Save Data")
        print("9. Exit")
        print("====================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            show_top_student(students)
        elif choice == "7":
            show_lowest_student(students)
        elif choice == "8":
            save_students(students)
        elif choice == "9":
            save_students(students)
            print("Thank you for using Student Management System.")
            break
        else:
            print("Invalid choice. Please select a number from 1 to 9.")


if __name__ == "__main__":
    main()
