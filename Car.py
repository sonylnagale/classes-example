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
class ElectricCar(Car):
    def __init__(self, brand, model, year, doors, battery_capacity):
        super().__init__(brand, model, year, doors)
        self.battery_capacity = battery_capacity

    def display_info(self):
        """Override the display_info method to include battery information."""
        return f"Electric Car: {self._brand} {self._model}, {self.doors} doors ({self._year}) - Battery: {self.battery_capacity} kWh"

    def charge(self):
        """New method specific to ElectricCar."""
        return "Charging the battery!"
