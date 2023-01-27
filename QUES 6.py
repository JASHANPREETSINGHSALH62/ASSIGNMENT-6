n=input("Enter student name: ")
sid = int(input("Enter SID: "))
c = int(input("Enter class"))
def student_data(student_id, student_name=None, student_class=None):
    print("Student ID:", student_id)
    if student_name:
        print("Student Name:", student_name)
    if student_class:
        print("Student Class:", student_class)
student_data(sid, student_name=n, student_class=c)