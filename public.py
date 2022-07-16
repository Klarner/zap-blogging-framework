from flask import Blueprint, render_template, url_for
from flask_jwt import jwt_required, current_identity
from model import Articles, articleSchema
from forms import SearchForm
from babel import dates

public = Blueprint("public", __name__, "static", "templates")

@public.route('/')
@public.route('/home/')
def index():
    return render_template('index.html')

@public.route('/about/')
def about():
    return render_template('about.html')

@public.route('/articles/')
def articles():
    posts = Articles.query.all()
    posts = Articles.query.order_by(Articles.date_posted.desc()).all()
    datePosted = []
    for post in posts:
        datePosted.append(dates.format_datetime(post.date_posted, "EEEE, d MMMM y 'at' HH:mm"))
    return render_template('articles.html', posts=posts, date_posted=datePosted)

@public.route('/article/<title>/')
def article(title):
    article = Articles.query.filter_by(link=title).first_or_404()
    datePosted = dates.format_datetime(article.date_posted, "EEEE, d MMMM y 'at' HH:mm")
    dateUpdated = dates.format_datetime(article.date_updated, "EEEE, d MMMM y 'at' HH:mm")
    return render_template('article.html', article=articleSchema.dump(article), date_posted=datePosted, date_updated=dateUpdated)

@public.context_processor
def base():
    form = SearchForm()
    return dict(form=form)

@public.route('/search/', methods=['POST'])
def search():
    form = SearchForm()
    posts = Articles.query
    if form.validate_on_submit():
        searched = form.searched.data
        posts = posts.filter(Articles.content.like('%' + searched + '%'))
        posts = posts.order_by(Articles.title).all()
        datePosted = []#dates.format_datetime(article.date_posted, "EEEE, d MMMM y 'at' HH:mm")
        for post in posts:
            datePosted.append(dates.format_datetime(post.date_posted, "EEEE, d MMMM y 'at' HH:mm"))
        return render_template('search.html', form=form, searched=searched, posts=posts, date_posted=datePosted)
