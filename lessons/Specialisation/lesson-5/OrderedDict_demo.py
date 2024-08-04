# Using OrderedDict
# With OrderedDict, the order of items is preserved as they are added.

# Preserving User Input Order:
# Scenario: You're developing a form where users can enter their preferences.
# You want to store these preferences in the order they were provided by the user.
# Usage: Use OrderedDict to maintain the insertion order of the preferences.

# Useful for Python versions older than 3.7

from collections import OrderedDict

user_preferences = OrderedDict()
user_preferences["Favourite colour"] = "Yellow"
user_preferences["Favourite food"] = "Dolmades"
user_preferences["Favourite hobby"] = "Cheerleading"
print(user_preferences.values())

