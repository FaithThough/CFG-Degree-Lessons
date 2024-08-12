# Function based approach
def status_code_meaning(number):
    if number == 200:
        return "OK"
    elif number == 301:
        return "Move permanently"
    elif number == 401:
        return "Unauthorised"
    elif number == 404:
        return "Not found"
    elif number == 500:
        return "Internal server error"

# Dictionary-Based Approach
status_code = {200: "OK",
               301: "Move permanently",
               401: "Unauthorised",
               404: "Not found",
               500: "Internal server error"}


