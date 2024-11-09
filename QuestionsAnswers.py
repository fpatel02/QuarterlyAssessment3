import sqlite3

# Connect to (or create) the SQLite database
conn = sqlite3.connect('questions_answers.db')
cursor = conn.cursor()

# Create separate tables for each class (if they don't already exist)

# Create table for Intro to Programming questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS programming_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# Create table for Business Database Management questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS business_db_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

#Create table for Business Analytics questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS business_analytics_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

#Create table for Business Law questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS business_law_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

#Create table for Business Management questions
cursor.execute('''
CREATE TABLE IF NOT EXISTS business_law_questions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question TEXT NOT NULL,
    option_a TEXT NOT NULL,
    option_b TEXT NOT NULL,
    option_c TEXT NOT NULL,
    option_d TEXT NOT NULL,
    correct_answer TEXT NOT NULL
)
''')

# List of questions for Intro to Programming
programming_questions = [
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
     "[1, 2, 3]", "[1, 2, 3, 4]", "[1, 2, 4, 3]", "Error", "B")
]

# List of questions for Business Database Management
business_db_questions = [
    ("What is a database?", 
     "A collection of files", "A collection of structured data", "A data processing system", "A software program", "B"),
    
    ("Which of the following is a type of database model?", 
     "Relational model", "Network model", "Hierarchical model", "All of the above", "D"),
    
    ("What does SQL stand for?", 
     "Structured Query Language", "Structured Quick Language", "Sequential Query Language", "Standard Query Language", "A"),
    
    ("Which SQL command is used to retrieve data from a database?", 
     "INSERT", "SELECT", "UPDATE", "DELETE", "B"),
    
    ("What is the purpose of a primary key in a relational database?", 
     "To ensure data integrity", "To store the largest data", "To create a backup of the table", "To link tables", "A")

    ("Which of the following is true about a 'foreign key' in a database?", 
     "It is a key that uniquely identifies a row in a table", "It creates a relationship between two tables", "It is always the same as the primary key", "It is used to delete records", "B"),
    
    ("What is a 'table' in a relational database?", 
     "A collection of related data organized in rows and columns", "A system for managing users", "A type of software", "A special type of primary key", "A"),
    
    ("Which of the following is used to uniquely identify a record in a database table?", 
     "Foreign key", "Primary key", "Index", "Column", "B"),
    
    ("Which SQL statement is used to add new records into a table?", 
     "INSERT INTO", "UPDATE", "DELETE", "CREATE TABLE", "A"),
    
    ("What is 'normalization' in database design?", 
     "The process of deleting data", "The process of organizing data to reduce redundancy", "The process of creating tables", "The process of writing SQL queries", "B")
]
#List of questions for Business Analytics
business_analytics_questions = [
    ("What is the primary purpose of business analytics?", 
     "To predict future trends", "To analyze past performance", "To create financial reports", "To evaluate employee performance", "B"),
    
    ("Which of the following is a measure of central tendency?", 
     "Variance", "Standard deviation", "Mean", "Range", "C"),
    
    ("What does the standard deviation measure in a dataset?", 
     "The middle value", "The spread or dispersion of the data", "The highest value", "The correlation between variables", "B"),
    
    ("Which of the following is an example of nominal data?", 
     "Age", "Income", "Gender", "Height", "C"),
    
    ("Which statistical measure is used to describe the relationship between two variables?", 
     "Variance", "Mean", "Correlation coefficient", "Median", "C"),
    
    ("Which of the following is true about a normal distribution?", 
     "It is skewed to the left", "It has two peaks", "The mean, median, and mode are all equal", "It has no variance", "C"),
    
    ("In hypothesis testing, what does the p-value represent?", 
     "The probability that the null hypothesis is true", "The probability of observing the data if the null hypothesis is true", "The probability of the alternative hypothesis being true", "The measure of variability in the data", "B"),
    
    ("Which of the following is a measure of data spread?", 
     "Mean", "Median", "Mode", "Range", "D"),
    
    ("What type of statistical test would you use to compare the means of two independent groups?", 
     "T-test", "ANOVA", "Chi-square test", "Correlation test", "A"),
    
    ("What is the purpose of regression analysis in business analytics?", 
     "To summarize the data", "To identify trends in categorical data", "To predict the value of a dependent variable based on independent variables", "To calculate the correlation between two variables", "C")
]

