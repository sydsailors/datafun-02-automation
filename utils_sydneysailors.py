"""
File: utils_sydneysailors.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Author: Sydney Sailors
"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# See more at: https://docs.python.org/3/library/

import statistics


#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
has_a_nursery_unit: bool = True

# declare an integer variable 
years_in_operation: int = 127

# declare a floating point variable
average_length_of_stay: float = 97.7

# declare a list of strings  
levels_offered: list = ["Well-Baby Nursery", "Special Care Nursery", "Neonatal Intensive Care Unit", "Regional Neonatal Intensive Care Unit"]

# declare a list of numbers so we can illustrate statistics skills  
length_of_stay: list = [1, 28, 127, 365, 50, 15]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(length_of_stay)  
max_score: float = max(length_of_stay)  
mean_score: float = statistics.mean(length_of_stay)  
stdev_score: float = statistics.stdev(length_of_stay)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Regional Hospitals - NICU Analytics
---------------------------------------------------------
Has A Nursery Unit:         {has_a_nursery_unit}
Years in Operation:         {years_in_operation}
Levels Offered:             {levels_offered}
Length of Stay:             {length_of_stay}
Minimum Length of Stay:     {min_score}
Maximum Length of Stay:     {max_score}
Mean Length of Stay:        {mean_score:.2f}
Standard Deviation of Length of Stay: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_sydneysailors.py")
    print(get_byline())
    print("END main() in utils_sydneysailors.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()