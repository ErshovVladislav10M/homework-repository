from homework4.task_5_optional import fizzbuzz


def test_fizzbuzz():
    generator = fizzbuzz(5)
    assert [next(generator) for i in range(5)] == [1, 2, "fizz", 4, "buzz"]
