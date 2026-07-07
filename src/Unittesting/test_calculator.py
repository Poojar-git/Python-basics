# from calculator import *
# def test_add1():
#     assert add(2,3)==5

# def test_add2():
#     assert add(10,20)==30

# def test_add3():
#     assert add(-2,2)==1

# def test_sub1():
#     assert sub(9,2)==7

# def test_sub2():
#     assert sub(8,0)==8

import pytest
from calculator import add

@pytest.mark.parametrize(
    "a,b,result",
    [
        (2, 3, 5),
        (5, 5, 10),
        (10, 20, 30)
    ]
)
def test_add(a, b, result):
    assert add(a, b) == result
