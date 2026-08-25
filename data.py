import random
import string


def generate_email():
    random_numbers = random.randint(100, 999)
    return f"georgiy_kayshev_52_{random_numbers}@yandex.ru"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))