from flask import render_template
from app import app

# Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    message = "Welcome to News Highlight"
    return render_template('index.html', message = message)

# @app.route('/articles/<articles_id>')
# def articles(articles_id):
#     '''
#     View articles page function that returns artcicles details and its data
#     '''
#     return render_template('articles.html')
