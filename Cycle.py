from Vehicle import Vehicle

class Cycle(Vehicle):
    def __init__(self, brand, model, year, wheels):
        super().__init__(brand, model, year)
        self.wheels = wheels

    def display_info(self):
        """Override the parent class method for a Cycle."""
        return f"Cycle: {self._brand}, Model: {self._model}, Wheels: {self.wheels} ({self._year})"

    def bell(self):
        """Specific implementation for a cycle."""
        return "Ring! Ring!"
