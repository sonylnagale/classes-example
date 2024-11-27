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

class Lamborghini(Car):
    def __init__(self, model, year, doors=2, max_speed=None):
        super().__init__("Lamborghini", model, year, doors)
        self.max_speed = max_speed

    def display_info(self):
        """Specific display method for Lamborghini."""
        info = super().display_info()
        if self.max_speed:
            return f"{info} - Top Speed: {self.max_speed} km/h"
        return info

    def honk(self):
        """Override honk for Lamborghini."""
        return "Roar! (Lamborghini style)"
