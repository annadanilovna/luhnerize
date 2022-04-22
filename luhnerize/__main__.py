#!/usr/bin/env python
"""Generate valid numbers."""

import argparse

from luhnerize import generate


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate valid Luhn numbers")
    parser.add_argument("seed", type=str, help="Seed number")

    args = parser.parse_args()
    numbers = generate(args.seed)
    for number in numbers:
        print(number)
