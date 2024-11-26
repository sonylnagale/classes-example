from Vehicle import Vehicle

class EBike(Vehicle):
    def __init__(self, brand, model, year):
        super().__init__(brand, model, year)

    def display_info(self):
        """Override parent class parameters for EBike"""
        return f"EBike: {self.brand} {self.model}, {self.year}"
    
    def battery(self, capacity):
        """Specific implementation for EBike."""
        self.__max_charge = capacity
        print(f"Your max charge is {max_charge}")

    def charged(self):
        return "Fully charged"
    
    def battery_usage(self, miles):
        """Specific implementation for EBike."""
        remaining = self.__max_charge - (miles * 5)
        print (f"You have {remaining} power remaining after riding for {miles} miles.")
