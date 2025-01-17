from homework6.counter import instances_counter


@instances_counter
class User:
    pass


def test_instances_counter():
    user, _, _ = User(), User(), User()
    assert (
        User.get_created_instances() == 3
        and user.get_created_instances() == 3
        and User.reset_instances_counter() == 3
        and User.get_created_instances() == 0
    )
