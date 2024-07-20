def add(x, y):
    """Return the sum of x and y."""
    return x + y

def sub(x, y):
    """Return the difference between x and y."""
    return x - y

def main():
    """Run the calculator script and display addition and subtraction results."""
    print("Running Calculator script")
    x, y = 5, 3
    print(f'{x} + {y} = {add(x, y)}')
    print(f'{x} - {y} = {sub(x, y)}')

if __name__ == "__main__":
    main()
