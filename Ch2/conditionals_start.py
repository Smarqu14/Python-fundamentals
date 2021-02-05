#
# Example file for working with conditional statements
#


def main():
    x, y = 100, 10

    # Doesnt have switch statements
    # conditional flow uses if, elif, else
    if (x < y):
        st = 'x is less than y'
    elif (x == y):
        st = 'X is greater than y'
    else:
        st = "They are greater"

    print(st)

# Ternary condioning
    # conditional statements let you use "a if C else b"
    st = 'X is less than Y' if (
        x < y) else "x is greater than or the same as y"
    print(st)


if __name__ == "__main__":
    main()
