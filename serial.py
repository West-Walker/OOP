class SerialNumberGenerator:
    def __init__(self, start_number=100):
        self.start_number = start_number
        self.current_number = start_number

    def generate_next_number(self):
        self.current_number += 1
        return self.current_number

    def reset_to_start(self):
        self.current_number = self.start_number

