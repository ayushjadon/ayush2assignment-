# creating class employee
class Employee:
    no_of_leaves = 8
# initialisation for anme asalary arole
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"

# alocating harry to employee class and enter details in it
harry = Employee("Harry", 255, "Instructor")


# printing output for harry
print(harry.salary,harry.name,harry.role)
print(harry.no_of_leaves)
