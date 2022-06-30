#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

import dash
from jupyter_dash import JupyterDash

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

import dash_bootstrap_components as dbc

import plotly.graph_objs as go
from dash.dependencies import Input, Output
from dash import no_update


from dash import dcc
from dash import html


# In[2]:


pd.set_option('display.max_colwidth', 255)


# # Read files

# In[3]:


types = pd.read_csv(r'files/types.csv')
types.dropna(inplace=True)

final = pd.read_csv(r"files/final.csv")


# # colors

# In[6]:


colors = {
    'ISTJ': '#EDC277',
    'ISTP': '#00806A',
    'ISFJ': '#00E3CC',
    'ISFP': '#400036',
    'INFJ': '#F2668B',
    'INFP': '#C4EEF2',
    'INTJ': '#267365',
    'INTP': '#D9D0C',
    'ESTP': '#B33F00',
    'ESTJ': '#F2CDAC',
    'ESFP': '#151F30',
    'ESFJ': '#B2BEBF',
    'ENFP': '#E67300',
    'ENFJ': '#7A577A',
    'ENTP': '#04D9D9',
    'ENTJ': '#F23030',
}


# In[ ]:





# # Graphs

# # Types

# In[7]:


types_pie = pd.read_csv(r'files/types_pie.csv')


# In[8]:


treeDownList = ['Male', 'Female']
tree_dropdown = dbc.Container(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(dd, id=dd, className='rounded-2') for dd in treeDownList
            ],
            label="Option",
            toggleClassName="dropdown-menu-dark",
            color='dark',
            menu_variant = 'dark',
            className="",  # add bottom margin
            id = 'tree-dropdown'
        ),
        dcc.Graph(id="tree-graph"),

    ], className='p-4'
)


# In[ ]:





# In[ ]:



# ## Drop down types

# In[ ]:





# # Heros Villains

# In[10]:


heros_ = pd.read_csv(r'files/heros_villains.csv')


# In[11]:


HV = heros_.sort_values('total', ascending=False)


# In[12]:


y = HV['type']
x1 = HV['heros']
x2 = HV['villains']


import plotly.graph_objects as go

types_bar = go.Figure()

