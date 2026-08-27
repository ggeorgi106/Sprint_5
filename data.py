import random
import string


BASE_URL = "https://stellarburgers.education-services.ru/"


def generate_email():
    random_numbers = random.randint(100000, 999999)
    return f"georgiy_kayshev_52_{random_numbers}@yandex.ru"


def generate_password():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=6))