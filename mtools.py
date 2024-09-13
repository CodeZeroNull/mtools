
def numbercheck(input_list):
    try:
        sum(input_list)
        return True
    except:
        return False

def am(input_list):
    """
    Calculate the Arithmetic Mean
    Input: list (list/tupple/set/etc) of numbers
    """
    if numbercheck(input_list) == False:
        print("I need a list of numbers as input.")
        print("Your input was:", input_list)
        return
    return sum(input_list) / len(input_list)


def sd(input_list):
    """
    Calculate the Standard Deviation
    Input: list (list/tupple/set/etc) of numbers
    """
    if numbercheck(input_list) == False:
        print("I need a list of numbers as input.")
        print("Your input was:", input_list)
        return
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

if __name__ == '__main__':
    A = [1, "2", 7]
    print("For A defined as", A)
    print("The mean is", am(A))
    print("The standard deviation is", sd(A))

def fibo(length, starting=0):
    """
    Generate Fibonacci sequence
    Input: Lenght of numbers to output
    Optional Input: Starting point:
     - 0: 0 and 1 (default)
     - 1: 1 and 1
     - 2: 1 and 2 (Fibonacci's way)
    """
    
    if starting == 0:
        num1 = 0
        num2 = 1
    elif starting == 1:
        num1 = 1
        num2 = 1
    elif starting == 2:
        num1 = 1
        num2 = 2
    else:
        print("Invalid starting option. Valid options are:")
        print(" 0 for 0 and 1 (default)")
        print(" 1 for 1 and 1")
        print(" 2 for 1 and 2 (Fibonacci's way)")
    
    if length < 1:
        print("I need the series to have a non-zero length.")
        return
    elif length == 1:
        print(num1)
        return
    elif length == 2:
        print(num1, num2)
        return

    else:
        next_number = num1 + num2
        count = 0
        print(num1, end=" ")
        print(num2, end=" ")
        while count <= length - 3:
            print(next_number, end=" ")
            count += 1
            num1, num2 = num2, next_number
            next_number = num1 + num2
    print()
    

