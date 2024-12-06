#AARON BENEDITT LAB 6
import pickle

class Course_grades():
    def __init__(self):
        self.course_name = ""
        self.stu_ID = []
        self.stu_grade = []
    def get_details(self):
        self.course_name = input("Enter the name of the course: ")
        while True:
            stu_amount = int(input("Enter the number of students you would like to add (at least 5): "))
            if stu_amount >= 5:
                break
            else:
                print("***Error*** There must be AT LEAST 5 students.Please Try Again***.")
        for x in range(0, stu_amount):
            print("Enter the following Student info: ")
            self.stu_ID.append(input("Enter the Student ID: "))
            self.stu_grade.append(int(input("Enter the student Grade(0-100): ")))
            print("***Student information added to the system***")

#Creation of objects
print("***************************")
print("***Enter the first class***")
print("***************************")
ob1 = Course_grades()
ob1.get_details()
print("****************************")
print("***Enter the second class***")
print("****************************")
ob2 = Course_grades()
ob2.get_details()
print("***************************")
print("***Enter the third class***")
print("***************************")

ob3 = Course_grades()
ob3.get_details()
print("****************************")
print("***Enter the fourth class***")
print("****************************")
ob4 = Course_grades()
ob4.get_details()

#Write the objects s1, s2 into a *.dat file
grades = open('grades_info.dat', 'ab')
pickle.dump(ob1, grades)
pickle.dump(ob2, grades)
pickle.dump(ob3, grades)
pickle.dump(ob4, grades)
grades.close()

#open the same dat file in read-binary mode
grades = open('grades_info.dat','rb')


#read the objects from the file and print the attributes of the class
while 1:
    try:
        data = pickle.load(grades)
        print("The course name is:")
        print(data.course_name)
        print("The Students ID for this course are the following:")
        print(data.stu_ID)
        print("The Students Grades for this course are the following:")
        print(data.stu_grade)
    except (EOFError):
        break
grades.close()