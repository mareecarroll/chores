import pytest
from housemate import Housemate


@pytest.mark.xfail
@pytest.mark.parametrize("name, email", [
    ("Bob", "bob@domain.com"),
    ("Mary", "mary@domain.com")
])
def test_housemate_init(name, email):
    """Tests that object instance created as expected
    """
    housemate = Housemate(name, email)
    assert housemate.name == name
    assert housemate.email == email


@pytest.mark.xfail
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