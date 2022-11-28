from typing import List

def get_divisors(triangle: int) -> List[int]:
    """
    Calculate and list divisords for triangle.
    Only search divisors from below triangle/2,
    since higher numbers cannot be divisords.
    """
    divisors = []
    for i in range(1, int(triangle/2) + 1):
        if triangle % i == 0:
            divisors.append(i)
    divisors.append(triangle)
    return divisors

def to_string(divisors: List[int]) -> str:
    """
    Divisors as numbers are logically casted as int. 
    This function converts them to str for printing and file writing.
    """
    return(",".join(str(div) for div in divisors ))

def get_triangle(ordinal: int) -> int:
    """ Calculate triangle number from ordinal"""
    return sum(range(1, ordinal + 1))

def get_ordinal_by_divisors(num_of_divisors: int) -> List[int]:
    """ Find the first ordinal of triangle that has given num of divisors"""
    i=1
    while len(get_divisors(get_triangle(i))) < num_of_divisors:
        i += 1
    return i

def save_file(ordinal: int, triangle:int, divisors: List[int]):
    """ Save triangle number and divisors to txt file """
    file_name = f"Divisors and sum of {ordinal}th term.txt"
    with open(file_name, 'w') as f:
        f.write(": ".join([str(triangle), to_string(divisors)]))

def execute(ordinal: int):
    """ Execute calculations from given ordinal. Print and save results. """
    triangle = get_triangle(ordinal)
    divisors = get_divisors(triangle)
    print(": ".join([str(triangle), to_string(divisors)])+"\n")
    save_file(ordinal, triangle, divisors)

def main():
    print("Highly Divisible Triangular Number Calculator v.1.0\n")

    while True:
        option = input(
        "What would desire, sir?\n"
        "(1) Calculate triangle and divisors from ordinal number\n"
        "(2) Calculate triangle and divisors from minimum number of divisors\n"
        "(q) quit\n"
        )
        try:
            if option == "1":
                arg = input("Please give the ordinal number\n")
                execute(int(arg))
            
            elif option == "2":
                arg = input("Please give minimum number of divisors for triangle number\n")
                execute(get_ordinal_by_divisors(int(arg)))

            elif option == "q":
                print("Good bye!\n")
                break

            else:
                print("Wrong input parameter. Please try again\n")
        
        except ValueError:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
