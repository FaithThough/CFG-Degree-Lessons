# CREATE A BASE CLASS
#
# class Vehicle:
#     def vehicle_method(self):
#         print("This is parent Vehicle class method")
#
#
# # CREATE A CAR CLASS INHERITS FROM VEHICLE
#
# class Car(Vehicle):
#     def car_method(self):
#         print("This is child Car class method")
#
#
# car_a = Car()
# car_a.vehicle_method()
#
#
# # ADD ANOTHER CHILD (HIERARCHICAL INHERITANCE)
#
# class Cycle(Vehicle):
#     def cycle_method(self):
#         print("This is child Cycle class method")
#
#
# cycle_a = Cycle()
# cycle_a.vehicle_method()

"""
MULTIPLE PARENTS/INHERITANCE
"""

class Camera:
    def camera_method(self):
        print("This is parent Camera class method")

class Radio:
    def radio_method(self):
        print("This is parent Radio class method")

class MobilePhone(Camera, Radio):
    def mobile_method(self):
        print("This is child MobilePhone class method")

phone_a = MobilePhone
# phone a has access to all camera, radio and mobilephone methods.