import random
import uuid


def random_string():
    return uuid.uuid4().hex


def random_int(max_value=100):
    return random.randint(0, max_value)


def random_float(max_value=100.0):
    return round(random.uniform(0, max_value), 2)


def random_boolean():
    return random.choice([True, False])


def random_nested_object():
    return {
        "nested_str": random_string(),
        "nested_int": random_int(),
        "nested_float": random_float()
    }
