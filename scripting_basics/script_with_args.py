# script_with_args.py

import sys

def main(args):
    """Print the command-line arguments."""
    if len(args) > 1:
        print(f"Arguments: {', '.join(args[1:])}")
    else:
        print("No arguments provided.")

if __name__ == "__main__":
    main(sys.argv)
