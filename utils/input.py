def get_integer(prompt, default=None, minimum=None, maximum=None):
    """Safely request an integer from the user."""

    while True:
        value = input(prompt).strip()

        if not value and default is not None:
            return default

        try:
            number = int(value)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if minimum is not None and number < minimum:
            print(f"Value must be at least {minimum}.")
            continue

        if maximum is not None and number > maximum:
            print(f"Value must be at most {maximum}.")
            continue

        return number


def get_yes_no(prompt, default=True):
    """Safely request a yes/no answer."""

    while True:
        value = input(prompt).strip().lower()

        if not value:
            return default

        if value in ("y", "yes"):
            return True

        if value in ("n", "no"):
            return False

        print("Please enter Y or N.")