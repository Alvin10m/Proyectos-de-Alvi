print("Bienvenido")

grade = float(input("Enter the student's grade: "))


if grade < 0 or grade > 100:
    print("Invalid value")
else:
   
    status = "Student promoted" if grade >= 70 else "Student failed"


    if grade == 100:
        letter = "A+"
    elif grade >= 90:
        letter = "A"
    elif grade >= 80:
        letter = "B"
    elif grade >= 70:
        letter = "C"
    else:
        letter = "F"


    print(f"{status} - Grade: {letter}")