types_bar.add_trace(go.Bar(
    x=y,
    y=x1,
    name='Heros',
#     orientation='h',
    marker=dict(
        color='rgba(58, 71, 80, 0.6)',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))

types_bar.add_trace(go.Bar(
    text='',
    x=y,
    y=x2,
    name='Villains',
#     orientation='h',
    marker=dict(
        color='red',
        line=dict(color='rgba(58, 71, 80, 1.0)', width=3)
    )
))
types_bar.update_yaxes(categoryorder='total ascending')
types_bar.update_layout(
    height = 500,
    width = 700,
    barmode='stack',
    legend = dict(orientation="h",
    yanchor="bottom",
    y=1.02,
    xanchor="right",
    x=1),
    margin = {'t': 20, 'r': 20},
    title = {'x': .1, 'y':.95, 'text': 'Heros vs Villains'},
    paper_bgcolor='rgba(0,0,0,0)',


)


# In[ ]:





# # Polar chart

# In[15]:


comp = pd.read_csv(r"files/movies_series_comp.csv")
comp.rename(columns={'Unnamed: 0': "cat"}, inplace=True)


# In[16]:


polar_graph = go.Figure()

trace1 = go.Scatterpolar(
    r=comp['movies'],
    theta=comp['cat'],
    fill='toself',
    name='Movies',
    uid = 'g1',
    marker = dict(
        color = "#FF5F5D",
        symbol = "octagon",
        size = 8
        )
)

trace2 = go.Scatterpolar(
    connectgaps = True,
    r=comp['series'],
    theta=comp['cat'],
    fill='toself',
    name='Series',
    uid = 'g2',
    marker = dict(
        color = "#00CCBF",
        symbol = "x",
        size = 8
        )
)


polar_graph.add_trace(trace1)
polar_graph.add_trace(trace2)

polar_graph.update_layout(
#     title = 'Comparison',
    margin = {'l': 50, 'r': 0, 't': 0, 'b': 0},
    legend={'bgcolor': 'white'},
    height = 450,
    width = 450,
    showlegend=True,
    paper_bgcolor='rgb(0,0,0,0)',
#     plot_bgcolor='rgb(0,0,0,0)',
)
polar_graph.update_yaxes(automargin=True)
polar_graph.update_xaxes(automargin=True)


# # Components

# ## BANs

# In[17]:


Bans_Style={'color': '#025159', 'font-family': 'Gentium Book Plus', 'font-weight': 'bold'}


# In[18]:


# Rarest class
rare_type = types.min()
common_type = types.max()


# In[19]:


rarest = html.Div([
    html.Div([
        html.H2(f"{rare_type['Population']}%",
                style={'color': '#7A577A', 'font-family': 'Gentium Book Plus', 'font-weight': 'bold'}),
        html.H6(f"Rarest Class: {rare_type['Type']}",
                style={'color': '#7A577A', 'font-family': 'Gentium Book Plus', 'font-weight': 'bold'})
    ], className='p-2 shadow text-center border rounded-3', style={'background-color': '#F2ECE4'})
], className='col-3')

common = html.Div([
    html.Div([
        html.H2(f"{common_type['Population']}%",
                style={'color': '#00806A', 'font-family': 'Gentium Book Plus', 'font-weight': 'bold'}),
        html.H6(f"Common Class: {common_type['Type']}",
                style={'color': '#00806A', 'font-family': 'Gentium Book Plus', 'font-weight': 'bold'})
    ], className='p-2 shadow text-center border rounded-3', style={'background-color': '#F2ECE4'})
], className='col-3')

total = html.Div([
    html.Div([
        html.H2(f"7", style=Bans_Style),
        html.H6("Categories", style=Bans_Style)
    ], className='p-2 shadow text-center border rounded-3', style={'background-color': '#F2ECE4'})
], className='col-3')

types_count = html.Div([
    html.Div([
        html.H2(16, style=Bans_Style),
        html.H6("16 Personality types", style=Bans_Style)
    ], className='p-2 shadow text-center border rounded-3', style={'background-color': '#F2ECE4'})
], className='col-3')


# # map drop down

# In[20]:


types_list = types["Type"].value_counts().index.tolist()


# In[21]:


map_dropdown = dbc.Container(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(dd, id=dd, className='rounded-2') for dd in types_list
            ],
            label="Type",
            toggleClassName="dropdown-menu-dark",
            color='dark',
            menu_variant = 'dark',
            className="mb-3",  # add bottom margin
            id = 'map-dropdown'
        ),
        dcc.Graph(id="map-graph"),

    ], className='p-4 border border-info'
)


# # Types drop down

# In[22]:


downDownList = ['Population', 'Comparison']
types_dropdown = dbc.Container(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem(dd, id=dd, className='rounded-2') for dd in downDownList
            ],
            label="Option",
            toggleClassName="dropdown-menu-dark",
            color='secondary',
            menu_variant = 'secondary',
            className="",
            id = "Types-Drop"
        ),
        dcc.Graph(id="types-graph"),

    ], className='p-4 border border-info'
)


# ## Polar dropdown

# In[23]:


polar_dropdown = dbc.Container(
    [
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("Movies", id="movies", className='rounded-2'),
                dbc.DropdownMenuItem("Series", id="series", className='rounded-2'),
                dbc.DropdownMenuItem("Anime", id="anime", className='rounded-2'),
                dbc.DropdownMenuItem("Sports", id="sports", className='rounded-2'),
            ],
            label="Movies",
            toggleClassName="dropdown-menu-secondary",
            color="#FF5F5D",
            menu_variant = 'secondary',
            className="p-2 d-inline",
            id= 'polar-dropdown1'
        ),
        dbc.DropdownMenu(
            [
                dbc.DropdownMenuItem("Movies", id="movies2", className='rounded-2'),
                dbc.DropdownMenuItem("Series", id="series2", className='rounded-2'),
                dbc.DropdownMenuItem("Anime", id="anime2", className='rounded-2'),
                dbc.DropdownMenuItem("Sports", id="sports2", className='rounded-2'),
            ],
            label="Series",
            toggleClassName="dropdown-menu-secondary",
            color="#00CCBF",
            menu_variant = 'secondary',
            className="p-2 d-inline",
            id= 'polar-dropdown2'
        ),
        dcc.Graph(id="polar-graph"),
    ], className='pt-3 border border-info'
)


