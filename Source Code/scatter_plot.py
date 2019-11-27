import pandas as pd
import random

from bokeh.palettes import inferno, magma, mpl, Category20, Set3
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_file, show
from bokeh.models.callbacks import CustomJS
from bokeh.models.widgets import Select
from bokeh.layouts import gridplot
from bokeh.io import output_notebook
from bokeh.models import HoverTool, Legend, TapTool, Circle, CheckboxGroup
from bokeh.models.annotations import Title

hundred_colors = Set3[12] + Category20[20] + magma(15) + inferno(5)

df = pd.read_csv('WikiArtClean.csv')

# columns to store in subset
name_col = ['Title']
categorical_cols = ['Style', 'Category', 'Face or body']
positive_cols = ['Gratitude', 'Happiness', 'Love', 'Humility', 'Trust', 'Optimism']
negative_cols = ['Pessimism', 'Sadness', 'Shame', 'Anger', 'Arrogance', 'Disgust', 'Fear', 'Regret']
all_cols = name_col + categorical_cols + positive_cols + negative_cols

subset = df[all_cols]

# sumup scores and store in new columns
subset['positive_score'] = df[positive_cols].sum(axis=1)
subset['negative_score'] = df[negative_cols].sum(axis=1)

# loop over different categories to assign unique colors 
for col in categorical_cols:
    length = len(subset[col].unique())
    unique_vals = subset[col].unique()
    
    random.shuffle(hundred_colors)
    
    colors_col = hundred_colors[:length]
    
    colors_dict = {}
    
    for key, val in zip(unique_vals, colors_col):
        colors_dict[key] = val
        
    subset[col+" color"] = subset.apply(lambda row: colors_dict.get(row[col]), axis=1)

    style_data = subset['Style color'].tolist()
category_data = subset['Category color'].tolist()
face_data = subset['Face or body color'].tolist()

info1 = subset['Style'].tolist()
info2 = subset['Category'].tolist()
info3 = subset['Face or body'].tolist()

pos_data = subset['positive_score'].tolist()
neg_data = subset['negative_score'].tolist()

titles = subset['Title'].tolist()

data =  {'Style': {'Style':style_data, 'pos':pos_data, 'neg':neg_data, 'info':info1, 'title':titles},
         'Category': {'Style':category_data, 'pos':pos_data, 'neg':neg_data, 'info':info2, 'title':titles},
         'Face or body': {'Style':face_data, 'pos':pos_data, 'neg':neg_data, 'info':info3, 'title':titles}}

### create plot ###
p = figure(x_range=(-0.1,4.1), y_range=(-0.1,4.1), plot_height=850, plot_width=1500, sizing_mode='scale_width',
           x_axis_label='Positive Total Score', 
           y_axis_label='Negative Total Score')

source = ColumnDataSource(data['Style'])
cir = p.circle(x="pos", y="neg", fill_color="Style", line_color="black", size=9, source=source, legend='info')

p.title.text = 'Negative vs Positive Painting Scores'
p.title.align='center'
p.title.text_font_size = '22pt'
p.yaxis.axis_label_text_font_size = '15pt'
p.xaxis.axis_label_text_font_size = '15pt'
p.yaxis.major_label_text_font_size = '15pt'
p.xaxis.major_label_text_font_size = '15pt'

p.legend.location = "bottom_right"
p.legend.orientation = "vertical"
p.legend.border_line_color = "black"

### add the select category option ###
callback = CustomJS(args = {'source': source, 'data': data}, code="""source.data = data[cb_obj.value]""")
color_select = Select(title="Select Category", value="Style", options = ["Style","Category", "Face or body"])
color_select.js_on_change('value', callback)

### add hover and tap tools ###
hover = HoverTool(tooltips = [('Art Title', '@title'), ('Category', '@info'), 
                              ('Positive', '@pos'), ('Negative', '@neg')])

taptool = TapTool()
tap_code = """
    var selected= source.selected['1d'].indices;
   // console.log('tap, you selected:', data_source['Style'][selected])
    
    var data = source.data,
    selected = source.selected.indices,
    select_inds = [];
    
    console.log('tap, you selected:', data['Style'][selected])
    
    if(selected.length == 1){
        selected_id = data['Style'][selected]
        for (var i = 0; i < data['Style'].length; ++i){
            if(data['Style'][i] == selected_id){
                select_inds.push(i)
            }
        }
    }
    source.selected.indices = select_inds 
    source.change.emit();
"""
tap_callback = CustomJS(code = tap_code, args={'source': source})
p.add_tools(hover, TapTool(callback=tap_callback))

# create layout for viz and HTML output
layout = gridplot([[p],[color_select]])
output_file("scatter_plot.html")