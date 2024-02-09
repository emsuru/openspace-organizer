# utils/openspace.py
# Importing the random module to enable shuffling of tables
import random
# Importing the Table class from the table module within the same package
from .table import Table
# Importing pandas for data manipulation, specifically for storing the output in Excel format
import pandas as pd

# Defining the Openspace class
class Openspace:
    """
    The Openspace class represents an open space with a number of tables.
    It provides methods to organize people into tables, display the current seating arrangement,
    and store the seating arrangement into an Excel file.
    """
    # Initializes the Openspace class with a default number of tables set to 6
    def __init__(self, number_of_tables: int = 6):
        """
        Initializes an Openspace instance with a specified number of tables.
        Each table is represented as an instance of the Table class.
        Also initializes an empty list to store the names of unseated people.

        :param number_of_tables: The number of tables in the open space. Defaults to 6.
        """
        # Creates a list of Table instances equal to the number of tables specified
        self.tables = [Table() for _ in range(number_of_tables)]
        # Stores the number of tables in the open space
        self.number_of_tables = number_of_tables
        # Initializes an empty list to store the names of unseated people
        self.unseated_names = []

    # Method to organize people into tables based on the list of names provided
    def organize(self, names: list):
        """
        Organizes people into tables based on the list of names provided.
        If the number of names exceeds the total number of seats available, a warning message is printed.
        The method also tracks unseated people.

        :param names: A list of names to be seated.
        """
        # Calculates the total number of seats available in the open space
        total_seats = sum([table.capacity for table in self.tables])
        # Checks if the number of names exceeds the total number of seats available
        if len(names) > total_seats:
            # Prints a warning message if there are more people than seats
            print(f"Warning: There are more people ({len(names)}) than seats available ({total_seats}).")

        # Creates a copy of the names list to track unseated people
        self.unseated_names = names.copy()
        # Iterates over each name in the list of names
        for name in names:
            # Shuffle the tables list to ensure randomness in seat assignment
            random.shuffle(self.tables)
            assigned = False
            # Iterates over each table in the list of tables
            for table in self.tables:
                # Checks if the table has a free spot
                if table.has_free_spot():
                    # Assigns the seat to the person
                    table.assign_seat(name)
                    # Removes the name from the list of unseated people
                    self.unseated_names.remove(name)
                    assigned = True
                    break
        # Checks if there are any unseated names left in the list
        if self.unseated_names:
            # Prints a message listing the names of people who couldn't be seated
            print("The following people could not be seated due to lack of seats:")
            for name in self.unseated_names:
                print(f"- {name}")

    # Method to display the current seating arrangement in the open space
    def display(self):
        """
        Displays the current seating arrangement in the open space.
        For each table, it prints the table number and the status of each seat.
        """
        # Iterates over each table and its index in the list of tables
        for table_index, table in enumerate(self.tables, start=1):
            # Prints the table number
            print(f"Table {table_index}:")
            # Iterates over each seat and its index in the list of seats for the current table
            for seat_index, seat in enumerate(table.seats, start=1):
                # Checks if the seat is free
                if seat.free:
                    # Prints that the seat is free
                    print(f"\tSeat {seat_index}: Free")
                else:
                    # Prints the occupant of the seat if it is not free
                    print(f"\tSeat {seat_index}: Occupied by {seat.occupant}")

    # Method to store the current seating arrangement into an Excel file
    def store(self, filename: str):
        """
        Stores the current seating arrangement into an Excel file.
        The file contains the table number, seat number, and occupant name for each seat.
        If there are unseated people, a warning message is also included in the file.

        :param filename: The name of the Excel file to store the seating arrangement.
        """
        data = []
        # Iterates over each table and its index in the list of tables
        for table_index, table in enumerate(self.tables, start=1):
            # Iterates over each seat and its index in the list of seats for the current table
            for seat_index, seat in enumerate(table.seats, start=1):
                # Appends the table number, seat number and occupant name to the data list
                data.append({
                    'Table': table_index,
                    'Seat': seat_index,
                    'Occupant': seat.occupant if not seat.free else 'Free'
                })
        # Checks if there are any unseated names left in the list
        if self.unseated_names:
            # Appends a warning message to the data list
            data.append({
                'Table': 'Warning:',
                'Seat': 'There are more people than seats available.',
                'Occupant': 'The following people could not be seated due to lack of seats: ' + ', '.join(self.unseated_names)
            })
        # Converts the data list into a pandas DataFrame
        df = pd.DataFrame(data)
        # Stores the DataFrame into an Excel file
        df.to_excel(filename, index=False)

    def __str__(self):
        """
        Returns a string representation of the Openspace instance.
        """
        return f"Openspace with {self.number_of_tables} tables."
