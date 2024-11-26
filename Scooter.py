from Vehicle import Vehicle

class Scooter(Vehicle):
        def __init__(self, brand, model, year, lights):
                super().__init__(brand, model, year)
                self.lights = lights

        def display_info(self):
                """Override the parent class method for a Car."""
                return f"Car: {self._brand} {self._model}, {self.lights} lights ({self._year})"

        def honk(self):
                """Specific implementation for a scooter."""
                return "MOVE!"