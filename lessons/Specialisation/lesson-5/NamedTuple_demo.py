# A NamedTuple is a subclass of Python's built-in tuple data type that allows you to give names to the elements of
# the tuple, making the code more readable and self-documenting.
# This is useful for creating simple classes or structures that are immutable and
# can be accessed using named attributes instead of
# just numerical indexes.

# --- Real-life Scenario ---
# Imagine you are working with a list of employees in a company. For each employee, you need to
# store their name, age, and job title.
# Using NamedTuple makes it clear what each element of the tuple represents,
# and you can access these elements by name.

from collections import namedtuple

Employee = namedtuple('Employee', ['name', 'age', 'job_title'])

employee1 = Employee('Elena Martinez', 29, 'Product Designer')
employee2 = Employee('Raj Patel', 35, 'Data Analyst')
employee3 = Employee('Mia Wong', 42, 'UX Researcher')

print(f"Employee 1 details \n Name: {employee1.name} \n Age: {employee1.age} \n Job title: {employee1.job_title}")
print(f"Employee 2 details \n Name: {employee2.name} \n Age: {employee2.age} \n Job title: {employee2.job_title}")
print(f"Employee 3 details \n Name: {employee3.name} \n Age: {employee3.age} \n Job title: {employee3.job_title}")

