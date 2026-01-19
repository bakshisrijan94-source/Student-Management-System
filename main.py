students = {}

def add_student():
    roll = input("Enter Roll No: ")
    name = input("Enter Name: ")
    students[roll] = name
    print("Student Added Successfully")

def view_students():
    for roll, name in students.items():
        print(roll, ":", name)

while True:
    print("1.Add Student")
    print("2.View Students")
    print("3.Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
