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

@pytest.mark.parametrize(
    "num",
    [-1, 0, 1, 99, 100, 101, 199, 200, 201]
)
def multi_test(num):
    if num < 100:
        response = 'low'
        assert response == "low", f"Полученный результат отличен от low, {response}"
    elif 100 <= num <= 200:
        response = 'medium'
        assert response == "medium", f"Полученный результат отличен от medium, {response}"
    else:
        response = 'high'
        assert response == "high", f"Полученный результат отличен от high, {response}"


