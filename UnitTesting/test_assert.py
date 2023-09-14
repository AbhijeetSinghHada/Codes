def test_int_assert():
    assert 1 == 1


def test_float_assert():
    assert 1.0 == 1.0


def test_string_assert():
    assert "1" == "1"


def test_list_assert():
    assert [1, 2, 3] == [1, 2, 3]


def test_tuple_assert():
    assert (1, 2, 3) == (1, 2, 3)


def test_set_assert():
    assert {1, 2, 3} == {1, 2, 3}


def test_dict_assert():
    assert {"a": 1, "b": 2, "c": 3} == {"a": 1, "b": 2, "c": 3}
