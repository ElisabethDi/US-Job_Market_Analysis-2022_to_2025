# Import Libraries
import pytest
from extract_role import extract_role


@pytest.mark.parametrize('input_title, expected', [
    (None, None),
    ('  Senior DATA Analyst   '    , 'Data Analyst'),
    ('Junior Data Engineer', 'Data Engineer'),
    ('Marketing analyst position', 'Marketing Analyst'),
    ('Completely unrelated', 'completely unrelated')
])
def test_extract_role(input_title, expected):
    assert extract_role(input_title) == expected
