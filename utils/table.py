# utils/table.py

class Seat:
    """
    Represents a seat within a table. Each seat can either be free or occupied by an occupant.
    """
    def __init__(self) -> None:
        """
        Initializes a Seat instance, setting it to free and without an occupant.
        """
        self.free = True  # A boolean attribute that indicates if the seat is free (True) or occupied (False)
        self.occupant = ""  # A string attribute that holds the name of the occupant. It's an empty string if the seat is free.

    def set_occupant(self, name: str) -> None:
        """
        Assigns an occupant to the seat if it is free.

        :param name: The name of the occupant to be assigned to the seat.
        """
        if self.free:  # Checks if the seat is currently free
            self.occupant = name  # If the seat is free, assigns the occupant's name to the seat
            self.free = False  # After assigning the seat, marks the seat as occupied

    def remove_occupant(self) -> str:
        """
        Removes the occupant from the seat, making it free again.

        :return: The name of the occupant that was removed.
        """
        occupant_name = self.occupant  # Stores the name of the current occupant before removing them
        self.occupant = ""  # Clears the occupant's name, making the seat free again
        self.free = True  # Marks the seat as free after removing the occupant
        return occupant_name  # Returns the name of the occupant that was removed

    def __str__(self):
        """
        Returns a string representation of the Seat instance.

        :return: A string indicating whether the seat is free or the name of the occupant.
        """
        return "Free" if self.free else f"Occupied by {self.occupant}"

class Table:
    """
    Represents a table which contains a collection of seats.
    """
    def __init__(self, capacity: int = 4):
        """
        Initializes a Table instance with a specified capacity.

        :param capacity: The number of seats the table can hold. Defaults to 4.
        """
        self.capacity = capacity  # The maximum number of seats at the table
        self.seats = [Seat() for _ in range(capacity)]  # Initializes the seats as a list of Seat instances

    def has_free_spot(self) -> bool:
        """
        Checks if there is at least one free spot at the table.

        :return: True if there is a free spot, False otherwise.
        """
        return any(seat.free for seat in self.seats)  # Returns True if any seat is free, False otherwise

    def assign_seat(self, name: str):
        """
        Assigns a seat to the first free spot available at the table for a given occupant.

        :param name: The name of the occupant to be seated.
        """
        for seat in self.seats:  # Iterates through each seat at the table
            if seat.free:  # Checks if the current seat is free
                seat.set_occupant(name)  # If the seat is free, assigns the occupant to the seat
                break  # Exits the loop after assigning the seat

    def left_capacity(self) -> int:
        """
        Calculates the number of free seats left at the table.

        :return: The number of free seats available.
        """
        return sum(seat.free for seat in self.seats)  # Sums up the number of free seats and returns it

    def __str__(self):
        """
        Returns a string representation of the Table instance.

        :return: A string indicating the table's capacity and the number of free seats.
        """
        return f"Table with capacity: {self.capacity}, Free seats: {self.left_capacity()}"
