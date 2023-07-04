def test_homework():
    assert ("home", "work") == ("home", "work")


def test_QA():
    a = "QA"
    b = "QC"
    assert a == b


def test_not():
    assert not (1, 1, 2, 3, 5) == (2, 3, 5)