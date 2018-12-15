import pytest
from chore import Chore


@pytest.mark.xfail
@pytest.mark.parametrize("name, frequency_days", [
    ("Clean bathroom", 7),
    ("Vacuuming", 7)
])
def test_chore_init(name, frequency_days):
    """Tests that object instance created as expected
    """
    chore = Chore(name, frequency_days)
    assert chore.name == name
    assert chore.frequency_days == frequency_days


@pytest.mark.xfail
@pytest.mark.parametrize("name, frequency_days", [
    ("Clean bathroom", 7),
    ("Vacuuming", 7)
])
def test_repr(name, frequency_days):
    chore = Chore(name, frequency_days)
    string = str(chore)
    assert name in string
    assert frequency_days in string
    assert 'name' in string
    assert 'frequency_days' in string