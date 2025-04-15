import dash
import dash_bootstrap_components  as dbc
from dash import dcc, Input, Output , html
import plotly.express as px
import pandas as pd



# Loading the data frame, check the dataset and clean the data : 


def load_data():
    df  = pd.read_csv(r'dash_learning\assets\healthcare_dataset.csv')
    print(df.head())



# Make the webapp for the dash application : 
app = dash.Dash(__name__ , external_stylesheets=[dbc.themes.BOOTSTRAP]) # This makes use the bootstrap theme for the dashb applicaiton the whole application is powered by flask. 

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
               dbc.Col(html.H1("Main Dashboard") , width=15 , className="text-center my-5")
        ])
    ]) , 

    # Another Section for the dashboard : '
    dbc.Row([
        dbc.Row([
            dbc.Col([
                dbc.Col(html.H1("This is another content") , width=10 )
            ])
        ])
    ])

    # We also can make the section for the :  

    , 

    dbc.Row([
        dbc.Col([
            dbc.Card([
            dbc.CardBody([
                html.H4(
                    "This is the h4 Title"

                ) , 

                dcc.Dropdown(
                    id ="dropdown"
                ) , 
                dcc.Graph(id="graph")

            ])
        ] )
        ] , width=8)
    ]) , 



dbc.Row([
    dbc.Col([
        dcc.Dropdown(
            id = 'gender' , options=[{"label" : "maale" , "value" : "data_set"}]
        )
    ])
])
   
    
] , fluid=True) # This starts as a class and takes and the list as the arguments it has the rows and inside the rows we have columns and top to bottom rows andleft to right columns just like a website 





## Overall in the dashboard we can have all the elements that we have in html we have to address it using the dash only.  

'''
Notes for the code : 


Callbacks : They are like a method to call certain actions when something happens :  




'''


@app.callback(
    Output('age-distribution' , 'figure'),
    Input('gender-filter' , 'value') # Gender filter is the id of the dropdown which we have made
)

def update_view(selected_gender):
    if selected_gender:
        filtered_df = # This is teh operation we can done of the pandas adn we can do anytbing in this fucniton for exaple iupdaing the graph and resetting the whole page 
    

    fig  = px.histogram (df , x ="name")
    return fig  # This we can use with the another calling for this function and the return graph would be loaded in the main page or else we can update the page from here only. 


## All the call back to be done before the main calling


'''
To use the css and scss we can indude the same in the code as well. 


'''





## Demo Code for the Graph and the Callbacks : 









if __name__ == '__main__':
    app.run()


