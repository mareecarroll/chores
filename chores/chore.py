"""The Chore class to hold name and frequency in days."""
class Chore:

    def __init__(self, name, frequency_days):
        self.name = name
        self.frequency_days = frequency_days
    
    def __repr__(self):
        return f"<Chore(name={self.name}, frequency_days={self.frequency_days})>"