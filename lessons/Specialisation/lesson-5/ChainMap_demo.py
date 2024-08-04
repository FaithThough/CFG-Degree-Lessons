# ChainMap is used to group multiple dictionaries into a single view.
# It allows you to treat them as a single dictionary.

# Scenario: Merging Employee Details from Different Departments
# Imagine you have two departments in a company, and you want to combine their employee details.

from collections import ChainMap

# Dictionary for employees in the Marketing department
marketing_department = {
    'Lydia Evergreen': 'Marketing Strategist',
    'Maximilian Drake': 'Creative Director',
    'Seraphina Blaze': 'Digital Marketing Specialist'
}

# Dictionary for employees in the Engineering department
engineering_department = {
    'Jasper Falcon': 'Lead Software Engineer',
    'Ariadne Storm': 'Cloud Solutions Architect',
    'Orion Blackwood': 'Data Science Lead'
}

combined_departments = ChainMap(marketing_department, engineering_department)
print(combined_departments['Maximilian Drake'])
print(combined_departments['Orion Blackwood'])

# Duplicate values
engineering_department['Lydia Evergreen'] = 'Software Engineering Graduate'
print(combined_departments['Lydia Evergreen'])



