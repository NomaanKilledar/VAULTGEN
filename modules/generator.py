import secrets
import string


AMBIGUOUS_CHARACTERS = "Il1O0"


def generate_password(
    length=16,
    use_uppercase=True,
    use_lowercase=True,
    use_digits=True,
    use_symbols=True,
    exclude_ambiguous=False,
):
    """Generate a cryptographically secure random password."""

    if length < 4:
        raise ValueError("Password length must be at least 4.")

    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_digits:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    if not character_sets:
        raise ValueError("At least one character type must be enabled.")

    if exclude_ambiguous:
        character_sets = [
            "".join(
                character
                for character in charset
                if character not in AMBIGUOUS_CHARACTERS
            )
            for charset in character_sets
        ]

    if any(not charset for charset in character_sets):
        raise ValueError("No usable characters remain.")

    # Guarantee at least one character from every selected category.
    password_characters = [
        secrets.choice(charset)
        for charset in character_sets
    ]

    all_characters = "".join(character_sets)

    remaining = length - len(password_characters)

    password_characters.extend(
        secrets.choice(all_characters)
        for _ in range(remaining)
    )

    # Securely shuffle the final password.
    secrets.SystemRandom().shuffle(password_characters)

    return "".join(password_characters)