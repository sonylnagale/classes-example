from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, brand, model, year, gears):
        super().__init__(brand, model, year)

    def display_info(self):
        """Override the parent class method for a Car."""
        return f"Bike: {self._brand} {self._model}, {self.gears} gears ({self._year})"

    def bell(self):
        """Specific implementation for a car."""
        return "Ring ring!"
    