students = []

def add_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")

    marks = []

    for i in range(5):
        mark = float(input("Enter marks of subject " + str(i+1) + ": "))
        marks.append(mark)

    total = sum(marks)
    percentage = total / 5

    if percentage >= 90:
        grade = "A+"
    elif percentage >= 80:
        grade = "A"
    elif percentage >= 70:
        grade = "B"
    elif percentage >= 60:
        grade = "C"
    elif percentage >= 40:
        grade = "D"
    else:
        grade = "Fail"

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade
    }

    students.append(student)

    print("\nStudent Added Successfully!")


def display_students():
    if len(students) == 0:
        print("No student records found.")
    else:
        for s in students:
            print("\n----------------------")
            print("Roll Number:", s["roll"])
            print("Name:", s["name"])
            print("Marks:", s["marks"])
            print("Total:", s["total"], "/ 500")
            print("Percentage:", s["percentage"], "%")
            print("Grade:", s["grade"])


def search_student():
    roll = int(input("Enter Roll Number to Search: "))

    found = False

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found!")
            print("Name:", s["name"])
            print("Total:", s["total"])
            print("Percentage:", s["percentage"], "%")
            print("Grade:", s["grade"])
            found = True

    if found == False:
        print("Student Not Found!")


while True:
    print("\n===== STUDENT RESULT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Display All Results")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        display_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")