import pytest


def test_first():
    name = "Boris"
    assert name == 'Boris', "Not upper"


@pytest.mark.parametrize("name,email,age,expected", [
    ('Boris Isac', 'borisisac@gmail.com', 38, 'Boris Isac 38 borisisac@gmail.com'),
    (None, 'borisisac@gmail.com', 38, 'None 38 borisisac@gmail.com'),
    ('Boris Isac', None, 38, 'Boris Isac 38 None'),
    ('Boris Isac', 'borisisac@gmail.com', None, 'Boris Isac None borisisac@gmail.com')
])
def test_user_created(user, name, email, age, expected):
    assert str(user(name, email, age)) == expected


@pytest.mark.parametrize("name,email,age,expected", [
    ('Boris Isac', 'borisisac@gmail.com', 38, 'Boris Isac'),
    (None, 'borisisac@gmail.com', 38, None),
    ('Boris Isac', None, 38, 'Boris Isac'),
    ('Boris Isac', 'borisisac@gmail.com', None, 'Boris Isac')
])
def test_get_name(user, name, email, age, expected):
    assert user(name, email, age).get_name() == expected


@pytest.mark.parametrize("name,email,age,expected", [
    ('Boris Isac', 'borisisac@gmail.com', 38, 'borisisac@gmail.com'),
    (None, 'borisisac@gmail.com', 38, 'borisisac@gmail.com'),
    ('Boris Isac', None, 38, None),
    ('Boris Isac', 'borisisac@gmail.com', None, 'borisisac@gmail.com')
])
def test_get_email(user, name, email, age, expected):
    assert user(name, email, age).get_email() == expected


@pytest.mark.parametrize("name,email,age,expected", [
    ('Boris Isac', 'borisisac@gmail.com', 38, 38),
    (None, 'borisisac@gmail.com', 38, 38),
    ('Boris Isac', None, 38, 38),
    ('Boris Isac', 'borisisac@gmail.com', None, None),
    ('Boris Isac', 'borisisac@gmail.com', 'Boris Isac', TypeError),
    ('Boris Isac', 'borisisac@gmail.com', -1, ValueError),
    ('Boris Isac', 'borisisac@gmail.com', 0, ValueError),
    ('Boris Isac', 'borisisac@gmail.com', 100, 100),
    ('Boris Isac', 'borisisac@gmail.com', 101, ValueError),
])
def test_get_age(user, name, email, age, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            user(name, email, age).get_age()
    else:
        assert user(name, email, age).get_age() == expected
