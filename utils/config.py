import json


DEFAULT_CONFIG = {
    "app": {
        "name": "VAULTGEN",
        "version": "1.0.0"
    },
    "generator": {
        "default_length": 16,
        "max_length": 512,
        "exclude_ambiguous": True
    },
    "passphrase": {
        "default_words": 4,
        "separator": "-"
    }
}


def load_config():
    """Return the built-in VAULTGEN configuration."""
    return DEFAULT_CONFIG


def get_config(section, key, default=None):
    """Get a configuration value safely."""

    config = load_config()
    section_data = config.get(section, {})

    if not isinstance(section_data, dict):
        return default

    return section_data.get(key, default)