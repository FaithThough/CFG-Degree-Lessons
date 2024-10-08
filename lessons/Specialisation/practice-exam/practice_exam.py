"""
TASK 1

Design a parent class called CFGStudent.

It should have general attributes like name, surname, age, email, student id
and methods to fetch student’s full name and student’s id.

Design a child class called NanoStudent, which  inherits from CFGStudent class.
This class should have exactly the same attributes as its parent class,
as well as an additional one called ‘specialization’ and course grades.

The child class ‘generate_id’ method should override its parent method to add the suffix ‘NANO’
in front of the id.

New methods ‘add_new_grade’ and ‘get_course_grades’ should be added.
You can use  it as a skeleton code for your classes OR adjust it and create your own.

SEE NOTES BELOW

"""
import random

class CFGStudent:

    def __init__(self, name, surname, age, email, student_id=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.student_id = student_id if student_id is not None else self.generate_id()

    @staticmethod
    def generate_id():
        student_id = random.randint(1000, 10000)
        return str(student_id)

    def get_id(self):
        return(self.student_id)

    def get_fullname(self):
        return(self.name, self.surname)

class NanoStudent(CFGStudent):

    def __init__(self, name, surname, age, email, student_id=None, specialization=None, course_grades=None):
        super().__init__(name, surname, age, email, student_id)
        self.specialization = specialization
        self.course_grades = course_grades
        # Initialising the container as an empty dictionary
        self.course_grades_container = {}


    @staticmethod
    def generate_id():
        random_number_string = str(random.randint(1000, 10000))
        student_id = "NANO" + random_number_string
        return str(student_id)

    def add_new_grade(self, task_title, grade):
        # Add or update task title with grade in container
        self.course_grades_container[task_title] = grade

    def get_course_grades(self):
        return(self.course_grades_container)

############################################

# Example run

s = CFGStudent('Anna', 'Smith', 18, 'anna@mail.com')  # do not pass ID, it should be generated automatically
print(s.get_fullname())
# returns 'Anna Smith'
print(s.student_id)
# returns '3868' or some other random number

cfg_s = NanoStudent(specialization='Software', name='Mia', surname='Papandopulu', age=20, email='mia@mail.com')
print(cfg_s.get_fullname())
# returns 'Mia Papandopulu'
print(cfg_s.get_id())
# returns 'NANO6180' or some other random number

cfg_s.add_new_grade('theory', 95)
cfg_s.add_new_grade('project', 78)
print(cfg_s.get_course_grades())
# returns {'theory': 95, 'project': 78}



"""
TASK 2

Given an index limit, find all corresponding Fibonacci values up to that limit in a sequence 
and return the sum of all even Fibonacci numbers. See more details in the task description in 
your assessment paper. 
"""
def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        return fibonacci_number(n-1) + fibonacci_number(n-2)

def even_fibonacci_sum(limit):
    fibonacci_sequence = [fibonacci_number(i) for i in range(limit)]
    even_fibonacci_numbers = [x for x in fibonacci_sequence if x % 2 == 0]
    return sum(even_fibonacci_numbers)

##### TESTS ####

print(even_fibonacci_sum(limit=10))  # should be 44
print(even_fibonacci_sum(limit=15))  # should be 188
print(even_fibonacci_sum(limit=1))   # should be 0





"""
TASK 3

Validate subsequence. Use suggested tests below to check
correctness of your solution. 
"""

def is_valid_subsequence(array, sequence):
    index = 0
    n = len(sequence)

    # Iterate through the main array
    for element in array:
        # Check if current element in array matches the current target in numbers
        if index < n and element == sequence[index]:
            index += 1  # Move to the next element in numbers

        # Check if we have matched all elements of numbers
        if index == n:
            return True

    # If loop completes and not all elements were matched
    return False


#### TESTS ####

array1 = [5,1,22,25,6,-1,8,10]
sequence1 = [1,6,-1,-2]

print(is_valid_subsequence(array1, sequence1))  # FALSE


array2 = [5,1,22,25,6,-1,8,10]
sequence2 = [1,6,-1, 10]

print(is_valid_subsequence(array2, sequence2))  # TRUE


array3 = [5,1,22,25,6,-1,8,10]
sequence3 = [25]

print(is_valid_subsequence(array3, sequence3))  # TRUE



"""
TASK 4

WRITTEN ASSIGNMENT

Write a review on how 'class Employee' can be improved.
(See PDF document with the code example)
"""


'''
- According to the single responsibility principles, a class should only have one job or responsibility, in this case it has 5 responsibilities, initialisation, updating department, updating status, saving employees, removing employees, and printing employee reports
    - Consider writing a new class for each.
    - *The reason for this being:*
        - *Adhering to the single responsibility principle promotes modularity.*
        - *Each class becomes a distinct module with a well-defined responsibility, making the system easier to understand, maintain, and extend.*
- *The code could be refactored as follows:*
    - *An employee class that contains information related to an employee only and methods that allow to modify employee
    information*
    - *A function or a class that can becalled something like ‘DB handler’, which would manage all DB actions: saving, fetching , deleting data etc*
    - *A function or a class that would be responsible for writing or reading reports. (slight refactoring variations allowed)*
- The is_active attribute doesn’t match the self.active status = is_active
    - Consider changing it to self.active_status = True/False
- The def remove_employee function only deletes their name and id
    - Consider deleting all attributes i.e. is_active and department
- Following the interface segregation method we should ensure that all methods are utilised. Again this should be divided into smaller interfaces rather than one large one.
- *Functions / methods that are concerned with using DB engines or even writing a report to a file do not have any error handling. → It is a good practice to use blocks like try/except to handle and raise errors with relevant informative messages, especially when trying to connect to a DB or write some data to a file.*
- *This class is lacking any comments or docstrings*

'''





