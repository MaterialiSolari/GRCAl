import math

homework_max = 800.0
quizzes_max = 400.0
midterm_max = 150.0
final_max = 200.0

#Write a program to calculate a course grade given points for homework,
#quizzes, midterm exam, and final exam. Grades are calculated differently
#for undergrads, grads and distance learners.
student_status = input('Student status:')

#input student status (str). If input is not one of "UG" (undergrad), "G" (grad), or "DL" (distance learner)
if student_status not in ['UG', 'G', 'DL']:
# print an error message and exit the program.
    print('Error: student status must be UG, G or DL')
    # Otherwise read from input floats for homework points, quiz points, midterm exam score, and final exam score
else:
    homework_points = float(input("Student homework points:"))
    quizzes_points = float(input("Student quizzes points:"))
    midterm_points = float(input("Student midterm points:"))
    final_points = float(input("Student final points:"))

    homework_average = (homework_points / homework_max) * 100  
    quizzes_average = (quizzes_points / quizzes_max) * 100  
    midterm_average = (midterm_points / midterm_max) * 100  
    final_average = (final_points / final_max) * 100  
    
    if student_status == 'UG':
        homework_weight = 0.20
        quizzes_weight = 0.20
        midterm_weight = 0.30
        final_weight = 0.30
        
    elif student_status == 'G':
        homework_weight = 0.15
        quizzes_weight = 0.05
        midterm_weight = 0.35
        final_weight = 0.45
        
    else:
        homework_weight = 0.05
        quizzes_weight = 0.05
        midterm_weight = 0.40
        final_weight = 0.50
        
    course_average = (homework_weight * homework_average + 
                      quizzes_weight * quizzes_average + 
                      midterm_weight * midterm_average + 
                      final_weight * final_average)

    
    if 0 <= homework_average <= 100:
        print(f"Homework: {homework_average:.1f}%")
    else:
        print(f"Average cannot be higher than {homework_max:.1f}")
    if 0 <= quizzes_average <= 100:
        print(f"Quizzes: {quizzes_average:.1f}%")
    else:
        print(f"Average cannot be higher than {quizzes_max:}")
    midterm_average = (midterm_points / midterm_max) * 100  
    if 0 <= midterm_average <= 100:
        print(f"Midterm: {midterm_average:.1f}%")
    else:
        print(f"Average cannot be higher than {midterm_max}")
    final_average = (final_points / final_max) * 100  
    if 0 <= final_average <= 100:
        print(f"Final: {final_average:.1f}%")
    else:
        print(f"Average cannot be higher than {final_max}")
    print(f'{student_status} average: {course_average:.1f}%')
#Identify the course letter grade based on the course average using the table below. Output the course letter grade
    grading_letters = ['A','B','C','D','F']
    if course_average >= 90 and course_average <= 100:
        print('Grade: A')
    elif course_average >= 80 and course_average < 90:
        print('Grade: B')
    elif course_average >= 70 and course_average < 80:
        print('Grade: C')
    elif course_average >= 60 and course_average < 70:
        print('Grade: D')
    else:
        print('F')
        