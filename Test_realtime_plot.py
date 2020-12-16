import bokeh

bokeh.sampledata.download()

import pandas as pd
from bokeh.plotting import figure
from bokeh.sampledata.stocks import AAPL

df = pd.DataFrame(AAPL)
df.index = pd.to_datetime(df['date'])
dfi = df.drop(['date'], axis=1)

import numpy as np
from bokeh.io import output_notebook, show
from bokeh.plotting import figure

p = figure(plot_width=500, plot_height=900, x_axis_type="datetime")
p.line(df.index, df["close"], color="navy", alpha = 0.5)

import jinja2
from bokeh.embed import components
template = jinja2.Template('''\
<html>
<link href='http://cdn.pydata.org/bokeh/release/bokeh-1.4.0.min.css' rel='stylesheet' type='text/css'>
<script src='http://cdn.pydata.org/bokeh/release/bokeh-1.4.0.min.js'></script>
<head><title>bokeh test</title>
<head>
<body>
<h1>This is a webpage for the bokeh library test</h1>

{{script}}
{{div}}

</body>
</html>
'''
                          )

script, div = components(p)

with open("bokeh_graphweb.html", "w") as f:
    f.write(template.render(script=script, div=div))
    
import webbrowser
webbrowser.open("index.html")