#List of questions for Business Law
business_law_questions = [
    ("What is the primary purpose of business law?", 
     "To protect employees from workplace discrimination", "To govern the relationships between businesses and consumers", "To ensure compliance with environmental regulations", "To regulate international trade", "B"),
    
    ("Which of the following is required for a contract to be legally binding?", 
     "Written agreement", "Offer and acceptance", "Signature of a notary", "Payment in full", "B"),
    
    ("Which of the following best defines 'tort' in business law?", 
     "A breach of contract", "A criminal offense", "A wrongful act leading to civil legal liability", "An agreement between parties", "C"),
    
    ("What does 'intellectual property' refer to in business law?", 
     "Property used in a business", "Ideas, inventions, and creations that can be protected by law", "The property rights of employees", "Real estate used by a company", "B"),
    
    ("What is the legal term for a contract that is not legally enforceable due to illegality?", 
     "Void contract", "Breach of contract", "Voidable contract", "Executed contract", "A"),
    
    ("Which of the following is a requirement for a valid offer in contract law?", 
     "It must be made in writing", "It must be communicated to the offeree", "It must be made with a promise of payment", "It must be accepted immediately", "B"),
    
    ("What is the legal doctrine of 'respondeat superior'?", 
     "The principle that an employee is liable for their own actions", "The employer is not responsible for employee actions", "The employer is liable for the actions of an employee performed within the scope of employment", "The employee can be held liable for any breach of contract", "C"),
    
    ("Which of the following is a defense to a breach of contract claim?", 
     "Lack of consideration", "Mutual mistake", "Impossibility of performance", "All of the above", "D"),
    
    ("Which of the following is NOT a type of business entity?", 
     "Sole proprietorship", "Limited liability company (LLC)", "Partnership", "Sole contract", "D"),
    
    ("What does 'fair use' mean in intellectual property law?", 
     "It allows for the unrestricted use of copyrighted works", "It allows for limited use of copyrighted works without permission under certain conditions", "It allows only non-commercial use of intellectual property", "It allows companies to use copyrighted materials freely", "B")
]

#List of questions for Business Management
business_management_questions = [
    ("What is the primary role of a manager in an organization?", 
     "To manage human resources", "To oversee operations and ensure goals are met", "To create the company’s marketing plan", "To design the product and its features", "B"),
    
    ("Which of the following is an example of a leadership style?", 
     "SWOT analysis", "Team-building exercise", "Autocratic", "Employee training program", "C"),
    
    ("What is the purpose of a mission statement in a business?", 
     "To outline the company's long-term financial goals", "To provide a roadmap for employees on tasks and responsibilities", "To define the company’s purpose and core values", "To create a marketing strategy", "C"),
    
    ("Which of the following is NOT one of the four functions of management?", 
     "Planning", "Organizing", "Monitoring", "Controlling", "C"),
    
    ("What does SWOT analysis stand for?", 
     "Systematic Way Of Testing", "Strategic Way Of Thinking", "Strengths, Weaknesses, Opportunities, Threats", "Standard Work Operating Template", "C"),
    
    ("Which of the following is a characteristic of a successful team?", 
     "A clear division of roles and responsibilities", "Conflict avoidance", "A single leader who makes all decisions", "All of the above", "A"),
    
    ("Which management theory emphasizes the importance of organizational structure and employee needs?", 
     "Scientific management theory", "Human relations theory", "Contingency theory", "Systems theory", "B"),
    
    ("Which of the following is an example of a strategic goal for a business?", 
     "Increase customer satisfaction by 10% in the next quarter", "Reduce employee turnover by 2%", "Expand into three new international markets within 5 years", "Improve internal communication by scheduling weekly meetings", "C"),
    
    ("What is the purpose of a performance appraisal in business management?", 
     "To evaluate the company’s financial health", "To assess employee performance and provide feedback", "To develop marketing strategies", "To assess customer satisfaction", "B"),
    
    ("Which of the following is an example of a functional area of management?", 
     "Marketing", "Human resources", "Operations", "All of the above", "D")
]



# Insert questions for Programming class into the 'programming_questions' table
for question in programming_questions:
    cursor.execute('''
    INSERT INTO programming_questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Insert questions for Business Database class into the 'business_db_questions' table
for question in business_db_questions:
    cursor.execute('''
    INSERT INTO business_db_questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Insert questions for Business Analytics class into the 'business_analytics_questions' table
for question in business_analytics_questions:
    cursor.execute('''
    INSERT INTO business_analytics_questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Insert questions for Business Law class into the 'business_law_questions' table
for question in business_law_questions:
    cursor.execute('''
    INSERT INTO business_law_questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Insert questions for Business Management class into the 'business_management_questions' table
for question in business_management_questions:
    cursor.execute('''
    INSERT INTO business_management_questions (question, option_a, option_b, option_c, option_d, correct_answer)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', question)

# Commit the transactions
conn.commit()

# Verify if the data was inserted by fetching and printing all questions for each class

# Retrieve and print all questions from 'programming_questions'
print("Programming Questions:")
cursor.execute('SELECT * FROM programming_questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Retrieve and print all questions from 'business_db_questions'
print("\nBusiness Database Management Questions:")
cursor.execute('SELECT * FROM business_db_questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Retrieve and print all questions from 'business_analytics_questions'
print("\nBusiness Analytics Questions:")
cursor.execute('SELECT * FROM business_analytics_questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Retrieve and print all questions from 'business_law_questions'
print("\nBusiness Law Questions:")
cursor.execute('SELECT * FROM business_law_questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Retrieve and print all questions from 'business_management_questions'
print("\nBusiness Management Questions:")
cursor.execute('SELECT * FROM business_management_questions')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the database connection
conn.close()
