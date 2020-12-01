import dash_html_components as html
import dash_core_components as dcc

def create_header():

    header = html.Div(className='banner-container',
                      children=[
                          html.Img(
                              className='banner-image',
                              src='assets/logo.png'
                          )
                      ]

    )

    return header