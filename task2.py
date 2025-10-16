class Student:
    def __init__(student, name, age, course):
        student.name = name
        student.age = age
        student.course = course
    
    def display_info(student):
        print(f"Hi, I'm {student.name}. I'm {student.age} years old, studying for {student.course}.")

student1 = Student("Emmanuel", 22, "Bachelor in Computer Science")
student2 = Student("Regina", 19, "Diploma in Business Administration")

student1.display_info()
student2.display_info()