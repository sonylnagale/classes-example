from Vehicle import Vehicle

class Moped(Vehicle):
	def __init__(self, brand, model, year):
		super().__init__(brand,model,year)

	def beepbeep(self):
		return "beep beep"

	def speed(self):
		return "this moped is moving at an astonishing 3 mph!"
