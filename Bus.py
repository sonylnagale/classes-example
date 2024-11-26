from Vehicle import Vehicle

class Bus(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.capacity = capacity

    def display_info(self):
        """Override the parent class method for a Bus."""
        return f"Bus: {self._brand} {self._model}, seats {self.capacity} passengers ({self._year})"

    def honk(self):
        """Specific implementation for a bus."""
        return "Beep Beep! Make way for the bus!"

    def open_doors(self):
        """Simulate opening the bus doors."""
        return "The bus doors are open."
