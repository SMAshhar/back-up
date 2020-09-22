# # # # MAIN CLASS DEFINITION # # # #

class PIAIC():
    def __init__(self, name, resid, alies):
        self.name = name
        self.resid = resid
        self.alies = alies

# # # Following the Student's path # # #

class Student(PIAIC):
    def __init__(self, name, resid, alies, r_no, batch, course):
        super().__init__(name, resid, alies)
        self.r_no = r_no
        self.batch = batch
        self.course = course

# # Making the subclass for admin # #

class Admin(Student):
    def __init__(self, name, resid, alies, r_no, batch, course):
        super().__init__(name, resid, alies, r_no, batch, course)
        self.rights = "All rights to the system"

# # Making the last subclass of user # #

class User(Student):
    def __init__(self, name, resid, alies, r_no, batch, course):
        super().__init__(name, resid, alies, r_no, batch, course)
        self.rights = "Use the library but cabn't have access to change"

# # # Following the Employee's Path # # #

class Employee(PIAIC):
    def __init__(self, name, resid, alies, e_no, faculty):
        super().__init__(name, resid, alies)
        self.e_no = e_no
        self.faculty = faculty

# # Making the first subclass of Teacher # #

class Teacher(Employee):
    def __init__(self, name, resid, alies, e_no, faculty, course):
        super().__init__(name, resid, alies, e_no, faculty)
        self.course = course
        self.reports_to = "Zia"

# # Making the last subclass of Management # #

class Managemnet(Employee):
    def __init__(self, name, resid, alies, e_no, faculty, section):
        super().__init__(name, resid, alies, e_no, faculty)
        self.section = section
        self.reports_to = "Riaz"
        
# Just playing around with classes #

Ashhar = Admin("Ashhar", "Karachi", "Mr.", 950231, 8, "AI")

Inam = Teacher("Inam-ul-Haq", "Karachi", "Mr.", 100625, "AI", "Introduction to Python")

Kashifa = Managemnet("Kashifa Jalaal","Lahore", "Mrs.", 100523, "AI", "Accounts Manager")

# Printed my name Card #

print(f"""
    {Ashhar.alies} {Ashhar.name}
    Card No. {Ashhar.r_no}
    Batch {Ashhar.batch}
    Course {Ashhar.course}
    Resident of {Ashhar.resid}
    """)