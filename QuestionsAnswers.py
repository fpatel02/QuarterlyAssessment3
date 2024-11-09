import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect('questions_answers.db')
cursor = conn.cursor()

# Create the table to store questions and answers (if it doesn't already exist)
cursor.execute('''
CREATE TABLE IF NOT EXISTS questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# List of questions, options, and correct answers
questions = [
    ("What is the correct syntax to output 'Hello, World' in Python?", 
     "echo('Hello, World')", "print('Hello, World')", "console.log('Hello, World')", "printf('Hello, World')", "B"),
    
    ("Which of the following is a correct variable name in Python?", 
     "1variable", "variable_name", "variable-name", "var name", "B"),
    
    ("Which of the following is the correct data type for a decimal number in Python?", 
     "int", "float", "str", "bool", "B"),
    
    ("What does the 'len()' function do in Python?", 
     "Returns the length of a list only", "Returns the total memory used by an object", "Returns the number of characters in a string", "Returns the number of items in an object (list, string, etc.)", "D"),
    
    ("What is the result of the expression: 10 % 3?", 
     "3", "1", "0", "2", "B"),
    
    ("Which of the following is NOT a valid Python data type?", 
     "List", "Dictionary", "Tuple", "Character", "D"),
    
    ("Which of the following methods is used to add an item to a list in Python?", 
     "add()", "append()", "insert()", "extend()", "B"),
    
    ("How do you create a comment in Python?", 
     "// This is a comment", "# This is a comment", "/* This is a comment */", "/* This is a comment", "B"),
    
    ("Which operator is used for exponentiation in Python?", 
     "+", "-", "**", "//", "C"),
    
    ("What will the following code output?\n\nx = [1, 2, 3]\nx.append(4)\nprint(x)", 
     "[1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 4, 3]", "Error", "B"),
    
]

# Insert questions and answers into the table
for question in questions:
    cursor.execute('''
    INSERT INTO questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Commit the transaction and close the connection
conn.commit()

# Verify if the data was inserted by fetching and printing all questions
cursor.execute('SELECT * FROM questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
