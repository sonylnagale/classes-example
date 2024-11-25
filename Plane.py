from Vehicle import Vehicle
#Add a child class and edit a current class

class Plane(Vehicle): #created a child class called Plane
    def __init__(self, brand, model, year, flight_time):
        super().__inti__(brand, model, year)
        self.flight_time = flight_time

    def display_info(self):
        return f"Plane: {self._brand} {self._model}, Max load: {self.max_load} tons ({self._year})"

    def honk(self):
        return "It's a plane! It's a bird! No it is a plane!"
    
    def diplay_flight(self):
        return "Flight time."