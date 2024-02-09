# Open Space Organizer

## Description
This Openspace Organizer takes a list of names from the user, randomly assigns each person on the user list to a table seat in an open space, and returns this random distribution of seats to the user in a different file.

This Organizer is built for the following concrete specifications:

- the user input is accepted in a csv file that contains 24 names;
- the open space is organized in 6 tables of 4 seats each;
- the random table seat distribution output is given to the user in the form of an xcel file .


## Project Structure
The project is structured into several Python files and directories, each serving a specific purpose to ensure modularity and ease of maintenance. Here's a breakdown:

- `main.py`: This is the entry point of the application. It orchestrates the process of loading colleague names, shuffling them for randomness, and then utilizing the `Openspace` class to assign seats. Finally, it displays and stores the seating arrangement.
- `utils/`: This directory contains utility classes and functions that support the main application.
  - `openspace.py`: Defines the `Openspace` class responsible for managing the open space, including organizing and displaying the seating arrangement, and storing it to an Excel file.
  - `table.py`: Contains the `Table` and `Seat` classes. `Table` manages a collection of `Seat` instances, each of which can be occupied by a colleague.
  - `file_utils.py`: Provides functionality to load colleague names from a CSV file.

## Setup
To set up the project, ensure you have Python installed on your system. Then, install the required packages by running:
```bash
pip install pandas openpyxl
```
These packages are necessary for handling CSV and Excel files, respectively.

## Usage
To run the program, navigate to the project directory in your terminal and execute:
```bash
python3 main.py
```
This will load the colleagues from `./colleagues.csv`, randomly assign them to seats, and output the final seating arrangement. Additionally, it will create an Excel file named `seating_arrangement.xlsx` with the seating details.

## Contributing
Contributions are welcome!
Some of the ways in which you can contribute to this OpenSpace Organizer include:
- Adding a feature to be able to define the room setup from a config.json file
- Adding a feature to be able to change dynamically the setup and re-run the program.
- Adding a feature to deliver an extra format for the distribution of the seats, in a more visual, graphic way


Please follow these steps to contribute:
- fork the repository
- create a new branch for your feature or bug fix
- implement your changes
- submit a pull request with a clear description of your changes
- thank you for your contribution :D
