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
        """Override the parent class method for an ElectricCar."""
        return (f"Electric Car: {self._brand} {self._model}, {self.doors} doors, "
                f"{self.battery_capacity} kWh battery ({self._year})")

    def charge(self):
        """Specific implementation for charging the electric car."""
        return f"{self._brand} {self._model} is now charging."

    def honk(self):
        """Specific implementation for an electric car's horn."""
        return "Beep beep!"