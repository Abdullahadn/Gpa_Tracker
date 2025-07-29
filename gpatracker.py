import numpy as np
class Student:
    def __init__ (self,name,roll_no,marks,grades = 0,GPA = 0):
        self.name = name
        self.rollno = roll_no
        self.marks = marks
        self.grades = grades
        self.GPA = GPA
class Gradebook:
    Max_Students = 50
    Max_Subjects = 5
    Dhl_threshold = 3.4
    
    def __init__(self):
        self.students_list = []
        self.all_marks = np.empty(shape=(self.Max_Students,self.Max_Subjects))
        self.Subjects = ['CS 101','MT 101','PHY 101','CH 101','HM 101']
        self.student_count = 0
    
    def add_student(self):
        if self.student_count >= self.all_marks.shape[0]:
            print("Cannot add more students. Limit reached.")
            return
        
        name1 = input("Enter name of Student: ")
        while True:
            try:
                rollinput = int(input("Enter Roll Number of Student: "))
                if (rollinput <1 or rollinput > self.Max_Students):
                    print("Invalid Roll Number")
                    continue
                break
            except ValueError:
                print("Invalid Input!")
                
        rollno1 = int('202900' + str(rollinput).zfill(2))
        for student in self.students_list:
            if (student.rollno == rollno1):
                print("Roll number already exists. Try again.")
                return

        marks1 = np.empty(self.Max_Subjects)
        for i in range(self.Max_Subjects): 
            while True:
                try:
                    marks1[i] = float(input("Enter marks for {} ".format(self.Subjects[i])))
                    if (marks1[i] <0 or marks1[i] > 100):
                        print("Invalid Marks ")
                        continue
                    break
                except ValueError:
                    print("Invalid Input!") 
        student1 = Student(name1,rollno1, marks1)
        self.students_list.append(student1)
        self.all_marks[self.student_count,:] = marks1
        self.student_count += 1
        
    def delete_student(self,rollno):
        for i,student in enumerate(self.students_list):
            if (student.rollno == rollno):
                del self.students_list[i]
                self.all_marks[i:self.student_count - 1] = self.all_marks[i + 1:self.student_count]
                self.student_count -=1
                self.all_marks[self.student_count] = np.zeros(self.Max_Subjects)
                
                print(f"Student with roll number {rollno} has been deleted.")
                return
        print(f"Student with roll number {rollno} not found.")
  
    
    def Subject_grading(self):
        if self.student_count == 0:
            print("No student records available.")
            return

        data = self.all_marks[:self.student_count, :]
        subject_average = np.mean(data,axis = 0)
        subject_std = np.std(data,axis = 0)
        z_scores = (data - subject_average) / subject_std
        conditions = [z_scores >= 1.5,(z_scores >= 1.0) & (z_scores < 1.5),(z_scores >= 0.5) & (z_scores < 1.0),(z_scores >= 0) & (z_scores < 0.5),(z_scores >= -0.5) & (z_scores < 0),(z_scores >= -1) & (z_scores < -0.5),(z_scores >= -1.5) & (z_scores < -1),(z_scores >= -2) & (z_scores < -1.5),z_scores < -2]
        choices = [4.0, 3.7,3.3,3.0,2.7,2.3,2.0,1.0,0]
        gpa_matrix = np.select(conditions, choices)
        conditions2 = [gpa_matrix == 4.0,gpa_matrix ==3.7,gpa_matrix ==3.3,gpa_matrix ==3.0,gpa_matrix ==2.7,gpa_matrix ==2.3,gpa_matrix ==2.0,gpa_matrix ==1.0,gpa_matrix ==0]
        choices2 = ['A','A-','B+','B','B-','C+','C','D','F']
        grades_matrix = np.select(conditions2,choices2,default = 'F')
        for i in range(self.student_count):
            self.students_list[i].GPA = np.mean(gpa_matrix[i,:])
            self.students_list[i].grades = grades_matrix[i,:]
    
    def Display_DHL(self):
        i = 1
        for student in self.students_list:
            if (student.GPA >= self.Dhl_threshold):
                print("-" * 10,"\nStudent",i,"\n1.Roll no. : ",student.rollno,"\n2.Name : ",student.name)
                for j,k,l in zip(self.Subjects,student.marks,student.grades):
                    print(f"{j}: {k:.1f} ({l})")
                print("\n5.GPA : ",np.round(student.GPA,2))
            i= i+1
            
    def Display_everything(self):
        i = 1
        for student in self.students_list:
            print("-" * 10,"\nStudent",i,"\n1.Roll no. : ",student.rollno,"\n2.Name : ",student.name)
            i= i+1
            for j,k,l in zip(self.Subjects,student.marks,student.grades):
                print(f"{j}: {k:.1f} ({l})")
            print("\n5.GPA : ",np.round(student.GPA,2))
    def generate_dummy_students(self):
        for i in range(self.Max_Students):
            name = f"Student_{i+1}"
            rollno = int(f"202900{i+1}")
            marks = np.random.uniform(40, 100, size=self.Max_Subjects)
            student = Student(name,rollno, marks)
            self.students_list.append(student)
            self.all_marks[self.student_count, :] = marks
            self.student_count += 1
            
            
            
gradebook = Gradebook()
print("\n\t\t\t\tWELCOME TO GPA TRACKER")

while True:
    print("-" * 30,"\n1.Add Student\n2.Delete Student\n3.Compute Grades\n4.Display ALL\n5.Display DHL Holders\n6.Generate Dummy\n7.Exit Program")
    
    try:
        choice = int(input("\nEnter Choice: "))
        if (choice == 1):
            gradebook.add_student()
        elif(choice == 2):
            roll_no = int('202900' + input("Enter Roll Number of Student to Delete: "))
            gradebook.delete_student(roll_no) 

        elif (choice == 3):
            gradebook.Subject_grading()
        elif (choice == 4):
            gradebook.Display_everything()
        
        elif(choice == 5):
            gradebook.Display_DHL()
        elif (choice == 6):
            gradebook.generate_dummy_students() 
        elif (choice == 7):
            print("Program terminated!")
            break 

        else: print("Wrong Input \n Try Again!")
    except ValueError:
        print("Invalid Choice!")
        continue
      
print("GOODBYE!!!")