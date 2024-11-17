class Car:
    def __init__(self, year_model, make):
        self.year_model = year_model
        self.make = make
        self.speed = 0

    def accelerate(self):
        self.speed += 5

    def brake(self):
        self.speed = max(0, self.speed - 5)

    def get_speed(self):
        return self.speed


# Demonstrate the Car class
my_car = Car(2024, "Toyota")

# Accelerate 5 times
print("Accelerating:")
for _ in range(5):
    my_car.accelerate()
    print(f"Current speed: {my_car.get_speed()} km/h")

# Brake 5 times
print("\nBraking:")
for _ in range(5):
    my_car.brake()
    print(f"Current speed: {my_car.get_speed()} km/h")
