from utils.clipboard import copy_to_clipboard
from modules.generator import generate_password
from modules.passphrase import generate_passphrase
from modules.strength import get_strength, calculate_entropy
from utils.colors import Colors
from utils.input import get_integer, get_yes_no
from utils.config import get_config


def clear_screen():
    print("\033[2J\033[H", end="")


def banner():
    print(
        f"{Colors.CYAN}{Colors.BOLD}"
        "╔══════════════════════════════════════════╗\n"
        "║                 VAULTGEN                 ║\n"
        "║       SECURE PASSWORD GENERATOR          ║\n"
        "╚══════════════════════════════════════════╝"
        f"{Colors.RESET}"
    )


def generate_password_menu():
    clear_screen()
    banner()

    print(f"\n{Colors.YELLOW}PASSWORD GENERATOR{Colors.RESET}\n")

    default_length = get_config(
        "generator",
        "default_length",
        16,
    )

    max_length = get_config(
        "generator",
        "max_length",
        512,
    )

    length = get_integer(
        f"Password length [{default_length}]: ",
        default=default_length,
        minimum=4,
        maximum=max_length,
    )

    uppercase = get_yes_no(
        "Include uppercase? [Y]: ",
        True,
    )

    lowercase = get_yes_no(
        "Include lowercase? [Y]: ",
        True,
    )

    digits = get_yes_no(
        "Include numbers? [Y]: ",
        True,
    )

    symbols = get_yes_no(
        "Include symbols? [Y]: ",
        True,
    )

    default_ambiguous = get_config(
        "generator",
        "exclude_ambiguous",
        False,
    )

    ambiguous = get_yes_no(
        f"Exclude ambiguous characters "
        f"[{'Y' if default_ambiguous else 'N'}]: ",
        default_ambiguous,
    )

    try:
        password = generate_password(
            length=length,
            use_uppercase=uppercase,
            use_lowercase=lowercase,
            use_digits=digits,
            use_symbols=symbols,
            exclude_ambiguous=ambiguous,
        )
    except ValueError as exc:
        print(f"\n{Colors.RED}Error: {exc}{Colors.RESET}")
        input("\nPress Enter to continue...")
        return

    print(f"\n{Colors.GREEN}Generated Password:{Colors.RESET}")
    print(f"\n  {password}\n")
    if get_yes_no("Copy password to clipboard? [Y]: ", True):
        if copy_to_clipboard(password):
            print(f"{Colors.GREEN}Copied to clipboard.{Colors.RESET}")
        else:
            print(f"{Colors.RED}Could not copy to clipboard.{Colors.RESET}")


def multiple_passwords_menu():
    clear_screen()
    banner()

    print(f"\n{Colors.YELLOW}MULTIPLE PASSWORDS{Colors.RESET}\n")

    count = get_integer(
        "Number of passwords [5]: ",
        default=5,
        minimum=1,
        maximum=100,
    )

    default_length = get_config(
        "generator",
        "default_length",
        16,
    )

    max_length = get_config(
        "generator",
        "max_length",
        512,
    )

    length = get_integer(
        f"Password length [{default_length}]: ",
        default=default_length,
        minimum=4,
        maximum=max_length,
    )

    print()

    for index in range(1, count + 1):
        password = generate_password(length)
        print(f"{index:>3}. {password}")

    print()


