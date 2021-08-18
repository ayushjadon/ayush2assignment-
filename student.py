# creating class student
class Student:
  pass

  def __init__(self, name, age, grade):
    self.name = name
    self.age = age
    self.grade = grade
# getting grades
  def get_grade(self):
      return self.grade
#  s1 and s2 to located for student
s1=Student ("tom", 16, 90)
s2=Student("arun",18,88)
print(s1.get_grade)
print(s1.name)
print(s1.age)
# creating new class course
class Course:
  def __init__(self, name, max_student):
    self.name = name
    self.max_student = max_student
    self.student = []
  def add_student(self, student):
    if(len(self.student) < self.max_student):
      self.student.append(student)
      print(self.student[0].grade)
      return true
      return false

  def avg_grade(self):
    value =0
    for s in self.student:
      value=value +s.get_get()

      return value / len(self.student)
s1=Student("joy",28,90)
s2=Student('tom',19,77)
c1=Course("science",2)
print(s1.add_Student(s1))
print(s1.add_Student(s2))
print(c1.avg_grade)