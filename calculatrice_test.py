from calculatrice_textuelle import *


def test_empty_string():
    assert add("") == "0"


def test_single_number():
    assert add("3") == "3"


def test_two_numbers():
    assert add("17,3") == "20"


def test_add_many():
    assert add_many("17,3,5,2,3") == "30"


def test_add_return():
    assert add_return("17\n3") == "20"


def test_add_float_end():
    assert add_float_end("17\n3,") == "20"
    assert add_float_end(",") == "0"
