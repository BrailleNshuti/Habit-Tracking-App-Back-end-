# Habit Tracking Application

A Python Habit Tracking Application, Modular Created for the course DLBDSOOFPP01, Object-Oriented and Functional Programming with Python at IU International University of Applied Sciences. 
This Application (back-end) provides functionalities for users to define habits, record completions, measure progress, calculate streaks, and save habit data between two sessions via JSON storage. The project exhibits object-oriented programming, functional programming concepts, modular software design, automated testing, and analytics implementation.


**Author**

**Name**: Rusingiza Nshuti Braille

**Matriculation Number**: 4243333

**University**: IU International University of Applied Sciences

**Course**: DLBDSOOFPP01 – Object-Oriented and Functional Programming with Python

## Project Description

The Habit Tracking Application is a backend-focused command-line application designed to help users build and monitor habits over time. Users can create habits with different periodicities, mark habits as completed, analyse streaks, and persist their progress between sessions.
The project was developed using Python while applying software engineering principles such as:
-	Object-Oriented Programming (OOP)
-	Functional Programming
-	Modular Software Architecture
-	Persistent Data Storage
-	Automated Unit Testing
-	Analytics and Streak Calculation

The application supports both daily and weekly habits and correctly calculates streaks according to each habit’s periodicity.

## Features

### Habit Management
-	Create new habits
-	Delete habits
-	Mark habits as completed
-	View all tracked habits

### Analytics Features
-	View all currently tracked habits
-	Filter habits by periodicity
-	Calculate the longest streak overall
-	Calculate the longest streak for a specific habit

### Data Persistence
-	Habit data is stored in JSON format
-	Data persists between application sessions 

### Testing
-	Automated unit tests using pytest
-	Tests for habit management and analytics
-	Tests for daily and weekly streak calculations

## Technologies Used

Python 3:	Main programming language
pytest:	Automated unit testing
JSON:	Persistent data storage
Git & GitHub:	Version control and project hosting

## Object-Oriented Programming Concepts Used:
The project applies several important object-oriented programming concepts:

### Encapsulation
Related data and functionality are grouped together inside classes.
Example:
class Habit:
    def __init__(self, name, periodicity):
        self.name = name
        self.periodicity = periodicity

### Composition
The HabitTracker class uses storage and analytics modules together.
### Modular Design
The application is divided into logically separated modules to improve readability and maintainability.

## Project Structure

```text
Habit-Tracking-App-Back-end/
├── data/
│   └── habits.json
├── habit_tracker/
│   ├── __init__.py
│   ├── analytics.py
│   ├── cli.py
│   ├── exceptions.py
│   ├── fixtures.py
│   ├── habit.py
│   ├── storage.py
│   └── tracker.py
├── tests/
│   ├── test_analytics.py
│   ├── test_habit.py
│   └── test_tracker.py
├── screenshots/
│   ├── cli_menu.png
│   ├── analytics_results.png
│   ├── unit_tests.png
│   └── streak_examples.png
├── .gitignore
├── main.py
├── README.md
├── requirements.txt
└── pytest.ini

## Analytics Module
The analytics module was implemented using functional programming concepts and contains functions for:

**list_habits()**:	Returns all tracked habits
**filter_by_periodicity()**:	Filters habits by periodicity (daily/weekly)
**longest_streak_all()**:	Returns the longest streak overall
**longest_streak_per_habit()**:	Returns the longest streak for one habit

The analytics functions are separated from the user interface and storage logic to improve modularity.

## Streak Calculation Logic
One of the most important parts of the project is streak calculation.
### Daily Habits
Daily streaks are calculated using consecutive calendar days.
### Weekly Habits
Weekly streaks are calculated using consecutive ISO calendar weeks.

This ensures that weekly habits are not incorrectly evaluated as daily habits.

## Predefined Habit Data
The project includes predefined fixture data containing more than four weeks of habit completion history.
### The predefined data is used for:
-	Testing streak calculations
-	Testing analytics functions
-	Demonstrating application functionality
-	Automated unit testing

### The fixture data includes:
-	Daily habits
-	Weekly habits
-	Continuous streak examples
-	Broken streak examples

## Installation
1. Clone the Repository
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME

2. Create a Virtual Environment
Windows
python -m venv .venv
.venv\Scripts\activate
Mac/Linux
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

## How to Run the Application
Run the application using:
python main.py

The command-line interface will open and allow users to:
-	Create habits
-	Complete habits
-	Delete habits
-	View analytics
-	Track streaks

How to Run Unit Tests
Run all tests using:
pytest
Example successful result:
9 Tests passed

Screenshots

## Screenshots

**Main CLI Menu**  
<image-card alt="Main CLI Menu" src="screenshots/cli_menu.png" ></image-card>

**Analytics Results**  
<image-card alt="Analytics Results" src="screenshots/analytics_results.png" ></image-card>

**Unit Tests Passing**  
<image-card alt="Unit Tests Passing" src="screenshots/unit_tests.png" ></image-card>

9 Tests passed

**Streak Calculation Example**  
<image-card alt="Streak Calculation Example" src="screenshots/streak_examples.png" ></image-card>



## Code Quality and Documentation
The project follows Python naming conventions and software engineering best practices.
Naming Conventions
-	Classes use PascalCase
-	Variables and functions use snake_case
-	File names are lowercase

## Documentation
The source code includes:
-	Docstrings
-	Inline comments
-	Modular file organisation

## .gitignore
The repository includes a .gitignore file to avoid uploading unnecessary local files.
Example:
__pycache__/
.pytest_cache/
.venv/
*.pyc
.DS_Store
This keeps the GitHub repository clean and professional.

## Unit Testing Coverage
The project contains automated tests covering:
Test Area     covered
Habit creation	Yes
Habit deletion	Yes
Daily streak calculations	yes
Weekly streak calculations	Yes
Analytics filtering	Yes
Longest streak calculations	Yes
Persistence and storage	Yes

## Challenges and Improvements
One of the hardest things during development was figuring out how to correctly calculate streaks not only for daily habits but also for weekly habits.
Based on the Phase 2 tutor feedback, a major upgrade was done by breaking the project into modular files and introducing better automated testing.

The final Phase 3 version significantly improved:
-	Project modularity
-	Testing quality
-	Documentation
-	GitHub organisation
-	Analytics reliability
-	Repository cleanliness

## Future Improvements
Possible future improvements include:
-	Graphical user interface (GUI)
-	SQLite database support
-	Habit reminder notifications
-	User authentication
-	Statistics visualisation
-	Exporting analytics reports

## Conclusion
The Habit Tracking Application perfectly meets the portfolio requirements for the Object-Oriented and Functional Programming with Python course.
The final application demonstrates:
-	Object-oriented programming
-	Functional analytics
-	Modular software design
-	Persistent storage
-	Automated testing
-	Command-line interaction
-	Professional GitHub project organisation

The project changed quite a bit since previous phases and at this point is a clean, maintainable, and well-tested backend Python application.

## GitHub Repository

https://github.com/BrailleNshuti/Habit-Tracking-App-Back-end-
