# main.py
# Import the random module to enable random shuffling of the colleagues list
import random
# Import pandas as it's a dependency for Openspace.store method;
# The Openspace.store method is used to store the seating arrangement in an Excel file
import pandas as pd
# Import Openspace class from the utils package
# The Openspace class contains the logic for seat allocation in the open space
from utils.openspace import Openspace
# Import load_colleagues function from the utils package
# The load_colleagues function is used to load names from a CSV file
from utils.file_utils import load_colleagues

# Define the main function which orchestrates the seat allocation process
def main():
    # Display a welcome message to indicate the start of the seat allocation process
    print("\nWelcome to our Open Space!\nHere is the seat and table distribution for the day: \n")

    # Load colleagues' names from a CSV file using the load_colleagues function
    # The path to the CSV file is specified as "./colleagues.csv"
    colleagues = load_colleagues("./colleagues.csv")
    # Shuffle the list of colleagues to ensure that the seat allocation is random each time the script runs
    random.shuffle(colleagues)

    # Create an instance of the Openspace class to manage the seating arrangement
    # This object will be used to organize, display, and store the seating arrangement
    openspace = Openspace()

    # Use the organize method of the Openspace instance to allocate seats to colleagues
    # The list of shuffled colleague names is passed as an argument to the organize method
    openspace.organize(colleagues)

    # After organizing the colleagues into seats, display the final seating arrangement
    # This is done through the display method of the Openspace instance
    openspace.display()

    # Store the seating arrangement in an Excel file for the user
    # The filename is specified as "seating_arrangement.xlsx"
    # The store method of the Openspace instance is used for this purpose
    openspace.store("seating_arrangement.xlsx")


# This conditional statement checks if the script is being run directly (not imported)
# If true, it calls the main function to start the seat allocation process
if __name__ == "__main__":
    main()
