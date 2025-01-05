import string
import random

def generate_random_code(length=6):
    """Generate a random short code of specified length."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
