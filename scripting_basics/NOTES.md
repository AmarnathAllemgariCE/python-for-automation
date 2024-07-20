# Notes on Scripting Basics

## `hello.py`
- **Purpose:** Demonstrates a basic Python script that prints a message to the console.
- **Key Concept:** This file shows how to write and execute a simple Python script.
- **How to Run:**
  ```sh
  python hello.py
- **Expected Output:**
  ```sh
  Hello, World!
## `greet.py`
- **Purpose:** Illustrates the use of functions and user input.
- **Key Concept:** This script uses the `input()` function to get user input and then calls a function to greet the user.
- **How to Run:**
  ```sh
  python greet.py
  Enter your name: Alice
- **Expected Output:**
  ```sh
  Expected Output: Hello, Alice!
## `script_with_args.py`
- **Purpose:** Shows how to handle command-line arguments in Python.
- **Key Concept:** The script uses `sys.argv` to access command-line arguments passed to the script when executed.
- **How to Run:**
  ```sh
  python script_with_args.py arg1 arg2
- **Expected Output:**
  ```sh 
  Arguments: arg1, arg2
  If no arguments are provided:
  No arguments provided.
## `main.py`
- **Purpose:** Demonstrates the use of the `if __name__ == "__main__":` construct.
- **Key Concept:** This construct ensures that code in this block is only executed when the script is run directly, not when imported as a module.
- **How to Run:**
  ```sh
  python main.py
- **Expected Output:**
  ```sh
  This script is being run directly.
## `greet_with_args.py`
- **Purpose:** Shows how to handle command line arguments in Python.
- **Key Concept:** This script uses `sys.argv` to access command-line arguments passed to the script when executed
- **How to Run:**
  ```sh
  python greet_with_args.py
- **Expected Output:** if right number of arguments are provided.
  ```sh
  Hello, YourName!
- **Expected Output:** if right number of arguments are not provided.
  ```sh
  Usage: python greet_with_args.py <name>

