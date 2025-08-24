#comparison operators - compares values and returns either true or false
# == equal to
# != not equal to
# > greater than
# < less than
# >= greater than or equal to
# <= less than or equal to

# output is true
a = 5
b = 5
print(a == b)

# output is false
a = 5
b = 6
print(a == b)   

# output is true
a = 5
b = 6
print(a != b)

# output is false
a = 5
b = 5
print(a != b)

# output is true
a = 5
b = 6
print(a < b)

# output is false
a = 5
b = 5
print(a < b)

# output is true
a = 6
b = 5
print(a > b)

# output is false   
a = 5
b = 5
print(a > b)

# output is true
a = 5
b = 5
print(a >= b)

# output: True
a = 3
b = 5
print(a <= b)

age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

def evaluate_student_performance(score, attendance_percent, submitted_assignments, total_assignments):
    # Equal to (==) and Not equal to (!=)
    if score == 100:
        print("Perfect score!")
    elif score != 0:
        print(f"Score: {score}/100")
    else:
        print("No score recorded")
    
    # Greater than (>) and Less than (<)
    if attendance_percent > 90:
        print("Excellent attendance!")
    elif attendance_percent < 60:
        print("Poor attendance - needs improvement")
    
    # Greater than or equal to (>=)
    if submitted_assignments >= total_assignments:
        print("All assignments completed!")
    
    # Less than or equal to (<=)
    assignment_percentage = (submitted_assignments / total_assignments) * 100
    if assignment_percentage <= 50:
        print("Warning: Less than half of assignments submitted")
    
    # Multiple comparisons using 'and'
    if score >= 70 and attendance_percent >= 80:
        print("Good standing in class")
    
    # Multiple comparisons using 'or'
    if score < 60 or attendance_percent < 70:
        print("Student needs support")
    
    # Chained comparisons
    if 60 <= score <= 70:
        print("Score is in the D grade range")
    elif 70 < score <= 80:
        print("Score is in the C grade range")
    elif 80 < score <= 90:
        print("Score is in the B grade range")
    elif 90 < score <= 100:
        print("Score is in the A grade range")
    
    # in and not in operators (using a list of passing grades)
    passing_grades = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    if score in passing_grades:
        print("Student is passing")
    if score not in passing_grades:
        print("Student is not passing")

# Test the function with different scenarios
print("=== Student 1 ===")
evaluate_student_performance(95, 98, 10, 10)

print("\n=== Student 2 ===")
evaluate_student_performance(65, 55, 5, 10)

print("\n=== Student 3 ===")
evaluate_student_performance(85, 85, 9, 10)

print("\n=== Student 4 ===")
evaluate_student_performance(100, 100, 10, 10)