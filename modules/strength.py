import math
import string


def calculate_entropy(password):
    """Estimate password entropy in bits based on its character set."""

    if not password:
        return 0.0

    pool_size = 0

    if any(char in string.ascii_lowercase for char in password):
        pool_size += 26

    if any(char in string.ascii_uppercase for char in password):
        pool_size += 26

    if any(char in string.digits for char in password):
        pool_size += 10

    if any(char in string.punctuation for char in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0.0

    return len(password) * math.log2(pool_size)


def get_strength(password):
    """Return a simple local strength classification."""

    entropy = calculate_entropy(password)

    if entropy < 28:
        return "Very Weak"
    if entropy < 36:
        return "Weak"
    if entropy < 60:
        return "Moderate"
    if entropy < 80:
        return "Strong"

    return "Very Strong"