print("=== Student Grading System ===")

students = {}

while True:
    name = input("\nEnter student name (or type 'done' to finish): ")

    if name.lower() == "done":
        break

    score = int(input("Enter score: "))

    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"

    students[name] = {
        "Score": score,
        "Grade": grade
    }

print("\n===== STUDENT REPORT =====")

for name, details in students.items():
    print(f"Name: {name}")
    print(f"Score: {details['Score']}")
    print(f"Grade: {details['Grade']}")
    print("-" * 20)

print(f"Total Students: {len(students)}")