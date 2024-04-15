class student:
    school="telusko"
    def __init__(self,m1,m2,m3):
        self.m1= m1
        self.m2 = m2
        self.m3 = m3

    def average(self):
        return (self.m1 + self.m2 + self.m3)/3
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
    @classmethod
    def getschool(cls):
        return cls.school
    @staticmethod
    def info():
        print("This is student class ABC")




s1= student(34,67,67)
s2= student(45,67,87)
print(s1.average())
s1.set_m1(35)
print(s1.get_m1())
print(student.getschool())
student.info()
