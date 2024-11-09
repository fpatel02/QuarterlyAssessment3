# QuarterlyAssessment3

Overview

For your third quarterly assessment, we’ll be creating a GUI for our Quiz Bowl
Project. The graphical user interface is only necessary for the user (the one
taking the quiz). Populating the database does not have to be done in a GUI
format, nor does reading the data stored inside the database (though those
files are obviously needed for you to manage the program). In other words,
you’re the programmer. You set up the database in the back-end. The user is
given a GUI to interact with. You should be able to give this GUI to a user that
does not have any coding knowledge.

Instructions

On the back end, you should have a database with 5 different tables – one
for each course. Each course (i.e., table) should have at least 10 questions.
Your GitHub folder should include a way for you to add/remove/read current
questions from the database in the back end.
There should be two windows the user interacts with. The first (sample
below) should allow the user to select a category of questions. You can use
any widget you’d like for the user to select the category of questions (e.g.,
combo box, entry box, radio button, etc.) When the user selects a category
and presses “start quiz now,” this first window should close and the second
window should open.

Options for selecting a category (first window)

On the second window (i.e., after the user presses Start Quiz button in the
window above), the user should be given at least 10 multiple choice
questions on the topic they selected. Use your imagination on how the
questions, answers, and solutions are displayed. The user should be able to
a) select an answer (text box, multiple-choice answer, etc.), b) submit their
answer(s), and c) receive feedback on their answer.
When you’re creating these questions/answers, save the format you use in
for you question displaying in a class. The class can then be called for every
question inside your database. This is a requirement not a suggestion. It
may take more time to set up, but scaling up after that requires minimal
effort.


QuestionsAnswers.py:
    Create the Database: The script connects to a SQLite database called questions_answers.db. If the file does not exist, SQLite will automatically create it.

    Create a Table: The CREATE TABLE IF NOT EXISTS statement ensures that the questions table is created if it doesn't already exist. The table has columns for:

        id (Primary key)
        question (The question text)
        option_a, option_b, option_c, option_d (The answer choices)
        correct_answer (The correct answer's identifier, e.g., "a", "b", "c", "d")
    Insert Data: The script inserts each question and its corresponding answer choices into the table using the INSERT INTO statement.

    Verify Data: After inserting the data, it retrieves and prints all records from the questions table.



databasereadfile.py:
    Connecting to the Database:

        The function read_from_db() accepts the db_file as an argument, which is the path to the SQLite database file.
        It establishes a connection to the database and creates a cursor to execute SQL queries.
    Retrieving Table Names:

        The SQL query SELECT name FROM sqlite_master WHERE type='table'; is used to retrieve all the table names in the database.
        The result is stored in tables, and each table name is printed with a numbered list.
    User Table Selection:

        The user is prompted to input the table number they want to read data from.
        The function checks if the input is valid and if the table choice is within the valid range of available tables.
    Fetching and Printing Data:

        Once the user selects a table, the function executes SELECT * FROM <table_name> to fetch all rows from the chosen table.
        If the table contains data, it prints the column names as a header followed by the data in each row. If no data is found, it prints a message indicating the table is empty.
    Closing the Connection:

    Finally, the function closes the database connection after printing the data.


main.py:

    Database Connection: The sqlite3 connection fetches questions based on the selected category.
    First Window (Category Selection): Allows users to choose a quiz category.
    Second Window (Quiz): Displays questions and multiple-choice answers, with a submit button to check answers.
    Answer Validation: Compares the user’s choice with the correct answer, providing feedback with a message box.