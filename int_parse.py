# This file contains all the functions to parse the input string

from scraper import *


class Variable:
    """Class for a variable (of type int, bool, array, double, string, etc.)

    Attributes
    ----------
    datatype : str
        String representation of the data type of the variable
        Eg: "string", "bool", "int[n]" (for array)
    name : str
        Name of the variable
    """

    def __init__(self, datatype_cpp, datatype_py, name):
        self.datatype_cpp = datatype_cpp
        self.datatype_py = datatype_py
        self.name = name


class Wrapper:
    """Class for a loop including repetitive input

    Attributes
    ----------
    iterations : int
        Number of times the outer loop runs in the wrapper
    *enclosed : tuple of Wrapper and/or Variable objects
        Everything enclosed in the outer loop's body
    """

    def __init__(self, iterations, *enclosed):
        self.iterations = iterations
        self.enclosed = enclosed


# Useful where questions might use words instead of digits for small numbers
text_numbers = {"one": 1,
                "two": 2,
                "three": 3,
                "four": 4,
                "five": 5,
                "six": 6,
                "seven": 7,
                "eight": 8,
                "nine": 9,
                "ten": 10}


# Function to check a line of input for the presence of an array
def check_integer(line):

    is_integer = False
    words = line.split()
    found_index = -1
    n = len(words)
    for i in range(n):
        word = words[i].lower()
        if word == "integer" or word == "number":
            is_integer = True
            found_index = i
            break
    if not is_integer:
        return

    # qty = words[found_index - 1].lower().strip(",$")
    # try:
    #     qty = int(qty)
    # except ValueError:
    #     try:
    #         qty = text_numbers[qty]
    #     except KeyError:
    #         pass
    name = words[found_index + 1].lower().strip(",$")
    # i = name.find('_')
    # if i != -1:
    #     name = name[:i]
    return Variable("int", "int", name)