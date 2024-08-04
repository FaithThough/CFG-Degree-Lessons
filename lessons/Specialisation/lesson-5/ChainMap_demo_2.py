from collections import ChainMap

# Define different levels of settings
default_settings = {
    'theme': 'light',
    'language': 'English',
    'show_notifications': True
}

user_settings = {
    'language': 'Spanish',
    'show_notifications': False
}

session_settings = {
    'show_notifications': True
}

# Create a ChainMap
settings = ChainMap(session_settings, user_settings, default_settings)

# Accessing settings
print("Theme:", settings['theme'])  # Output: light (from default_settings)
print("Language:", settings['language'])  # Output: Spanish (from user_settings)
print("Show Notifications:", settings['show_notifications'])  # Output: True (from session_settings)

# Updating settings
settings['theme'] = 'dark'
print("Updated Theme:", settings['theme'])  # Output: dark

# Adding new settings to the session
settings['volume'] = 70
print("Volume:", settings['volume'])  # Output: 70

# The underlying dictionaries
print("Session Settings:", session_settings)
print("User Settings:", user_settings)
print("Default Settings:", default_settings)