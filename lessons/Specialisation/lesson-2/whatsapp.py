class WhatsAppProfile:
    def __init__(self, name, phone_number, status = "Hello, I am using WhatsApp", profile_picture=None):
        self.name = name
        self.phone_number = phone_number
        self.status = status
        self.profile_picture = profile_picture

    def update_status(self, new_status):
        self.status = new_status

    def display_profile(self):
        print(f"Name: {self.name}")
        print(f"Phone number: {self.phone_number}")
        print(f"Status: {self.status}")

faith = WhatsAppProfile("Faith", "07123456789")
marcus = WhatsAppProfile("Marcus", "07987654321")
print(faith.display_profile())
print(marcus.display_profile())

marcus.update_status("At the gym")
print(marcus.display_profile())