class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        return {"Name": self.name, "Age": self.age}


class StudentGrades(Student):
    def __init__(self, student):
        super().__init__(student.name, student.age)
        # BTW I used AI to help build this project
        self.grades = []

    def add_grade(self, name, grade):
        if is_duplicate_subject(self.grades, name):
            return f"{name} is already added"
        self.grades.append({"Name": name, "Grade": grade})
        return "Success"

    def get_grade(self, name):
        for g in self.grades:
            if g["Name"] == name:
                return g["Grade"]
        return None

    def get_all_grades(self):
        return {"Name": self.name, "Grades": self.grades}

    def get_average(self):
        return calculate_average(self.grades)


class School:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.students = []

    def info(self):
        # BTW I used AI to help build this project
        return {
            "Name": self.name,
            "Type": get_school_type_name(self.type),
            "Students": len(self.students),
        }

    def add_student(self, student):
        for s in self.students:
            if s.name == student.name:
                return "Student already exists"
        self.students.append(student)
        return "Added Successfully"

    def get_student_by_name(self, name):
        for s in self.students:
            if s.name == name:
                return s
        return None


schools = []


# ---------- pure / testable functions (required by CS50P: top-level, not I/O) ----------

def calculate_average(grades):
    """Return the average of a list of {"Name":..., "Grade":...} dicts, or 0 if empty."""
    if len(grades) == 0:
        return 0
    total = 0
    for g in grades:
        total += g["Grade"]
    return total / len(grades)


def is_duplicate_subject(grades, name):
    """Return True if a subject with this name already exists in the grades list."""
    for g in grades:
        if g["Name"] == name:
            return True
    return False


def get_school_type_name(type_number):
    """Map a school type number (1/2/3) to its readable name."""
    # BTW I used AI to help build this project
    types = {1: "Primary", 2: "Secondary", 3: "Both"}
    return types.get(type_number, "Unknown")


def parse_number(text):
    """Convert a string to an int, or return None if it isn't a valid whole number."""
    if not text.isdigit():
        return None
    return int(text)


# ---------- input / output helpers ----------

def show(message):
    print()
    print(message)


def get_input(message):
    return input(message)


def get_number(message):
    data = get_input(message)
    result = parse_number(data)
    if result is None:
        show("Please enter a number")
    return result


# ---------- picking helpers ----------

def school_pick():
    if len(schools) == 0:
        show("No schools available")
        return None
    show("Schools:")
    for i in range(len(schools)):
        print(f"press {i + 1} for {schools[i].name}")
    choice = get_number("Enter your input: ")
    if choice is None:
        return None
    if choice < 1 or choice > len(schools):
        show("Invalid school number")
        return None
    return schools[choice - 1]


def student_pick():
    school = school_pick()
    if school is None:
        return None
    name = get_input("Enter the student name: ")
    student = school.get_student_by_name(name)
    if student is None:
        show("Student not found")
        return None
    return student


# ---------- school operations ----------

def create_school():
    name = get_input("Enter the school name: ")
    type_choice = get_number("Enter the type (1 Primary, 2 Secondary, 3 Both): ")
    if type_choice is None:
        return
    if type_choice not in (1, 2, 3):
        show("Invalid school type")
        return
    school = School(name, type_choice)
    schools.append(school)
    show("Created Successfully")


def show_schools():
    if len(schools) == 0:
        show("No schools available")
        return
    show("Schools:")
    for school in schools:
        print(school.info())


def create_student():
    school = school_pick()
    if school is None:
        return
    name = get_input("Enter the student name: ")
    age = get_number("Enter the student age: ")
    if age is None:
        return
    base_student = Student(name, age)
    student = StudentGrades(base_student)
    result = school.add_student(student)
    show(result)


def show_students():
    school = school_pick()
    if school is None:
        return
    if len(school.students) == 0:
        show("No students in this school")
        return
    show(f"Students of {school.name}:")
    for student in school.students:
        print(student.info())


# ---------- student / grade operations ----------

def add_grade():
    student = student_pick()
    if student is None:
        return
    name = get_input("Enter the subject name: ")
    grade = get_number("Enter the grade: ")
    if grade is None:
        return
    result = student.add_grade(name, grade)
    show(result)


def show_grades():
    student = student_pick()
    if student is None:
        return
    data = student.get_all_grades()
    if len(data["Grades"]) == 0:
        show(f"{student.name} has no grades yet")
        return
    show(f"Grades of {student.name}:")
    for g in data["Grades"]:
        print(g)


def show_average():
    student = student_pick()
    if student is None:
        return
    average = student.get_average()
    show(f"The average of {student.name} is {average}")


# ---------- menus ----------

def menu_school():
    show("School inputs")
    print("press 1 to create school")
    print("press 2 to show all schools")
    print("press 3 to create student in a school")
    print("press 4 to show the students of a school")
    print("press 0 to go back")
    choice = get_number("Enter your input: ")
    if choice is None:
        return
    if choice == 1:
        create_school()
    elif choice == 2:
        show_schools()
    elif choice == 3:
        create_student()
    elif choice == 4:
        show_students()
    elif choice == 0:
        return
    else:
        show("Invalid choice")


def menu_student():
    show("Student inputs")
    print("press 1 to add a grade")
    print("press 2 to show all the grades")
    print("press 3 to show the average of the grades")
    print("press 0 to go back")
    choice = get_number("Enter your input: ")
    if choice is None:
        return
    if choice == 1:
        add_grade()
    elif choice == 2:
        show_grades()
    elif choice == 3:
        show_average()
    elif choice == 0:
        return
    else:
        show("Invalid choice")


def main():
    while True:
        show("Hi User select what do you want to do")
        print("For School inputs press 1")
        print("For Student inputs press 2")
        print("To exit press 0")
        # BTW I used AI to help build this project
        choice = get_number("Enter your input: ")
        if choice is None:
            continue
        if choice == 1:
            menu_school()
        elif choice == 2:
            menu_student()
        elif choice == 0:
            show("Bye")
            break
        else:
            show("Invalid choice")


if __name__ == "__main__":
    main()
