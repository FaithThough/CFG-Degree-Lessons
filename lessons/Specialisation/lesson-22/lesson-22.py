class Vehicle:
    def __init__(self, name, max_speed, fuel_type):
        self.name = name
        self.max_speed = max_speed
        self.fuel_type = fuel_type

    def get_travel_time_to_destination(self):
        distance = 300
        travel_time = distance/self.max_speed
        return travel_time


class ElectricCar(Vehicle):
    def __init__(self, name, max_speed, fuel_type):
        super().__init__(name, max_speed, fuel_type)

    @staticmethod
    def battery_status(initial_battery_life_percentage, distance_travelled):
        # Define battery consumption rate: 1% per 3 kilometers
        battery_consumption_rate = 1 / 3  # percentage per kilometer

        # Calculate the battery consumption
        battery_consumed = distance_travelled * battery_consumption_rate

        # Calculate projected battery life
        projected_battery_life = initial_battery_life_percentage - battery_consumed

        # Ensure battery life does not go below 0%
        if projected_battery_life < 0:
            projected_battery_life = 0

        # Print the battery status
        return(f"Battery consumed: {battery_consumed:.0f}%")

Tesla = ElectricCar("Tesla Model 3", 261, "Electric")

print(Tesla.battery_status(100, 150))

class PassengerPlane(Vehicle):
    def __init__(self, name, max_speed, fuel_type,number_of_passengers):
        super().__init__(name, max_speed, fuel_type)
        self.number_of_passengers = number_of_passengers

    def boarding_time(self):
        boarding_time = self.number_of_passengers * 2
        return(f"The boarding time for {self.number_of_passengers} passengers is {boarding_time} minutes")

Boeing = PassengerPlane("Boeing 747", 920, "jet fuel", 416)
print(Boeing.boarding_time())