# # table

# In[ ]:





# In[24]:


from dash import Dash, dash_table
from dash.dash_table import DataTable, FormatTemplate
from collections import OrderedDict

from dash.dash_table.Format import Format, Group, Prefix, Scheme, Symbol


# In[25]:


table_data = pd.read_csv(r'files/table.csv')


# In[26]:


table_data.rename(columns={'Unnamed: 0': 'type'}, inplace=True)



th = ['type',
    'historical',
    'science',
    'fashion',
    'football',
    'basketball',
#     'chess',
 ]


# In[29]:


table_header = [
    html.Thead(html.Tr(
        [html.Th(s.capitalize(), className='text-center') for s in th]
    ), className='table-dark')
]

rows = [
    html.Tr([
    html.Th(row['type'], className='table-light text-center align-middle'),
    html.Td(row["historical"], className='text-center p-1'), 
    html.Td(row["science"], className='text-center p-1'),
    html.Td(row["fashion"], className='text-center p-1'),
    html.Td(row["football"], className='text-center p-1'),
    html.Td(row["basketball"], className='text-center p-1'),
#     html.Td(row["chess"], className='text-center p-1'),
    ]) for index, row in table_data.iterrows()
]

table_body = [html.Tbody(rows)]

table = dbc.Table(table_header + table_body, bordered=True, className='table table-hover', size='sm')


# In[30]:


def highlight_max_row(df):
    df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
    return [
        {
            'if': {
                'filter_query': '{{id}} = {}'.format(i),
                'column_id': col
            },
            'backgroundColor': '#BD2A2E',
            'color': 'white',
            'font-weight': 'bold'
        }
        # idxmax(axis=1) finds the max indices of each row
        for (i, col) in enumerate(
            df_numeric_columns.idxmax(axis=1)
        )
    ] + [
        {
            'if': {
                'filter_query': '{{id}} = {}'.format(i),
                'column_id': col
            },
            'backgroundColor': '#889C9B',
            'color': 'white'
        }
        # idxmax(axis=1) finds the min indices of each row
        for (i, col) in enumerate(
            df_numeric_columns.idxmin(axis=1)
        )
    ] + [
        {
            'if': {
                'column_id': 'type',
            },
            'backgroundColor': 'lightgrey',
            'color': 'black'
        }
    ]
    
    
percentage = FormatTemplate.percentage(2)

df = table_data[th]
df['id'] = df.index
table_2 = dash_table.DataTable(
#     fill_width=False,
    style_table = {'width':'100%',
                   'border': '1px solid #EEEEEE',
                   'border-radius': '10px',
                   'font-size': '14px'
                  },
    style_cell = {
        'padding': '8px',
        'textAlign': 'center',
                 },
    style_header={
        'backgroundColor': 'white',
        'fontWeight': 'bold'
    },
    style_data={
        'backgroundColor': '#f2f2f2',
        'color': 'black'
    },
    data=df.to_dict('records'),
    sort_action='native',
    columns=[{'name': i.capitalize(), 'id': i} for i in df.columns if i != 'id'],
    style_data_conditional=highlight_max_row(df),
)


# In[ ]:





# # App Layout

# In[31]:


