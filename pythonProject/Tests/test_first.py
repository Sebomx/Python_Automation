import pytest
from contextlib import nullcontext as does_not_raise



# from src.main import A
#
# def test_main():
#     assert A.x==1


def test_sum():
    x = 1
    y = 2
    assert x + y == 3

def test_devision():
    x = 1
    y = 2
    assert x / y == 0.5

# test_calculator



from src.main import Calculator
class TestCalculator:
    @pytest.mark.parametrize(   #Параметризация данных
        "x, y, res, expectation",
        [
        (1, 2, 0.5, does_not_raise()),
        (5, -1, -5, does_not_raise()),
        (5, "-1", -5, pytest.raises(TypeError)),
        ]
    )
    def test_divide(self, x, y, res, expectation):
        with expectation:  #pytest.raises(TypeError): пример без использования does_not_raise
#    x = 1
#    y = 2
#    res = 0.5
            assert Calculator().divide(x, y) == res

    @pytest.mark.parametrize(
        "x, y, res, expectation",
        [
            (3, 2, 5, does_not_raise()),
            (4, -2, 2, does_not_raise()),
            (5, "-3", -2, pytest.raises(TypeError)),
        ]
    )
    def test_add(self, x, y, res, expectation):
        with expectation:
            assert Calculator().add(x, y) == res


#-----------------------------------------------------------------------------------------
# test_assert_examples.py
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"
def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]
def test_some_primes():
    assert 37 in {
        num
        for num in range(2, 50)
        if not any(num % div == 0 for div in range(2, num))
    }



