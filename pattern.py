for i in range(1, 6):

    # Pattern 1 (stars)
    if i <= 4:
        col1 = "*" * i
    else:
        col1 = ""

    # Pattern 2 (numbers 1 to i)
    col2 = "".join(str(j) for j in range(1, i + 1))

    # Pattern 3 (letters A to ...)
    col3 = "".join(chr(64 + j) for j in range(1, i + 1))

    # Pattern 4 (5 repeated)
    col4 = "5" * i

    # Pattern 5 (reverse stars)
    col5 = "*" * (6 - i)

    print(f"{col1:<6}{col2:<10}{col3:<10}{col4:<10}{col5}")