class Student :
    def __init__(self,name,studentNumber) -> None:
        self.name = name 
        self.studentNumber = studentNumber 
    
    def doHomework(self):
        print(f"{self.name} is doing homework")
    
    def notStudy(self):
        print(f"{self.name} is not studying")


student1 =Student("Ahmet Suat",1010)
student2 =Student("Yasemin",1020)
student1.doHomework()
student2.notStudy()

