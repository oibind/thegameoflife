from thegameoflife import *


def test_field_insert():
    field = Field()
    field.add(0, 0)
    assert field.get((0, 0)) is not None


def test_cell_ns():
    field = Field()
    field.add(0, 0)
    field.add(0, 1)
    assert len(field.get((0, 0)).ns()) == 1


def test_lives():
    field = Field()
    field.add(1, 0)
    field.add(1, 1)
    field.add(0, 0)
    field.add(2, 0)
    field.add(3, 0)
    assert field.get((3, 0)).lives() == False
