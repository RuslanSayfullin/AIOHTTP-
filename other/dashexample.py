import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-box', type='text'),
    html.Button('Submit', id='submit-button'),
    html.Div(id='output-container')
])

@app.callback(
        Output('output-container', 'children'),
        [Input('submit-button', 'n_clicks')],
        [dash.dependencies.State('input-box', 'value')]
)
def update_output(n_clics, value):
    if n_clics:
        return f'You entered: {value}'
    return

if __name__ == "__main__":
    app.run_server(debug=True)
