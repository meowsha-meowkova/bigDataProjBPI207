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
# release_date DATE


# create a csv with columns: id, platform, is_free

# get windows games

cur.execute("SELECT id, 'windows', is_free FROM games WHERE platform_windows = True")

windows_games = cur.fetchall()

# get mac games

cur.execute("SELECT id, 'mac', is_free FROM games WHERE platform_mac = True")

mac_games = cur.fetchall()

# get linux games

cur.execute("SELECT id, 'linux', is_free FROM games WHERE platform_linux = True")

linux_games = cur.fetchall()

# combine all games

all_games = windows_games + mac_games + linux_games

# write to csv with headers

with open('platform_dist.csv', 'w') as f:
    f.write("id,platform,is_free\n")
    for row in all_games:
        f.write(f"{row[0]},{row[1]},{row[2]}\n")


