import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc

# Dados fictícios
df_bar = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D'],
    'Values': [10, 20, 30, 40]
})

df_line = pd.DataFrame({
    'Date': pd.date_range(start='1/1/2021', periods=10, freq='M'),
    'Values': [10, 15, 13, 17, 19, 23, 18, 22, 25, 27]
})

df_scatter = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D'],
    'X': [1, 2, 2, 3, 3, 4, 4, 5],
    'Y': [5, 7, 6, 8, 9, 11, 10, 12]
})

# Inicializa a aplicação Dash com o tema escuro do Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# Layout do dashboard
app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                html.H1("Meu Dashboard Expandido", className="text-center text-light mb-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                html.Div("Exemplo de dashboard com Dash.", className="text-center text-light mb-4"),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(
                    id='bar-graph',
                    figure=px.bar(df_bar, x='Category', y='Values', title='Gráfico de Barras')
                ),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(
                    id='line-graph',
                    figure=px.line(df_line, x='Date', y='Values', title='Gráfico de Linhas')
                ),
                width=12
            )
        ),
        dbc.Row(
            dbc.Col(
                dcc.Graph(
                    id='scatter-graph',
                    figure=px.scatter(df_scatter, x='X', y='Y', color='Category', title='Gráfico de Dispersão')
                ),
                width=12
            )
        )
    ],
    fluid=True
)

# Executa a aplicação
if __name__ == '__main__':
    app.run_server(debug=True)
