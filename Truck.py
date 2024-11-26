from Vehicle import Vehicle

class Truck(Vehicle):
    def __init__(self, brand, model, year, max_load, truckHeight):
        super().__init__(brand, model, year)
        self.max_load = max_load
        self.truckHeight = truckHeight

    def display_info(self):
        """Override the parent class method for a Truck."""
        return f"Truck: {self._brand} {self._model}, Max load: {self.max_load} tons ({self._year})"

    def honk(self):
        """Specific implementation for a truck."""
        return "HOOOOONK!"

    def heightLimit(self):
        """Method for comparing truck's height to height restrictions in bridges/tunnels"""
        return f"Truck height is {self.truckHeight}, and the height limit is 20"
