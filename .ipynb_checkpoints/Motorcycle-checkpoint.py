from Vehicle import Vehicle

class Motorcycle(Vehicle):
    def __init__(self, brand, model, year, has_sidecar):
        super().__init__(brand, model, year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        """Override the parent class method for a Motorcycle."""
        sidecar = "with sidecar" if self.has_sidecar else "without sidecar"
        return f"Motorcycle: {self._brand} {self._model}, {sidecar} ({self._year})"

    def honk(self):
        """Specific implementation for a motorcycle."""
        return "Meep meep!"
