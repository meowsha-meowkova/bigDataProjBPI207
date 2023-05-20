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

# get the number of rows in the table

cur.execute("SELECT COUNT(*) FROM " + table_name + ";")

# fetch the result

res = cur.fetchone()

# print the result

print("Total number of rows in the table: ", res[0])