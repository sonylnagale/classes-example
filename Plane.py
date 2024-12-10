from Vehicle import Vehicle

class Plane(Vehicle):
    def __init__(self, brand, model, year, num_engines):
        super().__init__(brand, model, year)
        self.num_engines = num_engines

    def display_info(self):
        """Override the parent class method for a Plane."""
        return f"Plane: {self._brand} {self._model} ({self._year}), {self.num_engines} engines"

    def get_fuel_type(self):
        """Implement get_fuel_type specific to planes"""
        return "Jet fuel"

    def take_off(self):
        """New method specific to planes"""
        return "Taking off!"