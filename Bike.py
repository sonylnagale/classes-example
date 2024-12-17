from Vehicle import Vehicle

class Bike(Vehicle):
	def __init__(self, brand, model, year, bike_type):
		super().__init__(brand, model, year)
		self.bike_type = bike_type

    	def display_info(self):
		"""Override the parent class method for a Bike."""
		return f"Bike: {self._brand} {self._model}, Type: {self.bike_type} ({self._year})"

    	def honk(self):
		"""Specific implementation for a bike."""
		return "Ring Ring!"
