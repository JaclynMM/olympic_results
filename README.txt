README

Project Description:
In this project I wanted to compare all the Olympic Medal Winners (total).
I wanted to find out the differences in gender between multiple medal winners.
How many men won more than one medal in each sport or vice versa.


Installs Needed:
Phython3
Bokeh


Files Included:
- input_data folder contains all original data found on internet and what I made myself to have complete data
- output_data folder contains the dataset created when everything was combined into one for further analysis
- venv folder contains my virtual environment
- datamerge.py
- sqlconnect.py
- querydata.py
- graphing.py
- graphing_results.html
- stuff.db (sqlite database)


Process of Project (file order and breif description of what file does)
1. datamerge.py: this is the code where I combined all the original datasets into one
                 and neutralized everything to make it all lowercase
2. sqlconnect.py: in this file I create the database, dump all data into it and create a table called "winners"
3. querydata.py: creates a query of the data I want to pull specifically for graphing purposes
4. graphing.py: this file is where I implement bokeh to graph the data found
5. graphing_results.html: visual graph created from running the bokeh file

bokeh serve --show graphing.py