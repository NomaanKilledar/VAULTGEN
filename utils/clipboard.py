import pyperclip


def copy_to_clipboard(text):
    """Copy text to the system clipboard."""
    if not text:
        return False

    try:
        pyperclip.copy(text)
        return True
    except pyperclip.PyperclipException:
        return False