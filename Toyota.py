from Vehicle import Vehicle

class Toyota(Vehicle)
    def __init__(self, model, year, doors):
        super().__init__(model, year)
        self.color = color

    def display_info(self):
        return f"Toyota: {self._model}, {self.color} color ({self._year})"
    
    def talkingcar(self):
        return "I am a talking toyota"