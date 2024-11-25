from Vehicle import Vehicle

class Mazda(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def display_info(self):
        """Override the parent class method for a Mazda car."""
        return f"Mazda: {self._brand} {self._model} ({self._year})"

    def honk(self):
        """Specific implementation for a Mazda."""
        return "Beep beep, I’m stylish!"

    def fuel(self):
        """Mazda-specific fuel advice."""
        return "Fuel up, zoom ready!"


