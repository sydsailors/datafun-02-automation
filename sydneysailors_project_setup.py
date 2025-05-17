"""
File: sydneysailors_project_setup.py

Purpose: Automate the creation of project folders 
(and demonstrate basic Python coding skills).

Hint: See the Textbook, Skill Drills, and GUIDES for code snippets to help complete this module.

Author: Sydney Sailors
  
"""

#####################################
# Import Modules at the Top
#####################################

import os 
import time

# Import from the Python Standard library
import pathlib
import sys      

# Import packages from requirements.txt
import loguru   

# Ensure project root is in sys.path for local imports
sys.path.append(str(pathlib.Path(__file__).resolve().parent))

# Import local modules
import utils_sydneysailors

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare global variables
#####################################

# Create a project path object for the root directory of the project.
ROOT_DIR = pathlib.Path.cwd()

HOSPITALS = [
    "University of Kansas Medical Center", 
    "Childrens Mercy",  
    "Overland Park Regional", 
    "Advent Health Shawnee Mission", 
    "University Health"
]

#####################################
# Define Function 1. For item in Range: 
# Create a function to generate folders for a given range (e.g., minutes).
# Pass in an int for the minimum minute
# Pass in an int for the maximum minute
#####################################

def create_folders_for_range(minutes_min: int, minutes_max: int) -> None:
    '''
    Create folders for a given range of minutes.

    Arguments:
    minutes_min -- The minimum amount of time to drive to a hospital of the range (inclusive).
    minutes_max -- The maximum amount of time to drive to a hospital of the range (inclusive).
    '''

    # Log function name and parameters
    logger.info("FUNCTION: create_folders_for_range()")
    logger.info(f"PARAMETERS: minutes_min = {minutes_min}, minutes_max = {minutes_max}")

    for minutes in range(minutes_min, minutes_max +1):
        minutes_path = ROOT_DIR / str(minutes)
        minutes_path.mkdir(exist_ok=True)
        print(f"Created folder: {minutes_path}")


  
#####################################
# Define Function 2. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# After everything else is working, 
# add options to force lowercase and remove spaces
#####################################

def create_folders_from_list(folder_list: list) -> None:
    '''
    Create folders based on a list of folder names.
    
    Arguments:
    folder_list -- A list of strings representing folder names.
    '''

    logger.info("FUNCTION: create_folders_from_list()")
    logger.info(f"PARAMETER: folder_list = {folder_list}")

   
    for name in folder_list:
        name_path = ROOT_DIR / str(name)
        name_path.mkdir(exist_ok=True)
        print(f"Created folder: {name_path}")
        name2 = [item.lower() for item in name]
        print('data-csv', 'data-excel', 'data-json', sep='  ')

    pass





#####################################
# Define Function 3. List Comprehension: 
# Create a function to create prefixed folders by transforming a list of names 
# and combining each with a prefix (e.g., "output-").
# Pass in a list of folder names
# Pass in a prefix (e.g. 'output-') to add to each
#####################################

def create_prefixed_folders_using_list_comprehension(folder_list: list, prefix: str) -> None:
    '''
    Create folders by adding a prefix to each item in a list 
    using a concise form of a for loop called a list comprehension.

    Arguments:
    folder_list -- A list of strings (e.g., ['csv', 'excel']).
    prefix -- A string to prefix each name (e.g., 'output-').
    '''

    logger.info("FUNCTION: create_prefixed_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, prefix = {prefix}")

    
    #List comprehension 
    for name in folder_list:
        name_path = ROOT_DIR / str(name)
        name_path.mkdir(exist_ok=True)
        print(f"Created folder: {name_path}")
        name2 = [item.lower() for item in name]
        print('csv', 'excel', 'json', sep='  ')
        

    pass

  

#####################################
# Define Function 4. While Loop: 
# Write a function to create folders periodically 
# (e.g., one folder every 5 seconds).
# Pass in the wait time in seconds
#####################################


def create_folders_periodically(duration_seconds: int) -> None:
    '''
    Create folders periodically over time.

    Arguments:
    duration_seconds -- The number of seconds to wait between folder creations.
    '''

    logger.info("FUNCTION: create_folders_periodically()")
    logger.info(f"PARAMETER: duration_seconds = {duration_seconds}")


    count = 5
    max_folders = 5
    while count <= max_folders: 
        folder_name = f"folder_{count}"
        if count <= max_folders:
            logger.info(f"Waiting for {duration_seconds} seconds before creating next folder")
            time.sleep(duration_seconds)
    
    pass

#####################################
# Define Function 5. For Item in List: 
# Create folders from a list of names.
# Pass in a list of folder names 
# Add options to force lowercase AND remove spaces
#####################################

def create_standardized_folders(folder_list: list, to_lowercase: bool = False, remove_spaces: bool = False) -> None:
    '''
    Create folders from a list of names with options to standardize names.

    Arguments:
    folder_list -- A list of strings representing folder names.
    to_lowercase -- If True, convert names to lowercase.
    remove_spaces -- If True, remove spaces from names.
    '''

    logger.info("FUNCTION: create_standardized_folders()")
    logger.info(f"PARAMETERS: folder_list = {folder_list}, to_lowercase = {to_lowercase}, remove_spaces = {remove_spaces}")

    if to_lowercase:
        folder_list = [name.lower() for name in folder_list]

    if remove_spaces:
        folder_list = [name.replace(' ','') for name in folder_list]

    for name in folder_list:
        name_path = ROOT_DIR / str(name)
        name_path.mkdir(exist_ok=True)
        print(f"Created folder: {name_path}")
    

    pass
  
#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    ''' Main function to demonstrate module capabilities. '''

    logger.info("#####################################")
    logger.info("# Starting execution of main()")
    logger.info("#####################################\n")

    logger.info(f"Byline: {utils_sydneysailors.get_byline()}")

    # Call function 1 to create folders for a range (e.g. minutes away)
    create_folders_for_range(minutes_min=11, minutes_max=26)

    # Call function 2 to create folders given a list
    folder_names = ['data-csv', 'data-excel', 'data-json']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using list comprehension
    folder_names = ['csv', 'excel', 'json']
    prefix = 'output-'
    create_prefixed_folders_using_list_comprehension(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs:int = 5  # duration in seconds
    create_folders_periodically(duration_secs)

    # Call function 5 to create standardized folders, no spaces, lowercase
    create_standardized_folders(HOSPITALS, to_lowercase=True, remove_spaces=True)

    logger.info("\n#####################################")
    logger.info("# Completed execution of main()")
    logger.info("#####################################")


#####################################
# Conditional Execution
#####################################

if __name__ == '__main__':
    main()