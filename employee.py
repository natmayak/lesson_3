class Employee:
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)


emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)
emp1.displayCount()
emp2.displayEmployee()

emp1.age = 27  # Add an 'age' attribute
emp1.age = 28  # Modify 'age' attribute
del emp1.age # Delete 'age' attribute
emp2.age = 26  # Add an 'age' attribute

print(emp2)

hasattr(emp2, 'age')    # Returns true if 'age' attribute exists
getattr(emp2, 'age')    # Returns value of 'age' attribute
setattr(emp2, 'age', 8) # Set attribute 'age' at 8
delattr(emp2, 'age')    # Delete attribute 'age'

# __dict__ − Dictionary containing the class's namespace.
# __bases__ − A possibly empty tuple containing the base classes, in the order of their occurrence in the base class list.
print("Employee.__bases__:", Employee.__bases__)
print("Employee.__dict__:", Employee.__dict__)