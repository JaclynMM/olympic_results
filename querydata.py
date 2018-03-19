import sqlite3, csv


# con = sqlite3.connect(":memory:")
con = sqlite3.connect("stuff.db")
con.row_factory = sqlite3.Row
cur = con.cursor()


# cur.execute("SELECT * FROM winners")
# cur.execute("SELECT athlete, sport, medal, gender, year FROM winners WHERE country = 'usa'")
cur.execute("SELECT athlete, UPPER(sport) AS discipline, gender, medal, COUNT(*) AS total FROM winners GROUP BY athlete, discipline HAVING total > 1 ORDER BY discipline ASC")


medal_winner = cur.fetchone()


total_winners = 0


disciplines = []

genders = ['Men', 'Women']

data = {
    'men': [],
    'women': []
}


while medal_winner != None:
    total_winners = total_winners + 1
    # print ('%s %s %s' % (usa_winner[2], usa_winner[1], usa_winner[0]))
    # print ('%s' % (type(usa_winner)))
    print ('%(discipline)s %(athlete)s %(gender)s %(medal)s' % (medal_winner))
    # print ('%(year)s' % { 'year': 2017 })

    if medal_winner["discipline"] not in disciplines:
        disciplines.append(medal_winner["discipline"])
        data['men'].append(0)
        data['women'].append(0)

    if medal_winner['gender'] != 'men':
        # data['women'] = data['women'] + 1
        data['women'][-1] +=1
    else:
        data['men'][-1] +=1



    medal_winner = cur.fetchone()


print(total_winners)







