from Vehicle import Vehicle

class Tesla(Vehicle):
    def __init__(self, brand, model, year, mode, carColor):
        super().__init__(model, year)
        self.mode = mode
        self.carColor = carColor

    def display_info(self):
        """Override the parent class method for a specific Tesla model vehicle."""
        return f"Tesla: {self._model} {self._year}, {self._carColor}, and current mode is set at: ({self._mode})"

    def chargeWarning(self):
        """Specific warning implementation for a Tesla"""
        criticalBatteryWarning = True
        if (criticalBatteryWarning):
            return f"Your Tesla battery is at 10% or lower, you need to charge ASAP!"
    
    def noise(self):
        """Specific noise implementation for a Tesla"""
        if ({self._mode=="autopilot"}):
            return "You might hear beeping or alert sounds top help indicate actions."
        else:
            return "No noise as Tesla models are designed to be quiet, but you might hear faint whirring sounds at most."
        