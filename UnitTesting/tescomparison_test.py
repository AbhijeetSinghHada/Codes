from pytest import approx


def test_bad_float_compare():
    assert 0.3333333 == 1.0 / 3.0


def test_good_float_compare():
    val = (1.0 / 3.0)
    assert val == approx(0.3333333)
