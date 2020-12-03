from dash.dependencies import Input, Output, State


def register_callbacks(app):

    # category1
    @app.callback(
        Output('category1', 'children'),
        [Input('categorySelector1', 'value')])
    def output_category1(category1):
        return category1

