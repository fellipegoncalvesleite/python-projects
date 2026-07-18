#!/usr/bin/env python3
"""Generate cryptographically secure passwords from the command line."""

from __future__ import annotations

import argparse
import secrets
import string
from collections.abc import Sequence


SYMBOLS = "!@#$%^&*()-_=+[]{};:,.?"


def generate_password(
    length: int = 16,
    *,
    uppercase: bool = True,
    lowercase: bool = True,
    digits: bool = True,
    symbols: bool = True,
) -> str:
    """Return a secure password containing every enabled character type."""
    groups = []
    if uppercase:
        groups.append(string.ascii_uppercase)
    if lowercase:
        groups.append(string.ascii_lowercase)
    if digits:
        groups.append(string.digits)
    if symbols:
        groups.append(SYMBOLS)

    if not groups:
        raise ValueError("Enable at least one character type.")
    if length < len(groups):
        raise ValueError(
            f"Length must be at least {len(groups)} to include every enabled type."
        )

    password = [secrets.choice(group) for group in groups]
    alphabet = "".join(groups)
    password.extend(secrets.choice(alphabet) for _ in range(length - len(groups)))
    secrets.SystemRandom().shuffle(password)
    return "".join(password)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate secure random passwords.")
    parser.add_argument(
        "-l", "--length", type=int, default=16, help="password length (default: 16)"
    )
    parser.add_argument(
        "-n", "--count", type=int, default=1, help="number of passwords (default: 1)"
    )
    parser.add_argument("--no-uppercase", action="store_true")
    parser.add_argument("--no-lowercase", action="store_true")
    parser.add_argument("--no-digits", action="store_true")
    parser.add_argument("--no-symbols", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.count < 1:
        raise SystemExit("Count must be at least 1.")

    try:
        for _ in range(args.count):
            print(
                generate_password(
                    args.length,
                    uppercase=not args.no_uppercase,
                    lowercase=not args.no_lowercase,
                    digits=not args.no_digits,
                    symbols=not args.no_symbols,
                )
            )
    except ValueError as error:
        raise SystemExit(str(error)) from error

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