app = JupyterDash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server
app.title = "Personality Dashboard"
app.layout = html.Div(
    [
        # header
        html.Div([
            html.H1("Personality Types", style={'color': '#324E73', 'font-family': 'Proxima Nova', 'font-weight': 'bold'})
        ], className='container mb-3 pt-2'),
        
        html.Hr(),

        # BANS
        html.Div([
            html.Div([
            common,
            rarest,
            types_count,
            total,
  
        ], className='row')
            
        ], className='container mb-4'),
        
        # body
        # first section
        html.Div([
            # map
            html.Div([
                html.Div([
                    types_dropdown
                    
                ], className="shadow"),
                
            ], className="col-6"),
            
            
            # funned
            html.Div([

                html.Div([
                    map_dropdown,
                     
                ], className='shadow'),
            ], className='col-6'),

            
        ], className='container-fluid row'),
        
        html.Hr(),
        # section 2
        html.Div([
            # map
            html.Div([
                html.Div([
                    polar_dropdown
                ], className="shadow"),
                
            ], className="col-5"),
            
            # polar
            html.Div([
                html.Div([
                    dcc.Graph(figure=types_bar)
                ], className='shadow'),
            ], className='col-7'),
            
        ], className='container-fluid row'),
        
        html.Hr(),
        # section 3
        html.Div([
            html.Div([
                # table
                html.Div([
                    tree_dropdown
                ], className='col-6'),
                
                # tree
                html.Div([
                    table_2,
                    html.H4('Numbers shown in the table are percentages', className='lead text-center')
                ], className='col-6', style={'padding-top': '105px', 'padding-right': '50px'})
            ], className='row')
        ], className="container-fluid mb-5"),
        
        html.Hr(),
    

], className='bg-light bg-gradient overflow-hidden')

# polar call back
@app.callback(
   [Output("polar-graph", "figure"),
    Output("polar-dropdown1", 'label'),
    Output("polar-dropdown2", 'label')],
    [
        Input("movies", "n_clicks"),
        Input("series", "n_clicks"),
        Input("anime", "n_clicks"),
        Input("sports", "n_clicks"),
        
        Input("movies2", "n_clicks"),
        Input("series2", "n_clicks"),
        Input("anime2", "n_clicks"),
        Input("sports2", "n_clicks")
    ]
)

def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        return polar_graph, no_update, no_update
    else:
        category = ctx.triggered[0]["prop_id"].split(".")[0]

    if category == "movies":
        polar_graph.update_traces(
            selector = {'uid' : 'g1'},
            r = comp['movies'],
            theta = comp['cat'],
            name = 'Movies'
        )
        
    elif category == "series":
        polar_graph.update_traces(
            selector = {'uid' : 'g1'},
            r = comp['series'],
            theta = comp['cat'],
            name = 'Series'
        )
        
    elif category == "anime":
        polar_graph.update_traces(
            selector = {'uid' : 'g1'},
            r = comp['anime'],
            theta = comp['cat'],
            name = 'Anime'
        )
        
    elif category == "sports":
        polar_graph.update_traces(
            selector = {'uid' : 'g1'},
            r = comp['sports'],
            theta = comp['cat'],
            name = 'Sports'
        )
    
    if category == "movies2":
        polar_graph.update_traces(
            selector = {'uid' : 'g2'},
            r = comp['movies'],
            theta = comp['cat'],
            name = 'Movies'
        )
        
    elif category == "series2":
        polar_graph.update_traces(
            selector = {'uid' : 'g2'},
            r = comp['series'],
            theta = comp['cat'],
            name = 'Series'
        )
        
    elif category == "anime2":
        polar_graph.update_traces(
            selector = {'uid' : 'g2'},
            r = comp['anime'],
            theta = comp['cat'],
            name = 'Anime'
        )
        
    elif category == "sports2":
        polar_graph.update_traces(
            selector = {'uid' : 'g2'},
            r = comp['sports'],
            theta = comp['cat'],
            name = 'Sports'
        )
    
    if category[-1] == "2":
        return polar_graph, no_update, category[:-1].capitalize()
    else:
        return polar_graph, category.capitalize(), no_update
        

