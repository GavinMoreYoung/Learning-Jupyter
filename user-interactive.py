from bokeh.io import output_notebook, show
from bokeh.layouts import widgetbox
from bokeh.models.widgets import TextInput
from bokeh.models import WidgetBox, Button
import numpy as np
import pandas as pd
from bokeh.plotting import figure, show
from bokeh.layouts import layout

# output_notebook()
# load the vote counts
from_counts = np.load("from_counts.npy")
# convert array to a dataframe (Histogram requires a dataframe)
df = pd.DataFrame({'Votes':from_counts})
#print(df.head())
p = figure(plot_height=200,plot_width=600, title="How Many Votes Made byUsers")
p.vbar(x=range(0,6110), width=0.5, bottom=0,top=df.Votes, color="firebrick")
button = Button(label="Foo", button_type="success")
text = TextInput(title="title", value='A Text Box')
widgets = WidgetBox(button, text)
l = layout([p,widgets])
show(l)