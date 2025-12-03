# Name: Aishani Das
# Date: 09-11-2025
# Experiment Title: Student Marks Analyzer

import csv


def enter_marks_manually():
    students = {}
    n = int(input("Enter number of students: "))
    for i in range(n):
        name = input(f"Enter name of student {i+1}: ")
        marks = float(input(f"Enter marks of {name}: "))
        students[name] = marks
    return students


def read_from_csv():
    students = {}
    filename = input("Enter CSV file name (with .csv): ")
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # skip header if present
        for row in reader:
            if len(row) >= 2:
                name, marks = row[0], float(row[1])
                students[name] = marks
    return students


def analyze(students):
    if not students:
        print("No data available.")
        return
    marks = list(students.values())
    top_score = max(marks)
    avg_score = sum(marks) / len(marks)
    pass_count = sum(1 for m in marks if m >= 40)
    fail_count = len(marks) - pass_count
    print("\n--- Statistical Analysis ---")
    print(f"Top Score: {top_score}")
    print(f"Average Score: {avg_score:.2f}")
    print(f"Pass Count: {pass_count}")
    print(f"Fail Count: {fail_count}")


def assign_grades(students):
    grades = {}
    for name, marks in students.items():
        if marks >= 90:
            grade = 'A'
        elif marks >= 80:
            grade = 'B'
        elif marks >= 70:
            grade = 'C'
        elif marks >= 60:
            grade = 'D'
        else:
            grade = 'F'
        grades[name] = grade
    return grades


def pass_fail_summary(students):
    passed = [name for name, marks in students.items() if marks >= 40]
    failed = [name for name, marks in students.items() if marks < 40]
    print("\n--- Pass/Fail Summary ---")
    print("Passed Students:", ', '.join(passed) if passed else "None")
    print("Failed Students:", ', '.join(failed) if failed else "None")


def display_results(students, grades):
    print("\nName\t\tMarks\tGrade")
    print("-------------------------------")
    for name, marks in students.items():
        print(f"{name}\t\t{marks}\t{grades[name]}")


def main():
    print("Welcome to the Student Marks Analyzer\n")
    while True:
        print("\nMenu:")
        print("1. Enter student marks manually")
        print("2. Read marks from CSV file")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            students = enter_marks_manually()
        elif choice == '2':
            students = read_from_csv()
        elif choice == '3':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice.")
            continue

        analyze(students)
        grades = assign_grades(students)
        pass_fail_summary(students)
        display_results(students, grades)

        repeat = input("\nDo you want to run again? (y/n): ")
        if repeat.lower() != 'y':
            break


if __name__ == "__main__":
    main()
    