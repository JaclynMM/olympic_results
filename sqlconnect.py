import sqlite3, csv

# con = sqlite3.connect(":memory:")
con = sqlite3.connect("stuff.db")
cur = con.cursor()

# creates and connects data to sqlite database, create table if it does not already exist
cur.execute("""CREATE TABLE IF NOT EXISTS winners (post_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, city TEXT NOT NULL, sport TEXT NOT NULL, discipline TEXT NOT NULL, athlete TEXT NOT NULL, country TEXT NOT NULL, gender TEXT NOT NULL, event TEXT NOT NULL, medal TEXT NOT NULL, year INTEGER NOT NULL)""")

# directions on setting up the database
with open('./output_data/totalresults.csv','r') as person_table:
    dr = csv.DictReader(person_table, delimiter=',') # comma is default delimiter

    #special code to take any athlete name with a comma and reverse order while also delete comma
    to_db = [(i['City'], i['Sport'], i['Discipline'], ' '.join(i['Athlete'].split(", ")[::-1]), i['Country'], i['Gender'], i['Event'], i['Medal'], i['Year']) for i in dr]

cur.execute("DELETE FROM winners")

cur.executemany("INSERT INTO winners VALUES (NULL,?,?,?,?,?,?,?,?,?);", to_db)
con.commit()