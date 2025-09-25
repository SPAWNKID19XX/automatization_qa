import pytest

def test_first():
    name = "Boris"
    assert name == 'Boris', "Not upper"

@pytest.mark.parametrize("a,b,expected", [
    (0,0,0),
    (0,1,1),
    (1,0,1),
    (-1,4,3),
    (4,-1,3),
    (-4,-2,-6),
    (5.5,4.4,9.9),
    (5.5,4.5,10.0),
])
def test_add(calc,a,b,expected):
    assert calc.add(a,b) == expected


@pytest.mark.parametrize("a,b,expected", [
    (10,2,5),
    (2,10,0.2),
    (1,3,1/3),
    (0,1,0),
    (1,0,"ZeroDivisionError")
])
def test_div(calc,a,b,expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            calc.div(a, b)
    assert calc.div(a,b) == pytest.approx(expected)