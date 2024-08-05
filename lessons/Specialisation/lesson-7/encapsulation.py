class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.__price = price # Private attribute

    def get_price(self):
        return self.__price

    # Setter method for price with validation
    def set_price(self, new_price):
        if new_price >=0:
            self.__price = new_price
        else:
            raise ValueError("Price cannot be negative or zero❌")

    def  display_information(self):
        return f"Product: {self.name} \nDescription: {self.description} \nPrice: {self.get_price()}"


whoop = Product("Fitness tracker", "A wearable device designed to monitor and analyze various health metrics, such as heart rate, sleep quality, and activity levels, to help users optimize their fitness, recovery, and overall well-being.", 29.99)
print(whoop.display_information())
whoop.set_price(32.99)
print(whoop.get_price())




