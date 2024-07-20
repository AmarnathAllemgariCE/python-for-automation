#greet_with_args.py

import sys

def greet_user(name):
    '''Greet the user with their name.'''
    print(f"Hello, {name}!")

def main():
    '''Main function to handle command-line arguments and greet the user.'''
    if len(sys.argv) != 2:
        print("Usage: python greet.py <name>")
        sys.exit(1)
    name = sys.argv[1]
    greet_user(name)
    
if __name__ == '__main__':
    main()