#!/usr/bin/env python
# coding: utf-8

# # write a solution to find all dates'id with higher temperatues compared to its previous dates(yeasterday).

# In[1]:


import sqlite3

# Establish connection to SQLite database (create if not exist)
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# Create Weather table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Weather (
        id INTEGER PRIMARY KEY,
        recordDate DATE,
        temperature INTEGER
    )
''')

# Sample data to insert into Weather table
data = [
    (1, '2015-01-01', 10),
    (2, '2015-01-02', 25),
    (3, '2015-01-03', 20),
    (4, '2015-01-04', 30)
]

# Insert data into Weather table
cursor.executemany('INSERT INTO Weather VALUES (?, ?, ?)', data)

# Commit changes and close connection
conn.commit()
conn.close()
SELECT w.id
FROM Weather w
WHERE EXISTS (
    SELECT 1
    FROM Weather w2
    WHERE w2.recordDate = DATE(w.recordDate, '-1 day')
      AND w.temperature > w2.temperature
);
import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('weather.db')
cursor = conn.cursor()

# SQL query to find IDs with higher temperatures compared to the previous day
query = '''
    SELECT w1.id
    FROM Weather w
    WHERE EXISTS (
        SELECT 1
        FROM Weather w2
        WHERE w2.recordDate = DATE(w.recordDate, '-1 day')
          AND w.temperature > w2.temperature
    )
'''

# Execute the query and fetch all results
cursor.execute(query)
results = cursor.fetchall()

# Print the results
print("IDs with higher temperatures compared to the previous day:")
for row in results:
    print(row[0])

# Close the connection
conn.close()


# In[ ]:




