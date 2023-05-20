import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Maria",
    user="postgres",
    password="postgres")

# check if connection is successful

if conn:
    print("connected")
else:
    print("not connected")

table_name = "games"

# get the cursor

cur = conn.cursor()

# get data and write to csv file with header
# open file to write

with open('games.csv', 'w') as f:
    cur.copy_expert("COPY games TO STDOUT WITH CSV HEADER DELIMITER ','", f)
