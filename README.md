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