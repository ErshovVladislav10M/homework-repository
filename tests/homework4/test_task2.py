import os
from unittest import TestCase
from unittest.mock import patch

from homework4.task_2_mock_input import count_dots_on_i


class TestFunc(TestCase):
    @patch(
        "homework4.task_2_mock_input.get_html",
        return_value=open(os.getcwd() + "/homework4/test_task2_html.txt", "rb").read(),
    )
    def test_positive(self, get_html):
        assert count_dots_on_i("https://example.com/") == 59
