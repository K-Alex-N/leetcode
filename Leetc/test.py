import pytest

from Leetc.problem import Solution


@pytest.mark.parametrize(
    'a, b, res',
    [
        ([3, 2, 2, 3], 3, 2),
        # ('ab', "aabbccd", 4),
    ]
)
def test_main(a, b, res):
    solution = Solution()
    assert solution.removeElement(a, b) == res
