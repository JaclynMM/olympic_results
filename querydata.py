import sqlite3, csv


# con = sqlite3.connect(":memory:")
con = sqlite3.connect("stuff.db")
con.row_factory = sqlite3.Row
cur = con.cursor()

cur.execute("SELECT * FROM winners")
cur.execute("SELECT athlete, sport, year FROM winners WHERE country = 'usa'")

usa_winner = cur.fetchone()


total_winners = 0


while usa_winner != None:
    total_winners = total_winners + 1
    # print ('%s %s %s' % (usa_winner[2], usa_winner[1], usa_winner[0]))
    # print ('%s' % (type(usa_winner)))
    print ('%(year)s %(sport)s %(athlete)s' % (usa_winner))
    # print ('%(year)s' % { 'year': 2017 })

    usa_winner = cur.fetchone()


print(total_winners)




