from pathlib import Path

from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import plotly.express as px


import pandas as pd


EVENT_DATA_FILEPATH = Path(__file__).parent.joinpath('data', 'events.csv')
cols = ['REF', 'TYPE', 'YEAR', 'LOCATION', 'EVENTS',
        'SPORTS', 'COUNTRIES', 'MALE', 'FEMALE', 'PARTICIPANTS']
df_events = pd.read_csv(EVENT_DATA_FILEPATH, usecols=cols)
line_events = px.line(df_events,
                      x='YEAR',
                      y='EVENTS',
                      template="simple_white"
                      )
line_events.add_annotation(  # add a text callout with arrow
    text="1984 held in New York & Stoke Mandeville",
    x=1984,
    y=976,
    arrowhead=1,
    showarrow=True
)

df_events['M%'] = df_events['MALE'] / df_events['PARTICIPANTS']
df_events['F%'] = df_events['FEMALE'] / df_events['PARTICIPANTS']
df_gender = df_events.loc[df_events['TYPE'] == "Winter"]
df_gender = df_gender.sort_values(['YEAR'], ascending=(True))
df_gender['xlabel'] = df_gender['LOCATION'] + \
    ' ' + df_gender['YEAR'].astype(str)
bar_events = px.bar(df_gender, x='xlabel', y=[
                    'M%', 'F%'], title="Has the ratio of male and female athletes changed over time?")
bar_events.update_xaxes(showticklabels=False, visible=False)
bar_events.update_yaxes(showticklabels=False, visible=False)


DATA_PATH = Path(__file__).parent.joinpath('data')

app = Dash(__name__,
           external_stylesheets=[dbc.themes.BOOTSTRAP],
           meta_tags=[
               {"name": "viewport", "content": "width=device-width, initial-scale=1"},
           ],
           )

app.layout = dbc.Container(
    [
        html.H1("Paralympic Medals Dashboard"),
        html.H2(
            "Has the number of athletes, nations, events and sports changed over time?"),
        dcc.Graph(
            id='line-sports',
            figure=bar_events
        )
    ],
    fluid=True,
)

if __name__ == '__main__':
    app.run_server(debug=True)
