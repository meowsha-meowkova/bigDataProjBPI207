# bigDataProjBPI207

## Prerequisites

Download json with games info from kaggle (already in repo).
https://www.kaggle.com/datasets/souyama/steam-dataset

Put steam_sotre_data.json in project directory.

Start postgres server on port 5432 (default) and db Maria (Postgres.app used for mac)

## Files descriptions in order

### load_in_db.py
create table games and drop it if it already exists.
read steam_store_data.json and for each item execute and insert 

### get_db_stats.py
get the number of rows in the table
print the result

### get_csv.py
get data and write to csv file with header

### get_platform_dist.py
gets the data in platform separated view. Each row corresponds to one platform.
create and write a csv with columns: id, platform, is_free

### get_ml_csv.py
select everything from the table except the id, name, and release_date columns but add days_since_release column
write the rows to csv file


## Training ML model
Training was done on native apple mac program "Create ML". That allows for a gui to make different kinds of ml models. I chose to make a tabular regression model as the data was in tabular form and the data to predict was a continious number.

## Purpose of requirements.txt

This file stores the specific versions numbers for the libraries that my project requires.

