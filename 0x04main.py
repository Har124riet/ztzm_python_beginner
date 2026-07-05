students = []

while (name := input("Enter name (or 'done'): ")) != "done":
    score = float(input("Score: "))

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

    students.append((name, score, grade))

print("\n--- Report ---")

for name, score, grade in students:
    print(f"{name}: {score}, {grade}")

