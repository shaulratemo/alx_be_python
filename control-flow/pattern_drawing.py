size = int(input("Enter the size of the pattern: "))
rows = 1

while rows <= size:
    for i in range(1, size + 1):
        print("*", end="")
    rows += 1
    print()