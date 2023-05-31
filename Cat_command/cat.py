#!/usr/bin/python
"""
python path
"""

import argparse
from pathlib import Path
import sys

class CatError(Exception):
    """Exception class for cat command errors."""

class Logger:
    """Logger class for printing error messages."""
    def __init__(self, verbosity=False):
        self.verbose = verbosity

    @staticmethod
    def error(message):
        """Prints an error message."""
        print(f'ERROR: {message}')

    def dummy_method(self):
        """Dummy method to satisfy pylint warning."""

LOGGER = Logger()

def read_file(src: Path):
    """
    Reads the selected text file.

    Args:
        src (Path): Path to the text file.

    Raises:
        CatError: If the given path is a directory.
    """
    if src.is_dir():
        raise CatError(f'The path {src} is a directory')
    with open(src, 'r') as file:
        for line in file:
            print(line, end='')

def cli() -> argparse.Namespace:
    """
    Parses the command-line arguments.

    Returns:
        argparse.Namespace: Parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        prog='cat',
        description='cat command implementation in python',
        epilog='Example: your/path/file.txt'
    )

    parser.add_argument(
        'source',
        type=Path,
        help='Source file'
    )

    return parser.parse_args()

def main():
    """
    Main function to execute the cat command.
    """
    args = cli()

    try:
        read_file(args.source)
    except CatError as error:
        LOGGER.error(error)
        sys.exit(1)
    except KeyboardInterrupt:
        LOGGER.error('\nInterrupt')

if __name__ == '__main__':
    main()
