# Create a database and add different tables

# Libraries
import sqlite3

# Create database
sqlite_file = "database.db"

# Connection
conn = sqlite3.connect(sqlite_file)

# Cursor for commands and accessing information
cur = conn.cursor()

# Commands
# Command to create a SENSOR table
sql = "CREATE TABLE sensors (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, description TEXT, compound INTEGER)"
cur.execute(sql)

# Command to create a VARIABLES table
sql = "CREATE TABLE variables (id INTEGER PRIMARY KEY AUTOINCREMENT, sensor_id INTEGER, name TEXT NOT NULL, description TEXT, units TEXT)"
cur.execute(sql)

# Command to create a MEASURES table
sql = "CREATE TABLE measures (id INTEGER PRIMARY KEY AUTOINCREMENT, variable_id INTEGER, measure TEXT, date TEXT)"
cur.execute(sql)

# Commit the changes
conn.commit()


# MAIN COMMANDS


# Close connection
conn.close()



