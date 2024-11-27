from Vehicle import Vehicle

class Boat(Vehicle):
    def __init__(self, brand, model, year, boat_type):
        super().__init__(brand, model, year)  
        self.boat_type = boat_type 

    def display_info(self):
        """Override the parent class method for a Boat."""
        return f"Boat: {self._brand} {self._model}, Type: {self.boat_type} ({self._year})"
    
    def honk(self):
        """Specific implementation for a boat."""
        return "Hooo hooo!"


if __name__ == "__main__":
    my_boat = Boat("Jiajian", "242X", 2021, "Speedboat")
    print(my_boat.display_info())   
    print(my_boat.honk())           
    print(my_boat.sail())