"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    cls.counter_class_instance = 0

    cls.base_init = cls.__init__

    def new_init(*args):
        cls.counter_class_instance += 1
        cls.base_init(args)

    cls.__init__ = new_init

    def get_created_instances(*kwargs):
        return cls.counter_class_instance

    cls.get_created_instances = get_created_instances

    def reset_instances_counter(*kwargs):
        num_of_class_instance = cls.counter_class_instance
        cls.counter_class_instance = 0
        return num_of_class_instance

    cls.reset_instances_counter = reset_instances_counter

    return cls
