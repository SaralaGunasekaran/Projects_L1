
students = []

# Function 1: Calculate grade
def calculate_grade(mark):

    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"


# Function 2: Add students
def add_students():

    print("Enter student details (type 'done' to finish)")

    while True:

        name = input("\nEnter student name: ").strip()

        if name.lower() == "done":
            break

        # Validate name
        if not name:
            print("Invalid name! Name cannot be empty.")
            continue

        if not all(char.isalpha() or char.isspace() for char in name):
            print("Invalid name! Enter alphabets only.")
            continue

        # Validate marks
        while True:
            try:
                mark = float(input("Enter marks: "))

                if mark < 0 or mark > 100:
                    print("Invalid marks! Enter marks between 0 and 100.")
                    continue

                break

            except ValueError:
                print("Invalid input! Please enter numeric marks.")

        grade = calculate_grade(mark)

        students.append([name, mark, grade])

        print("Student added successfully!")


# Function 3: Display student table
def display_students():

    #print("\n" + "=" * 45)
    #print("             STUDENT REPORT")
    #print("=" * 45)

    print(f"{'Name':<15}{'Marks':<15}{'Grade':<10}")
    #print("-" * 40)

    for student in students:
        print(f"{student[0]:<15}{student[1]:<15.2f}{student[2]:<10}")

    #print("-" * 40)


# Function 4: Calculate statistics
def calculate_statistics():

    marks = [student[1] for student in students]

    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    print(f"Average: {average:.2f}    Highest: {highest:.2f}    Lowest: {lowest:.2f}")

    #print("=" * 45)


# Function 5: Main function
def main():

    add_students()

    if students:
        display_students()
        calculate_statistics()
    else:
        print("No student records found.")


# Program execution
main()
