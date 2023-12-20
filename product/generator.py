import random
import string
from time import time

def generate_sku(prefix='', length=8):
    timestamp = int(time())
    unique_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
    return f"{prefix}{unique_id}{timestamp}"