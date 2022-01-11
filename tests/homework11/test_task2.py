from homework11.task2 import Order


def morning_discount(order):
    return order.price * 0.25


def elder_discount(order):
    return order.price * 0.9


def test_order_1():
    order_1 = Order(100, morning_discount)
    assert order_1.final_price() == 75


def test_sizes_enum():
    order_2 = Order(100, elder_discount)
    assert order_2.final_price() == 10
