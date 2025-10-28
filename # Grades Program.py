# Grades Program

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
grades = [75, 82, 59, 90, 67]

total = 0
for g in grades:
    total = total + g

average = total / len(grades)
print("Average of all students:", average)

passed = 0
failed_students = []

for i in range(len(grades)):
    if grades[i] >= 60:
        passed = passed + 1
    else:
        failed_students.append(students[i])

percentage = (passed / len(grades)) * 100
print("Percentage of students who passed:", percentage)
print("Students who failed:", failed_students)

