
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