# multiplication_table.py
def print_table(number):
    print(f"Multiplication Table of {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

# Main program
if __name__ == "__main__":
    number = 5  # You can change the number or pass it as an argument
    print_table(number)
