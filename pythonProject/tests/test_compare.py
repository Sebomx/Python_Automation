import pytest

@pytest.mark.great
def test_greater():
    num = 100
    assert num > 100

@pytest.mark.great
def test_greater_equal():
    num = 100
    assert num >= 100

@pytest.mark.others
def test_greater_not_equal():
    num = 100
    assert num < 200

# pytest test_compare.py -v (для запуска тестов по названию файла)
#  pytest -k great -v (для запуска тестов по ключевому слову great)

