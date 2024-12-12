def golrang_zero():
    pattern = ["***", "*.*", "***"]
    zero = ("\n".join(pattern))
    return(zero)

def golrang_one():
    pattern = [".*.", ".*.", ".*."]
    one = ("\n".join(pattern))
    return(one)

input1 = int(input("Enter the length of the string (1-100): "))
if input1 < 1 or input1 > 100:
    print("Out of range!")
    exit()
input2 = input("Enter a binary string: ")
for binary in input2:
    if binary not in ['0', '1']:
        print("Not a binary number!")
        exit()
if len(input2) != input1:
    print("The length of binary number does not match the entered length!")
    exit()

for row in range(3):
    for digit in input2:
        if digit == "0":
            print(golrang_zero().splitlines()[row], end="")
        elif digit == "1":
            print(golrang_one().splitlines()[row], end="")
    print()