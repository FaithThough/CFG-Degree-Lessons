# Log Analysis:
# Scenario: You are analyzing server logs to identify the frequency of different types of HTTP requests.
# Usage: Count the occurrences of each type of request (e.g., GET, POST) to determine which ones are most common.

from collections import Counter
# List
log_entries = ['GET', 'POST', 'GET', 'GET', 'POST', 'PUT', 'PUT', 'GET', 'DELETE', 'GET', 'DELETE']
request_count = Counter(log_entries)
print(request_count)

# String
course_provider = "Code First Girls"
# Dictionary
courses = {"Javascript": 3, "Python": 2, "HTML": 1, "Careers advice":2, "DevOps": 2}

dictionary_count = Counter(course_provider)
course_count = Counter(courses)

print(dictionary_count)
print(course_count)

