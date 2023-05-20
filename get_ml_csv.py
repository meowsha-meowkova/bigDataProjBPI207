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

# id SERIAL PRIMARY KEY,
# type VARCHAR(255),
# name VARCHAR(255),
# required_age INTEGER,
# is_free BOOLEAN,
# platform_windows BOOLEAN,
# platform_mac BOOLEAN,
# platform_linux BOOLEAN,
# metacritic_score INTEGER,
# categories_array VARCHAR(255)[],
# genres_array VARCHAR(255)[],
# recommendations INTEGER,
# release_date DATE,
# first_group_price_cents INTEGER


# select everything from the table except the id, name, and release_date columns
# but add days_since_release column

cur.execute("""SELECT
    type,
    required_age,
    is_free,
    platform_windows,
    platform_mac,
    platform_linux,
    CASE WHEN metacritic_score IS NULL THEN 0 ELSE metacritic_score END,
    categories_array,
    genres_array,
    CASE WHEN recommendations IS NULL THEN 0 ELSE recommendations END,
    first_group_price_cents,
    (CURRENT_DATE - release_date) AS days_since_release
    FROM games
    """)
rows = cur.fetchall()

# write the rows to csv file

import csv
import json

with open('ml_games.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow([
        'type',
        'required_age',
        'is_free',
        'platform_windows',
        'platform_mac',
        'platform_linux',
        'metacritic_score',
        'categories_array',
        'genres_array',
        'recommendations',
        'first_group_price_cents',
        'days_since_release'
    ])

    for row in rows:
        writer.writerow(row)

# close the cursor and connection

cur.close()

# pip freeze > requirements.txt