def custom_password_menu():
    clear_screen()
    banner()

    print(f"\n{Colors.YELLOW}CUSTOM PASSWORD{Colors.RESET}\n")

    default_length = get_config(
        "generator",
        "default_length",
        20,
    )

    max_length = get_config(
        "generator",
        "max_length",
        512,
    )

    length = get_integer(
        f"Password length [{default_length}]: ",
        default=default_length,
        minimum=4,
        maximum=max_length,
    )

    uppercase = get_yes_no(
        "Uppercase? [Y]: ",
        True,
    )

    lowercase = get_yes_no(
        "Lowercase? [Y]: ",
        True,
    )

    digits = get_yes_no(
        "Numbers? [Y]: ",
        True,
    )

    symbols = get_yes_no(
        "Symbols? [Y]: ",
        True,
    )

    default_ambiguous = get_config(
        "generator",
        "exclude_ambiguous",
        False,
    )

    ambiguous = get_yes_no(
        f"Exclude ambiguous characters "
        f"[{'Y' if default_ambiguous else 'N'}]: ",
        default_ambiguous,
    )

    try:
        password = generate_password(
            length=length,
            use_uppercase=uppercase,
            use_lowercase=lowercase,
            use_digits=digits,
            use_symbols=symbols,
            exclude_ambiguous=ambiguous,
        )

        print(f"\n{Colors.GREEN}Generated:{Colors.RESET}")
        print(f"\n  {password}\n")
        if get_yes_no("Copy password to clipboard? [Y]: ", True):
            if copy_to_clipboard(password):
                print(f"{Colors.GREEN}Copied to clipboard.{Colors.RESET}")
            else:
                print(f"{Colors.RED}Could not copy to clipboard.{Colors.RESET}")

    except ValueError as exc:
        print(f"\n{Colors.RED}Error: {exc}{Colors.RESET}\n")


def passphrase_menu():
    clear_screen()
    banner()

    print(f"\n{Colors.YELLOW}PASSPHRASE GENERATOR{Colors.RESET}\n")

    default_words = get_config(
        "passphrase",
        "default_words",
        4,
    )

    words = get_integer(
        f"Number of words [{default_words}]: ",
        default=default_words,
        minimum=2,
        maximum=20,
    )

    default_separator = get_config(
        "passphrase",
        "separator",
        "-",
    )

    separator = input(
        f"Separator [{default_separator}]: "
    ).strip() or default_separator

    capitalize = get_yes_no(
        "Capitalize words? [N]: ",
        False,
    )

    add_number = get_yes_no(
        "Add a number? [N]: ",
        False,
    )

    try:
        phrase = generate_passphrase(
            word_count=words,
            separator=separator,
            capitalize=capitalize,
            add_number=add_number,
        )

        print(f"\n{Colors.GREEN}Generated Passphrase:{Colors.RESET}")
        print(f"\n  {phrase}\n")
        if get_yes_no("Copy passphrase to clipboard? [Y]: ", True):
            if copy_to_clipboard(phrase):
                print(f"{Colors.GREEN}Copied to clipboard.{Colors.RESET}")
            else:
                print(f"{Colors.RED}Could not copy to clipboard.{Colors.RESET}")

    except ValueError as exc:
        print(f"\n{Colors.RED}Error: {exc}{Colors.RESET}\n")


def strength_menu():
    clear_screen()
    banner()

    print(f"\n{Colors.YELLOW}PASSWORD STRENGTH{Colors.RESET}\n")

    password = input("Enter password to analyze: ")

    entropy = calculate_entropy(password)
    strength = get_strength(password)

    print(f"\nLength       : {len(password)}")
    print(f"Entropy      : {entropy:.2f} bits")
    print(f"Strength     : {strength}\n")


def main_menu():
    while True:
        clear_screen()
        banner()

        print(
            f"\n{Colors.WHITE}"
            "[1] Generate Password\n"
            "[2] Generate Multiple Passwords\n"
            "[3] Custom Password\n"
            "[4] Passphrase Generator\n"
            "[5] Password Strength\n"
            "[0] Exit"
            f"{Colors.RESET}"
        )

        choice = input(
            f"\n{Colors.GREEN}VAULTGEN > {Colors.RESET}"
        ).strip()

        if choice == "1":
            generate_password_menu()
            input("Press Enter to continue...")

        elif choice == "2":
            multiple_passwords_menu()
            input("Press Enter to continue...")

        elif choice == "3":
            custom_password_menu()
            input("Press Enter to continue...")

        elif choice == "4":
            passphrase_menu()
            input("Press Enter to continue...")

        elif choice == "5":
            strength_menu()
            input("Press Enter to continue...")

        elif choice == "0":
            print("\nGoodbye.")
            break

        else:
            print(
                f"\n{Colors.RED}Invalid option.{Colors.RESET}"
            )
            input("Press Enter to continue...")


if __name__ == "__main__":
    main_menu()