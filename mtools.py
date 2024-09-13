
def am(input_list):
    """
    Calculate the Arithmetic Mean
    Input: list (list/tupple/set/etc) of numbers
    """
    return sum(input_list) / len(input_list)


def sd(input_list):
    """
    Calculate the Standard Deviation
    Input: list (list/tupple/set/etc) of numbers
    """
    try:
        if len(input_list) < 2:
            print("I need at least 2 numbers to calculate the standard deviation!")
            return
    except:
        print("I need a list of numbers with at least 2 numbers to calculate the standard deviation!")
        return
    mean = am(input_list)
    s = sum([(member - mean) ** 2 for member in input_list])
    n = len(input_list)
    return (s / (n - 1)) ** 0.5


def fibo(input, starting=0):
    """
    Generate Fibonacci sequence
    Input: Lenght of numbers to output
    Optional Input: Starting point:
     - 0: 0 and 1 (default)
     - 1: 1 and 1
     - 2: 1 and 2 (Fibonacci's way)
    """
    if starting not in [0, 1 ,2]:
        print("Invalid starting option. Valid options are:")
        print(" 0 for 0 and 1 (default)")
        print(" 1 for 1 and 1")
        print(" 2 for 1 and 2 (Fibonacci's way)")
    print("So far so good... maybe")

if __name__ == '__main__':
    fibo(8)