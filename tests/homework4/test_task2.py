from unittest import TestCase
from unittest.mock import patch

from homework4.task_2_mock_input import count_dots_on_i


class TestFunc(TestCase):
    @patch("homework4.task_2_mock_input.count_dots_on_i", return_value=59)
    def test_positive(self, count_dots_on_i):
        assert count_dots_on_i("https://example.com/") == 59
