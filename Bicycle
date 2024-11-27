from Vehicle import Vehicle

class Bicycle(Vehicle):
    def __init__(self, brand, model, year, gear_count):
        super().__init__(brand, model, year)
        self.gear_count = gear_count

    def display_info(self):
        """Override the parent class method for a Bicycle."""
        return f"Bicycle: {self._brand} {self._model}, Gears: {self.gear_count} ({self._year})"

    def ring_bell(self):
        """Specific implementation for a bicycle."""
        return "Ring ring!"

    def pedal(self):
        """Simulate pedaling the bicycle."""
        return "Keep pedaling! You rock!!"