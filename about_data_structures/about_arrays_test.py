


def test_list():
    l = []
    assert str(type(l)) == "<class 'list'>"
    assert len(l) == 0

    list = [1, 2, 3, 4, 5]
    assert len(list) == 5


def test_append_etc():
    l1 = [1,2,3,4,5]
    l2 = [4,5,6,7,8]
