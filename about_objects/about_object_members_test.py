import pytest

class Duck:
    def quack(self):
        return "quack"


class Dog:
    def bark(self) :
        return "wuff"



def test_quack() :
    duck = Duck()
    assert "quack" == duck.quack()

def test_dog_is_no_duck() :
    dog = Dog()
    with pytest.raises(AttributeError) as excinfo:
        dog.quack()
    assert "'Dog' object has no attribute 'quack'" in str(excinfo.value)


def test_make_dog_duck() :
    dog = Dog()

    def instant_quack():
        return "instant_quack"
    dog.quack = instant_quack
    assert "instant_quack" == dog.quack()

def test_confuse_duck() :
    duck = Duck()
    assert "quack" ==  duck.quack()

    def instant_quack():
        return "wuff"
    duck.quack = instant_quack
    assert "wuff" == duck.quack()


def test_confuse_only_one_duck() :
    duck1 = Duck()
    duck2 = Duck()
    assert "quack" == duck1.quack()
    assert "quack" == duck2.quack()

    def instant_quack():
        return "wuff"
    duck2.quack = instant_quack
    assert "quack" == duck1.quack()
    assert "wuff" == duck2.quack()


def test_break_duck() :
    duck = Duck()
    assert "quack" == duck.quack()
    duck.quack = None

    with pytest.raises(TypeError) as excinfo:
        duck.quack()
    assert "'NoneType' object is not callable" in str(excinfo.value)
