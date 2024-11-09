import sqlite3

def read_from_db(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    # Retrieve all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print out all the table names
    if tables:
        print("Tables in the database:")
        for idx, table in enumerate(tables, start=1):
            print(f"{idx}. {table[0]}")
    else:
        print("No tables found in the database.")
        return
    
    # Ask the user to choose a table
    try:
        table_choice = int(input(f"Choose a table (1-{len(tables)}): "))
        if table_choice < 1 or table_choice > len(tables):
            print("Invalid choice. Exiting.")
            return
        table_name = tables[table_choice - 1][0]
    except ValueError:
        print("Invalid input. Exiting.")
        return
    
    # Fetch and print the data from the selected table
    print(f"\nData from table: {table_name}")
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    # If there are rows, print them
    if rows:
        # Get the column names
        column_names = [description[0] for description in cursor.description]
        print(f"{' | '.join(column_names)}")  # Print column names header
        
        for row in rows:
            print(' | '.join(map(str, row)))  # Print each row
    else:
        print(f"No data found in table {table_name}.")

    # Close the database connection
    conn.close()

# Call the function to test
db_file = 'questions_answers.db'  # Replace with your database file path
read_from_db(db_file)
