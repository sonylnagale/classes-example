from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, doors):
        super().__init__(brand, model, year)
        self.doors = doors

    def display_info(self):
        """Override the parent class method for a Car."""
        return f"Car: {self._brand} {self._model}, {self.doors} doors ({self._year})"

    def honk(self):
        """Specific implementation for a car."""
        return "Honk honk!"
my_car= Car(brand = 'Toyota', model = 'Supra', year = '2024', doors='2')
print(my_car.display_info())
print(my_car.honk())
