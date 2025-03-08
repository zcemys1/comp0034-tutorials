# Imports for Dash and Dash.html
import pathlib
import os
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from importlib import resources
import pandas as pd
import plotly.express as px


# Variable that defines the meta tag for the viewport
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.YETI]

#line chart function

def line_chart(feature):
    """ Creates a line chart using data from paralympics.csv """

    if feature not in ["sports", "participants", "events", "countries"]:
        raise ValueError('Invalid feature. Must be one of ["sports", "participants", "events", "countries"]')

    # ✅ Use the absolute file path (from what you provided)
    file_path = r"C:\Users\uswe\OneDrive - University College London\Desktop\COMP0035 24-25\New folder\comp0034-tutorials\src\student\data\paralympics.csv"

    # ✅ Check if the file exists before reading
    import os
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"❌ File not found: {file_path}")

    # Read the dataset
    df = pd.read_csv(file_path, usecols=["type", "year", "host", feature])

    # Create a Plotly Express line chart
    fig = px.line(df, x="year", y=feature, color="type",
                  title=f"How has the number of {feature} changed over time?",
                  labels={"year": "Year", feature: ""},
                  template="simple_white")
    
    return fig
# Create an instance of the Dash app and Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# create line chart
line_fig = line_chart("sports")  # Default is "sports", can change later

# Row 1: App Title and Description
row_one = dbc.Row([
    dbc.Col([
        html.H1("Paralympics Data Analytics"),
        html.P("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida.")
    ], width=12, className="text-center")
], className="mb-4")

# Row 2: Drop-down (left) & Checkboxes (right) with spacing
row_two = dbc.Row([
    dbc.Col([
        dbc.Select(
            options=[
                {"label": "Events", "value": "events"},
                {"label": "Sports", "value": "sports"},
                {"label": "Countries", "value": "countries"},
                {"label": "Athletes", "value": "participants"},
            ],
            value="events",
            id="dropdown-input"
        )
    ], width=4),


    dbc.Col([
        html.Div([
            dbc.Label("Select the Paralympic Games type"),
            dbc.Checklist(
                options=[
                    {"label": "Summer", "value": "summer"},
                    {"label": "Winter", "value": "winter"},
                ],
                value=["summer"],
                id="checklist-input"
            )
        ])
    ], width={"size": 4, "offset": 4})  # Adds spacing between the dropdown and checkboxes
], className="mb-4")


# Row 3: Placeholder Images for Charts
row_three = dbc.Row([
    dbc.Col(dcc.Graph(id="line-chart", figure=line_fig), width=6),
    dbc.Col(html.Img(src=app.get_asset_url('bar-chart-placeholder.png'), className="img-fluid"), width=6)
], className="mb-4")
# Row 4: Map Placeholder and Event Card
row_four = dbc.Row([
    dbc.Col(html.Img(src=app.get_asset_url('world-map-placeholder.png'), className="img-fluid"), width=8),
    dbc.Col(dbc.Card([
        dbc.CardImg(src=app.get_asset_url("logos/2022_Beijing.jpg"), top=True),
        dbc.CardBody([
            html.H4("Beijing 2022", className="card-title"),
            html.P("Number of athletes: XX", className="card-text"),
            html.P("Number of events: XX", className="card-text"),
            html.P("Number of countries: XX", className="card-text"),
            html.P("Number of sports: XX", className="card-text"),
        ])
    ], style={"width": "18rem"}), width=4)
], className="mb-4")


# Add an HTML layout to the Dash app
# Wrap the layout in a Bootstrap container
app.layout = dbc.Container([
    row_one,
    row_two,
    row_three,
    row_four,
])

# Run the app
if __name__ == '__main__':
    app.run(debug=True, port=5050)