# map call back
@app.callback(
    [Output("map-graph", "figure"),
    Output("map-dropdown", 'label'),
    Output("map-dropdown", 'color')],
    [
        Input(dd_in, "n_clicks") for dd_in in types_list
    ],
)
def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "INTJ"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    countries = pd.read_csv(r"files/countries_f.csv", encoding= 'unicode_escape')
    
    map_graph = px.choropleth(countries[countries['type']== button_id], locations='code', color='type',
                            color_discrete_map = colors,
                           hover_name='country',
                           scope='world',
                          center = {'lat': 36.033333, "lon": 31.233334}
                          )
    
    map_graph.update_layout(
    autosize=False,
    height = 350,
    width= 580,
    title_text = 'Personality Distribution',
    title_x = .5,
    title_y = 1,
    margin={"r":0,"t":0,"l":0,"b": 0, 'pad': 0},
    legend = {'orientation': 'h',
                'title': None,
                'yanchor': "top",
                'y': 1,
                'xanchor': "left",
                'x': .89
                },
    geo=dict(
        showframe=False,
#         bgcolor = 'rgba(0,0,0,0)',
        
    ),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    
    )
    c = colors[button_id.upper()]
        
    return map_graph, button_id.upper(), c


# map call back
@app.callback(
    [Output("types-graph", "figure"),
    Output("Types-Drop", "label")],
    [
        Input(dd_in, "n_clicks") for dd_in in downDownList
    ],
)
def make_graph(*args):
    ctx = dash.callback_context

    if not ctx.triggered:
        button_id = "Population"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
        
    if button_id == 'Comparison':
        pop_types = pd.read_csv(r'files/types_comp.csv')
        
        types_graph = px.bar(pop_types, x="Type", y="percent", color="gender", barmode='group',
                             color_discrete_map={'Male': '#184C78', 'Female': '#FF4858'})
        types_graph.update_layout(
            autosize=False,
            height= 366,
            width=580,
            xaxis= {'title': None},
            margin= {'l': 10, 'r':0, 't': 20, 'b': 20},
             legend = {'orientation': 'h',
                'title': None,
                'yanchor': "top",
                'y':1.1,
                'xanchor': "left",
                'x': .7
                },
            paper_bgcolor='rgba(0,0,0,0)',
        )

        return types_graph, button_id
    
    
    types_graph = px.bar(types, x="Type", y=button_id)
    types_graph.update_layout(
        autosize=False,
        height= 366,
        width=580,
        margin = {'l': 10, 'r': 10, 't': 20, 'b': 20},
        xaxis={'categoryorder':'total descending', 'title':None, 'showticklabels': True},
        yaxis={'title': 'Percentage'},
        paper_bgcolor='rgba(0,0,0,0)',
#         plot_bgcolor='rgba(0,0,0,0)',
    )
    
    types_graph.update_traces(marker_color='#025159')
    return types_graph, button_id


@app.callback(
    [Output("tree-graph", "figure"),
     Output("tree-dropdown", "label"),
     Output("tree-dropdown", "color")],
    [
        Input(dd_in, "n_clicks") for dd_in in treeDownList
    ],
)

def tree_graph(*args):
    ctx = dash.callback_context
    
    if not ctx.triggered:
        button_id = "Male"
    else:
        button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    
    root = '#184C78' if button_id == 'Male' else '#FF4858'
    
    colors = {
    '(?)' : root,
    'ISTJ': '#EDC277',
    'ISTP': '#00806A',
    'ISFJ': '#00E3CC',
    'ISFP': '#400036',
    'INFJ': '#F2668B',
    'INFP': '#C4EEF2',
    'INTJ': '#267365',
    'INTP': '#D9D0C',
    'ESTP': '#B33F00',
    'ESTJ': '#F2CDAC',
    'ESFP': '#151F30',
    'ESFJ': '#B2BEBF',
    'ENFP': '#E67300',
    'ENFJ': '#7A577A',
    'ENTP': '#04D9D9',
    'ENTJ': '#F23030',
    }
    types_pie = pd.read_csv(r'files/types_pie.csv')
    
    tree = px.treemap(types_pie[types_pie['gender']== button_id], path=['Type'],
                      values='percent', color='Type', color_discrete_map=colors)
    tree.update_traces(root_color="lightgrey")
    tree.update_layout(
        margin = dict(t=50, l=25, r=25, b=25),
        height=630, width=600,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    return tree, button_id, root
    


if __name__ == "__main__":
    app.run_server(debug=True)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




