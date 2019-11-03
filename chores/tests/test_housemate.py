import pytest
from housemate import Housemate


@pytest.mark.parametrize("email, expected", [
    ("bom@domain.com", True),
    ("mary@domain.co", True),
    ("@domain.com", False),
    ("@.com", False),
    ("domain.com", False)
])
def test_valid_email(email, expected):
    assert Housemate.is_valid_email(email) == expected, \
        f"Expected is_valid_email for email: {email} to be {expected}"


@pytest.mark.parametrize("name, email", [
    ("Bob", "bob@domain.com"),
    ("Mary", "mary@domain.com")
])
def test_housemate_init(name, email):
    """Tests that object instance created as expected"""
    housemate = Housemate(name, email)
    assert housemate.name == name, \
        f"Expected housemate.name to be set to {name}"
    assert housemate.email == email, \
        f"Expected housemate.email to be set to {email}"


@pytest.mark.parametrize("name, email", [
    ("Bob", "bdomain.com"),
    ("", "bob@domain.com"),
    ("Mary", "mary@d.c"),
    ("Mary", "mary@domain")
])
def test_invalid_housemate(name, email):
    """Tests that invalid housemate attributes raise ValueError."""
    with pytest.raises(
        ValueError, 
        message=f"Housemate should have been detected to be invalid with name {name} and email {email}"
    ):
        _ = Housemate(name, email)


@pytest.mark.parametrize("name, email", [
    ("Bob", "bob@domain.com"),
    ("Mary", "mary@domain.com")
])
def test_repr(name, email):
    housemate = Housemate(name, email)
    string = str(housemate)
    assert name in string
    assert email in string
    assert 'name' in string
    assert 'email' in string