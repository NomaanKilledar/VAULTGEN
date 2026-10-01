# VAULTGEN

**Secure Password Generator for Windows**

VAULTGEN is a lightweight command-line password utility designed to generate secure random passwords and passphrases locally.

It provides configurable password generation, multiple-password generation, passphrase generation, password strength analysis, and clipboard support through a simple interactive terminal interface.

## Features

* 🔐 Cryptographically secure password generation using Python's `secrets` module
* 🔢 Generate multiple passwords at once
* ⚙️ Custom password generation
* 🔤 Uppercase, lowercase, numbers, and symbols
* 🚫 Optional exclusion of ambiguous characters
* 🧩 Random passphrase generation
* 📊 Password length and entropy analysis
* 📋 Optional clipboard copying
* 🎨 Colored terminal interface
* 🖥️ Standalone Windows executable
* 🚫 Generated passwords are not stored by VAULTGEN

## Menu

```text
[1] Generate Password
[2] Generate Multiple Passwords
[3] Custom Password
[4] Passphrase Generator
[5] Password Strength
[0] Exit
```

## Download

Windows users can download the latest `VAULTGEN.exe` from the project's GitHub Releases page.

The standalone executable does not require a separate Python installation.

## Running from Source

### Requirements

* Python 3.10+
* Windows, Linux, or macOS
* `pyperclip`

### Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/VAULTGEN.git
cd VAULTGEN
```

Install the dependency:

```bash
python -m pip install -r requirements.txt
```

Run VAULTGEN:

```bash
python main.py
```

## Building the Windows Executable

Install PyInstaller:

```bash
python -m pip install pyinstaller
```

Build the executable:

```bash
pyinstaller --onefile --name VAULTGEN main.py
```

The executable will be created in:

```text
dist/VAULTGEN.exe
```

## Security Notes

VAULTGEN generates passwords using Python's `secrets` module, which is intended for security-sensitive random number generation.

VAULTGEN does not maintain a password history or intentionally save generated passwords to disk.

When using clipboard functionality, remember that clipboard contents may be accessible to other applications running on your system.

Password strength and entropy values provided by VAULTGEN are estimates based on the detected character set and password length. They should not be treated as a guarantee of real-world security.

## Project Structure

```text
VAULTGEN/
├── main.py
├── config.json
├── requirements.txt
├── README.md
├── LICENSE
├── modules/
│   ├── __init__.py
│   ├── generator.py
│   ├── passphrase.py
│   └── strength.py
└── utils/
    ├── __init__.py
    ├── colors.py
    ├── config.py
    ├── input.py
    ├── output.py
    └── clipboard.py
```

## License

VAULTGEN is released under the MIT License.

See the `LICENSE` file for details.

## Disclaimer

VAULTGEN is provided as a local password-generation utility. Users are responsible for how they use generated credentials and for following the security policies of the systems and services where they use them.
