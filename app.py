import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from dash import Dash, dash_table
from collections import OrderedDict
import json

#LECTURA DEL CSV
df = pd.read_csv('generacion-de-energia-electrica-en-mwh-conyx.csv')

#CONEXION BASE DE DATOS
def conectarDB():
    con = create_engine("postgresql://petladncckjelj:3c43bc633c86027bb3b0988306afd6027b7eb31aa3578733d61a51c802a9dd88@ec2-3-223-169-166.compute-1.amazonaws.com:5432/d6msbnm9tiriev")
    return con
con=conectarDB()



external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)


#SECCION DE GRAFICOS Y MAPAS 
app.layout = html.Div([
    #TITULO
        html.Div([
            html.H1('TÓPICOS II'),
            html.Img(src='assets/icono.png')
            ], className = 'banner'),
    
    #SECCIONES
    #SECCION MAPA
    dcc.Tabs([
        dcc.Tab(label='PLANTAS ELÉCTRICAS', children=[
           dcc.Dropdown(id="slct_year",
                 options=[
                     {"label": "2019", "value": 2019},
                     {"label": "2020", "value": 2020},
                     {"label": "2021", "value": 2021}],
                 value=2019,
                 style={'width': "30%"}
                 ),

                html.Div(id='output_container'),
        html.Div([
        dcc.Graph(id='mapa'), 

        ], className = 'create_container2 twelve columns')
          
         
        ]),

        #SECCION GRAFICA
        dcc.Tab(label='TIPO DE GENERACIÓN POR MES', children=[
            
             dcc.Dropdown(id="mes",
                 options=[
                     {"label": "enero", "value": 'enero'},
                     {"label": "febrero", "value": 'febrero'},
                     {"label": "marzo", "value": 'marzo'},
                     {"label": "abril", "value": 'abril'},
                     {"label": "mayo", "value": 'mayo'},
                     {"label": "junio", "value": 'junio'},
                     {"label": "julio", "value": 'julio'},
                     {"label": "agosto", "value": 'agosto'},
                     {"label": "septiembre", "value": 'septiembre'},
                     {"label": "octubre", "value": 'octubre'},
                     {"label": "noviembre", "value": 'noviembre'},
                     {"label": "diciembre", "value": 'diciembre'},
                     ],
                 value='enero',
                 style={'width': "30%"}
                 ),

        html.Div([
            dcc.Graph(id = 'Grafico', figure = {} )
           ], className = 'create_container2 twelve columns')
            
        ]),
    ])
])

#DATOS DROPDOWN
@app.callback(
    Output('mapa','figure'),
    Input('slct_year', 'value')
)

#UPDATES DEL DROPDOWN AL MAPA
def update_output(value):

    if(value==2019):
        querysql = """Select * from electrical_facilities WHERE electrical_facilities.ano = '2019'"""

    elif(value==2020):

        querysql = """Select * from electrical_facilities WHERE electrical_facilities.ano ='2020'"""
    else:

        querysql = """Select * from electrical_facilities WHERE electrical_facilities.ano ='2021'"""


    datos = gpd.read_postgis(querysql,con)

    #MAPA 1
    fig = px.scatter_mapbox(datos, lat=datos.y, lon=datos.x, hover_name="planta", hover_data=["tipo_de_generacion", "renovable"],
                        color_discrete_sequence=["blue"], zoom=6, height=350)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    return fig

#DATOS GRAFICOS
@app.callback(
    Output('Grafico','figure'),
    Input('mes', 'value')
)

#UPDATES DEL DROPDOWN AL GRAFICO
def update_output2(value):
    if value == 'enero':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='enero',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "enero": "ENERO"
                 },
                title="GRAFICO")

    elif value == 'febrero':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='febrero',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "febrero": "FEBRERO"
                 },
                title="GRAFICO")

    elif value == 'marzo':
       fig2 = px.bar(df, x= 'tipo_de_generacion', y='marzo',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "marzo": "MARZO"
                 },
                title="GRAFICO")

    elif value == 'abril':
       fig2 = px.bar(df, x= 'tipo_de_generacion', y='abril',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "abril": "ABRIL"
                 },
                title="GRAFICO")

    elif value == 'mayo':
       fig2 = px.bar(df, x= 'tipo_de_generacion', y='mayo',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "mayo": "MAYO"
                 },
                title="GRAFICO")
        
    elif value == 'junio':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='junio',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "junio": "JUNIO"
                 },
                title="GRAFICO")

    elif value == 'julio':
       fig2 = px.bar(df, x= 'tipo_de_generacion', y='julio',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "julio": "JULIO"
                 },
                title="GRAFICO")

    elif value == 'agosto':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='agosto',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "agosto": "AGOSTO"
                 },
                title="GRAFICO")

    elif value == 'septiembre':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='septiembre',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "septiembre": "SEPTIEMBRE"
                 },
                title="GRAFICO")

    elif value == 'octubre':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='octubre',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "octubre": "OCTUBRE"
                 },
                title="GRAFICO")

    elif value == 'noviembre':
        fig2 = px.bar(df, x= 'tipo_de_generacion', y='noviembre',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "noviembre": "NOVIEMBRE"
                 },
                title="GRAFICO")

    else:
       fig2 = px.bar(df, x= 'tipo_de_generacion', y='diciembre',
                 labels={
                     "tipo_de_generacion": "TIPOS DE GENERACION",
                     "diciembre": "DICIEMBRE"
                 },
                title="GRAFICO")
    return fig2
    

if __name__ == '__main__':
    app.run_server(debug=True)