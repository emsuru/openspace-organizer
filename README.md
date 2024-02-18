# Open Space Organizer

[![forthebadge made-with-python](https://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

## 📖 Description

This Openspace Organizer takes an input file with a list of names from the user, randomly assigns each person on the user list to a table seat in an open space, and returns this random distribution of seats to the user in an output file.

If the input file provided by the user contains more people than the available 24 seats in the default cofiguration, the program will run correctly and will return a warning and a list of people that remained without a seat.

The program can easily be changed to fit other user numbers.

## 🧬 Project Structure

```
.
├── main.py        
├── utils/
│ └── openspace.py
│ └── table.py 
│ └── file_utils.py
└── README.md
```

## 👩‍💻 Usage

1. To set up the project, ensure you have Python installed on your system. Then, install the required packages by running:

```bash
pip install pandas openpyxl
```
These packages are necessary for handling CSV and Excel files, respectively.

2. To use your own list, add or replace the existing `./colleagues.csv` (keep the filename) in the project directory.
   
3. To run the program, clone this repo on your local machine, then navigate to its directory in your terminal and execute:

```bash
python3 main.py
```

4. Running the program will:
   - load the list of names from a `./colleagues.csv`
   - shuffle the names & randomly assign them to seats
   - print the seating arrangement to the terminal
   - create an Excel file `seating_arrangement.xlsx` inside the project directory.

5. Each subsequent run will reshuffle the names, display the new random seating to terminal and overwrite the excel with this new arrangement.

## 📂 Project background

This is my first solo project submitted as part of the BeCode AI Bootcamp, 2024 in Ghent, Belgium. 
The project's main goal was to practice Object Oriented Programming in Python, as wel as file handling and other programming essentials.

![OOP-meme](https://i.giphy.com/sAFuZGCuBkaPGEtHRK.webp)

## ⚠️ Warning

All my code is currently *heavily*:

- docstringed
- commented

.. and sometimes typed.

This is to help me learn and for my feedback sessions with our coach.

---

Thank you for visiting my project page!

Connect with me on [LinkedIn](https://www.linkedin.com/in/mirunasuru/) 

🤍


