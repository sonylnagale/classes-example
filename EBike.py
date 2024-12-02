from Vehicle import Vehicle

class EBike(Vehicle):
    def __init__(self, brand, model, year, capacity):
        super().__init__(brand, model, year)
        self.__battery = capacity

    def display_info(self):
        """Override parent class parameters for EBike"""
        return f"EBike: {self.brand} {self.model}, {self.year}"
    
    def battery(self):
        """Specific implementation for EBike."""
        print (f"Your max charge is at: {self.__battery}")

    def charged(self):
        return "Fully charged"
    
    def battery_usage(self, miles):
        """Specific implementation for EBike."""
        remaining = self.__battery - (miles * 5)
        print (f"You have {remaining} power remaining after riding for {miles} miles.")
