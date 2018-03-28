import sqlite3


con = sqlite3.connect("stuff.db")
con.row_factory = sqlite3.Row
cur = con.cursor()


""" 
    query to answer the question: get the athlete name, sport, year, gender and medal of all athletes
    who have won more than one medal and group them by name and sport in ascending order 
"""
def getMedals(year):
    query = "SELECT athlete, UPPER(sport) AS discipline, year, gender, medal, " \
            "COUNT(*) AS total FROM winners where year >= " + str(year) + \
            " GROUP BY athlete, discipline HAVING total > 1 ORDER BY discipline ASC"
    cur.execute(query)

    medal_winner = cur.fetchone()

    total_winners = 0


    #create the format for data for graph
    disciplines = []

    genders = ['Men', 'Women']

    data = {
        'men': [],
        'women': []
    }


    """ 
        loops through list and adds multiple medal winner count in specific format for graph
        where men and women are counted separately 
    """
    while medal_winner != None:
        total_winners = total_winners + 1

        """ 
            create the graph relationship between the discipline and total number.
            this loops through and creates the discipline if it isn't there already and attaches the 0 to the total
        """
        if medal_winner["discipline"] not in disciplines:
            disciplines.append(medal_winner["discipline"])
            data['men'].append(0)
            data['women'].append(0)

        """ 
            this loop runs through athletes and totals the number by adding 1 for each new name 
            data['women'] = data['women'] + 1
        """
        if medal_winner['gender'] != 'men':
            data['women'][-1] +=1
        else:
            data['men'][-1] +=1

        medal_winner = cur.fetchone()


    print("total medalists since %s: %s" % (year, total_winners))
    range = [(discipline, gender) for discipline in disciplines for gender in genders]

    return dict(data=data, genders=genders, disciplines=disciplines, range=range)