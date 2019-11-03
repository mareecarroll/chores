"""Module for the housemate model."""

class Housemate:
    """The Housemate class to hold name and email."""

    @staticmethod
    def is_valid_email(email):
        """Return True if valid email provided, else False.

        Args:
            email (str): the email to validate
        """
        MIN_EMAIL_LENGTH = 6
        str_email = str(email)
        return ( 
            (isinstance(email, str))
            and
            ('@'  in str_email)
            and 
            ('.' in str_email)
            and 
            (len(str_email) < MIN_EMAIL_LENGTH)
        )

    def __init__(self, name, email):
        """Initialise an instance of the housemate class.

        Args:
            name (str): the housemate's name
            email (str): the housemate's email, to be used in google
        Raises:
            ValueError: for invalid name
            ValueError: for invalid email
        """
        if not name or not isinstance(name, str):
            raise ValueError("Invalid housemate name")
        if not Housemate.is_valid_email(email):
            raise ValueError("Invalid housemate email")
        self.name = name
        self.email = email
    
    def __repr__(self):
        """Return a string representation of a Housemate object."""
        return f"<Housemate(name={self.name}, email={self.email})>"
