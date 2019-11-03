"""Module for the chore model."""
class Chore:
    """The chore class represents a household chore."""

    def __init__(self, name, frequency_days):
        """Initialise an instance of the chore class.

        Args:
            name (str): the descriptive name of the chore
            frequency_days (int): how often the chore needs to be done in days
        """
        self.name = name
        self.frequency_days = frequency_days
    
    def __repr__(self):
        """Return a string representation of a class instance."""
        return f"<Chore(name={self.name}, frequency_days={self.frequency_days})>"
