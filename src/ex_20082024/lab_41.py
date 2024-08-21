score = int(input("Enter the Score\n"))
grade = "F"

if 90 <= score <= 100: #we can also use 90 <= score <=100
    grade = "A"
    print("Your grade is ", grade)
elif score >= 80 and score <= 89: #we can also use 90 <= score <=100
    grade = "B"
    print("Your grade is ", grade)
elif score >= 70 and score <= 79: #we can also use 90 <= score <=100
    grade = "C"
    print("Your grade is ", grade)
elif score >= 60 and score <= 69: #we can also use 90 <= score <=100
    grade = "C"
    print("Your grade is ", grade)
elif score < 60:
    grade = "F"
    print("Your grade is ", grade)
else:
    print("Invalid entry")
