import dash
import plotly.express as px
import pandas as pd
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

# Data Exploration with Pandas
# --------------------------------------

df = pd.read_csv("vgsales.csv")

# Interactive Graphing with Dash
# ------------------------------
app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1('Graph Analysis with Charming Data'),
    dcc.Dropdown(id='genre-choice',
                 options=[{'label': x, 'value': x}
                          for x in sorted(df.Genre.unique())],
                 value='Sports'
                 ),

    dcc.Graph(id='my-graph', figure={})

])


@app.callback(
    Output(component_id='my-graph', component_property='figure'),
    Input(component_id='genre-choice', component_property='value')
)
def interactive_graphing(value_genre):
    print(value_genre)
    dff = df[df.Genre==value_genre]
    fig = px.bar(data_frame=dff, x='Year', y='World Sales')
    return fig


if __name__ == '__main__':
    app.run_server()
