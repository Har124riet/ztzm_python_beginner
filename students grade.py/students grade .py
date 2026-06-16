Students = { }

while (name := input("Enter name (or 'done'): ")) != 'done':
    score = float(input("score:"))
    grade = ('F','D','C','B','A')[min(int(score//10),4)]

    Students.append((name,score,grade))

    print("/n--- Report --")
    for name, score, grade in Students:
        print(f"{name}:{score},{grade}")

