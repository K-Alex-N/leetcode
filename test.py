import pytest

from issue import main


@pytest.mark.parametrize(
    's, j2, res',
    [
        ('ab', "aabbccd", 4),
        ('ab', "aabbccd", 4),
    ]
)
def test_main(s, j2, res):
    assert main(s, j2) == res