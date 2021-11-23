from unittest.mock import patch

import homework4.task_2_mock_input


@patch("homework4.task_2_mock_input.count_dots_on_i", return_value=59)
def test_positive(self, count_dots_on_i):
    assert count_dots_on_i("https://example.com/") == 59
