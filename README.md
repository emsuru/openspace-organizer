# Open Space Organizer

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## Description

This Openspace Organizer takes an input file with a list of names from the user, randomly assigns each person on the user list to a table seat in an open space, and returns this random distribution of seats to the user in an output file.

This Organizer is built for the following concrete specifications:

- The input file is accepted in a CSV format
- The output file is provided in an  XLS format. 
- The default openspace is organized in 6 tables of 4 seats each.

If the input file provided by the user contains more more people than the available 24 seats in the default cofiguration, the program will run correctly but will return a warning and a list of people that remained without a seat.

The program can easily be changed to fit other numbers.

## Project Structure

The project is structured into several Python files and directories,to ensure modularity and ease of maintenance.

- `main.py`: This is the entry point of the application. It orchestrates the process of loading the names from the user list, shuffling them, assigning them seats at the openspace tables and storing the seating arrangement in a xls file.
  
- `utils/` this directory contains utility classes and functions that support the main application.
  -- `openspace.py` defines the `Openspace` class responsible for managing the open space.
  -- `table.py` contains the `Table` and `Seat` classes. `Table` manages a collection of `Seat` instances, each of which can be occupied by a person.
  -- `file_utils.py` provides functionality to load names from a CSV file.

## Setup

To set up the project, ensure you have Python installed on your system. Then, install the required packages by running:
```bash
pip install pandas openpyxl
```
These packages are necessary for handling CSV and Excel files, respectively.

## Usage

To run the program, clone this repo on your local machine, then navigate to its directory in your terminal and execute:
```bash
python3 main.py
```
This will load the list of names from a `./colleagues.csv` (replace this in the project directory with your list while keeping the filename), randomly assign them to seats, print the seating arrangement to the terminal and create an Excel file named `seating_arrangement.xlsx` with the seating arrangement inside the project directory.

Each subsequent run will reshuffle the names, display the new random seating to terminal and overwrite the excel with this new arrangement.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

- fork the repository
- create a new branch for your new feature or bug fix
- implement your changes
- submit a pull request with a clear description of your changes
- thank you for your contribution :D

## Ideas for further development / contributions:

- Adding a feature to enable defining the room setup from a config.json file
- Adding a feature to enable changing dynamically the setup and re-running the program.
- Adding a feature to deliver an extra format for the distribution of the seats, in a more visual, graphic way

## Personal background

This is my first solo project submitted as part of the BeCode AI Bootcamp, 2024 in Ghent, Belgium. 
The project's main goal was to practice Object Oriented Programming in Python, as wel as file handling and other programming essentials.

Connect with me on [LinkedIn](https://www.linkedin.com/in/mirunasuru/).

![OOP-meme-2](https://media.licdn.com/dms/image/D4D12AQHkg-fXKvjxEg/article-cover_image-shrink_423_752/0/1681026736811?e=1713398400&v=beta&t=0vtBUHAM2gSz1ZrLX8AhnjQs7q4YrENaldYbhfSnMAQ)



