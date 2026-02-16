def collatz(x):
    result = x // 2 if x % 2 == 0 else (3 * x) + 1
    print(result)
    return result

# Get valid input
while True:
    try:
        p = int(input("Heyy! give me a number and I will run the collatz sequence on it: "))
        if p >= 1:
            break
        print("Don't fuck with me! Anything less than 1 is not allowed >:[")
    except ValueError:
        print("Don't fuck with me! strings are not allowed >:[")

# Run Collatz
while p != 1:
    p = collatz(p)

input("Press enter to exit!")