#!/usr/bin/env python3
"""Main entry point for {{ project_name }}."""

import argparse
import sys
from typing import Optional


def main(argv: Optional[list[str]] = None) -> int:
    """Main entry point for {{ project_name }}.
    
    Args:
        argv: Command line arguments. If None, uses sys.argv[1:].
        
    Returns:
        int: Exit code (0 for success, non-zero for failure).
    """
    parser = argparse.ArgumentParser(
        description="{{ project_description|default('A Python project for ' + project_name) }}",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.0.1",
    )
    
    # Add your command line arguments here
    # parser.add_argument("input", help="Input file path")
    # parser.add_argument("--output", "-o", help="Output file path")
    
    args = parser.parse_args(argv)
    
    # Your main logic here
    print("Hello from {{ project_name }}!")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())