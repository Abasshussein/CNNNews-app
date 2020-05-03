from flask import render_template,request,redirect,url_for
from . import main 
from ..request import get_sources, get_articles



@main.route('/')
def index():
   
    general_list = get_sources('FR', 'general')
    business_list = get_sources('FR', 'business')
    technology_list = get_sources('FR', 'technology')
    sports_list = get_sources('FR', 'sports')
    health_list = get_sources('FR', 'health')
    science_list = get_sources('FR', 'science')
    entertainment_list = get_sources('us', 'entertainment')
    test_args = 'News'
    return render_template('index.html',general=general_list,business=business_list,technology=technology_list,sports=sports_list,health=health_list,science=science_list,entertainment=entertainment_list)


@main.route('/news/<id>')
def news(id):
    """
    View articles page that returns the news article from a highlight
    """
    news_args = get_articles(id)
    highlight_args = 'Route Working!!'
    # name = f'{results_list}'
    return render_template('news.html',highlight_param=highlight_args,news=news_args)


