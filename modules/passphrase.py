import secrets


DEFAULT_WORDS = [
    "amber", "anchor", "apple", "arrow", "autumn",
    "beacon", "blue", "breeze", "bridge", "cactus",
    "candle", "cloud", "comet", "coral", "crystal",
    "desert", "dragon", "dream", "eagle", "ember",
    "forest", "frost", "galaxy", "garden", "gold",
    "harbor", "hazel", "island", "jungle", "lantern",
    "maple", "meadow", "meteor", "moon", "ocean",
    "orange", "pebble", "planet", "rain", "river",
    "rocket", "shadow", "silver", "sky", "solar",
    "stone", "storm", "sunset", "thunder", "violet",
]


def generate_passphrase(
    word_count=4,
    separator="-",
    capitalize=False,
    add_number=False,
):
    """Generate a random passphrase from the built-in word list."""

    if word_count < 2:
        raise ValueError("Word count must be at least 2.")

    if not separator:
        raise ValueError("Separator cannot be empty.")

    words = [
        secrets.choice(DEFAULT_WORDS)
        for _ in range(word_count)
    ]

    if capitalize:
        words = [word.capitalize() for word in words]

    if add_number:
        words.append(str(secrets.randbelow(100)))

    return separator.join(words)