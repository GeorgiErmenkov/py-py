class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers. And is {self.size}"

class Bus(Vehicle):
    def __init__(self, name, max_speed, milage, size='big'):
        super().__init__(name, max_speed, milage)
        self.size = size

School_bus = Bus("School Volvo", 150, 10000)
print(School_bus.seating_capacity(50))
