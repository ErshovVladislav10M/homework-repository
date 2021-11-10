import pytest
from taks.task05 import find_maximal_subarray_sum


@pytest.mark.parametrize(
    "input_data, output_data",
    [(([0, 1, -10, 2, 5], 3), 8),
     (([0, -12, -10, 22, 5], 3), 27)]
)
def test_find_maximal_subarray_sum(input_data, output_data):
    assert find_maximal_subarray_sum(input_data) == output_data