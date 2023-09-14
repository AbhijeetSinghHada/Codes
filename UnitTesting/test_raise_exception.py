from pytest import raises


def raiseValueError():
    raise ValueError("ValueError exception thrown")
    # pass


def test_exception():
    with raises(ValueError):
        raiseValueError()
