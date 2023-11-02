def main():
    """This function should
    return the values of a 
    and b, respectively.
    """
    a = 12
    b = 2
    print(f"{a * b}")


main()


def positioned(first, second):
    # assignment based on order
    print(f"first: {first}")
    print(f"second: {second}")


positioned(1, 2)


def keyword(first=1, second=2):
    # default values assigned
    print(f"first: {first}")
    print(f"second: {second}")


keyword(0)
keyword(3, 4)
keyword(second=True, first=9)
