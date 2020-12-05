from dash.dependencies import Input, Output, State


def register_callbacks(app):

    # category1
    @app.callback(
        Output('category1', 'children'),
        [Input('demo-dropdown', 'value')])
    def output_category1(category1):
        return category1

    # category2
    @app.callback(
        Output('category2', 'children'),
        [Input('demo-checklist', 'value')])
    def output_category1(category2):
        return category2

