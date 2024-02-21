def calculate_final_mark(coursework_marks, coursework_weights):
    total_mark = 0
    num_coursework = len(coursework_marks)

    for i in range(num_coursework):
        # Calculate weighted mark for each coursework
        weighted_mark = coursework_marks[i] * coursework_weights[i]
        total_mark += weighted_mark

    return total_mark


def calculate_grade(final_mark):
    if final_mark >= 90:
        return "A*"
    elif 80 <= final_mark < 90:
        return "A"
    elif 70 <= final_mark < 80:
        return "B"
    elif 60 <= final_mark < 70:
        return "C"
    elif 50 <= final_mark < 60:
        return "D"
    else:
        return "F"


def main():
    module_name = input("Enter the module name: ")
    num_students = int(input("Enter the number of students: "))
    num_coursework = int(input("Enter the number of coursework: "))

    # Initialize empty lists for coursework weights and marks
    coursework_weights = []

    # Input coursework weights
    for i in range(num_coursework):
        weight = float(input(f"Enter weight for coursework {i + 1} (in percentage): "))
        coursework_weights.append(weight / 100)

    # Input coursework details for each student
    for student in range(num_students):
        print(f"\nEnter details for Student {student + 1}:")
        student_marks = []

        for i in range(num_coursework):
            mark = float(input(f"Enter mark for coursework {i + 1} (out of 100): "))
            student_marks.append(mark)

        # Calculate final mark for each student
        final_mark = calculate_final_mark(student_marks, coursework_weights)

        # Calculate and display grade
        grade = calculate_grade(final_mark)
        print(f"\nFinal mark for Student {student + 1} in {module_name}: {final_mark:.2f} (Grade: {grade})")


if __name__ == "__main__":
    main()
