from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, Dropdown
from bokeh.plotting import figure, curdoc
from bokeh.transform import factor_cmap
from bokeh.layouts import column

from querydata import *


# names the graph html file
# output_file ("./graphing_results.html")


# graphic colors specified
palette = ["#5C9E74", "#F98C6F"]


# graph specs
result = getMedals(1800)
p = figure(width=5000, height=700, toolbar_location="below", toolbar_sticky=False, x_range=FactorRange(*result['range']),
           title="Olympic Winners by Sport & Gender")


counts = sum(zip(result['data']['men'], result['data']['women']), ())
source = ColumnDataSource(data=dict(x=result['range'], counts=counts))


# graph bar specs
r = p.vbar(x='x', top='counts', width=0.5, source=source, line_color="white",
       fill_color=factor_cmap('x', palette=palette, factors=result['genders'], start=1, end=2))


# create a plot and style its properties
p.y_range.start = 0
p.x_range.range_padding = 0.025
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None


# create a callback
def dropdown_callback(attr, old, new):
  result = getMedals(new)
  counts = sum(zip(result['data']['men'], result['data']['women']), ())
  p.x_range = FactorRange(*result['range'])
  r.data_source.data = dict(x=result['range'], counts=counts)


# button details, range restrictions for display, with the callback
menu = [("1900", "1900"), ("1920", "1920"), ("1950", "1950"), ("1960", "1960"), ("1970", "1970"), ("1980", "1980"),
        ("1990", "1990"), ("2000", "2000"), ("2010", "2010"), ("2016", "2016")]
dropdown = Dropdown(label="Start Year", button_type="warning", menu=menu)
dropdown.on_change("value", dropdown_callback)


# add button to the graph page
curdoc().add_root(column(dropdown, p))
