class Vehicle:
    def __int__(self, mileage: int, max_sped=150):
        self.max_speed = max_sped
        self.mileage = mileage
        self.gadgets = []


car = Vehicle(20)
print(car.max_speed)
print(car.mileage)
print(car.gadgets)
car.gadgets.append('Hudly Wireless')
print(car.gadgets)
