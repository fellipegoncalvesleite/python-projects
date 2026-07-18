# Password Generator

A small command-line password generator built with Python's cryptographically
secure `secrets` module. It has no third-party dependencies.

## Requirements

- Python 3.9 or newer

## Usage

Generate one 16-character password:

```bash
python3 password_generator.py
```

Generate five 24-character passwords:

```bash
python3 password_generator.py --length 24 --count 5
```

Exclude symbols:

```bash
python3 password_generator.py --no-symbols
```

Run `python3 password_generator.py --help` to see every option.

## Tests

```bash
python3 -m unittest -v
```
