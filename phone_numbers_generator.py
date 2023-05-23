import random


def generate_phone_numbers(cant: int) -> list:
    phone_numbers = []
    for i in range(cant):
        digits = [random.randint(0, 9) for _ in range(10)]
        phone_number = "+57{}{}{}{}{}{}{}{}{}{}".format(*digits)
        phone_numbers.append(phone_number)

    return phone_numbers
