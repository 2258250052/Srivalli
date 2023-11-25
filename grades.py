def calculate_grade(grades):
    total_points = sum(grades)
    total_subjects = len(grades)
    overall_grade = total_points / total_subjects
    return overall_grade

grades = []

for i in range(6):
    semester_grades = []
    print(f"Enter grades for semester {i + 1}:")
    
    for j in range(5):  
        grade = float(input(f"Enter grade {j + 1}: "))
        semester_grades.append(grade)
    
    grades.append(calculate_grade(semester_grades))

overall_grade = calculate_grade(grades)
print(f"Overall grade based on 6 semesters: {overall_grade}")
