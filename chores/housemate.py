"""The Housemate class to hold name and email."""
class Housemate:

    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def __repr__(self):
        return f"<Housemate(name={self.name}, email={self.email})>"