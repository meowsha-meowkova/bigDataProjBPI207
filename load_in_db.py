# connect to postgres database

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

drop_table = f"DROP TABLE IF EXISTS {table_name}"

cur = conn.cursor()
cur.execute(drop_table)

create_table = f"""CREATE TABLE {table_name}(
    id SERIAL PRIMARY KEY,
    type VARCHAR(255),
    name VARCHAR(255),
    required_age INTEGER,
    is_free BOOLEAN,
    platform_windows BOOLEAN,
    platform_mac BOOLEAN,
    platform_linux BOOLEAN,
    metacritic_score INTEGER,
    categories_array VARCHAR(255)[],
    genres_array VARCHAR(255)[],
    recommendations INTEGER,
    release_date DATE,
    first_group_price_cents INTEGER
)""" 

cur.execute(create_table)
conn.commit()

import json

# the json file is a dictionary with ids as keys and game info as values

with open("steam_store_data.json") as f:
    data = json.load(f)

    # for each key value pair in the dictionary
    for key, value in data.items():
        id = key
        type = value["type"]
        name = value["name"]
        required_age = value["required_age"]
        is_free = value["is_free"]
        platform_windows = value["platforms"]["windows"]
        platform_mac = value["platforms"]["mac"]
        platform_linux = value["platforms"]["linux"]
        #  metacritic can be null so we need to check if it exists
        metacritic_score = value.get("metacritic", {}).get("score", None)
        # get array of strings from array of dictionaries with key "description"
        categories_array = [category["description"] for category in value.get("categories", [])]

        genres_array = [genre["description"] for genre in value.get("genres", [])]
        recommendations = value.get("recommendations", {}).get("total", None)
        release_date = value["release_date"]["date"]

        # path: package_groups[0]["subs"][0]["price_in_cents_with_discount"]
        # the arrays can be empty so we need to check if they exist
        # first_group_price_cents
        if len(value.get("package_groups", [])) > 0:
            if len(value["package_groups"][0].get("subs", [])) > 0:
                first_group_price_cents = value["package_groups"][0]["subs"][0].get("price_in_cents_with_discount", None)
            else:
                first_group_price_cents = None

        # insert the data into the table

        insert_data = f"""INSERT INTO {table_name}(
            id,
            type,
            name,
            required_age,
            is_free,
            platform_windows,
            platform_mac,
            platform_linux,
            metacritic_score,
            categories_array,
            genres_array,
            recommendations,
            release_date,
            first_group_price_cents
        ) VALUES (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )"""


        try:
            cur.execute(insert_data, (
                id,
                type,
                name,
                required_age,
                is_free,
                platform_windows,
                platform_mac,
                platform_linux,
                metacritic_score,
                categories_array,
                genres_array,
                recommendations,
                release_date,
                first_group_price_cents
            ))
            conn.commit()
        except Exception as e:
            print(f"""Error inserting row for game: {name}""")
            print(e)
            conn.rollback()

