# Insert data to database

# Libraries
import sqlite3

# Create database
sqlite_file = "database.db"

# Connection
conn = sqlite3.connect(sqlite_file)

# Cursor for commands and accessing information
cur = conn.cursor()

# Insert data 
sql = "INSERT INTO sensors (name, description, compound) VALUES ('Pressure', 'Pressure sensor',0)"
cur.execute(sql)
sql = "INSERT INTO sensors (name, description, compound) VALUES ('Humidity', 'Humidity sensor',0)"
cur.execute(sql)
sql = "INSERT INTO sensors (name, description, compound) VALUES ('Temperature', 'Temperature sensor',1)"
cur.execute(sql)

# Commit the changes
conn.commit()

# Close connection
conn.close()
