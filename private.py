from flask import Blueprint, jsonify, request
from flask_jwt import jwt_required, current_identity
from model import Articles, db, userSchema, articleSchema
from datetime import datetime

private = Blueprint('private', __name__, 'static', 'template')

@private.route('/get_post_id/<post_id>/', methods=['GET'])
@jwt_required()
def get_post_id(post_id):
    article = Articles.query.filter_by(id=post_id).first_or_404()
    if article:
        return jsonify(articleSchema.dump(article))
    return jsonify('Article not found.')

@private.route('/get_post/<title>/', methods=['GET'])
@jwt_required()
def get_post(title):
    article = Articles.query.filter_by(link=title).first_or_404()
    if article:
        return jsonify(articleSchema.dump(article))
    return jsonify('Article not found.')

@private.route('/add_post/', methods=['POST'])
@jwt_required()
def addPost():
    requestedArticle = request.get_json()
    article = Articles(title=requestedArticle['title'], author=requestedArticle['author'], link=requestedArticle['link'], content=requestedArticle['content'], summary=requestedArticle['summary'], date_posted=datetime.now(), date_updated=datetime.now(), tags=requestedArticle['tags'], categories=requestedArticle['categories'])
    db.session.add(article)
    db.session.commit()
    return jsonify(articleSchema.dump(article))

@private.route('/delete_post_id/<post_id>/', methods=['DELETE'])
@jwt_required()
def deletePostID(post_id):
    article = Articles.query.filter_by(id=post_id).first_or_404()
    if article:
        db.session.delete(article)
        db.session.commit()
        return jsonify('Article has been deleted successfully.')
    return jsonify('Article not found.')

@private.route('/delete_post_by_id/<title>/', methods=['DELETE'])
@jwt_required()
def deletePost(title):
    article = Articles.query.filter_by(link=title).first_or_404()
    if article:
        db.session.delete(article)
        db.session.commit()
        return jsonify('Article has been deleted successfully.')
    return jsonify('Article not found.')

@private.route('/edit_post_id/<post_id>/', methods=['PUT'])
@jwt_required()
def editPostID(post_id):
    requestedArticle = request.get_json()
    article = Articles.query.filter_by(id=post_id).first_or_404()
    if article:
        article.title = requestedArticle['title']
        article.content = requestedArticle['content']
        article.summary = requestedArticle['summary']
        article.date_updated = datetime.now()
        article.tags = requestedArticle['tags']
        article.categories = requestedArticle['categories']
        db.session.commit()
        return jsonify(articleSchema.dump(article))
    return jsonify('Article not found.')

@private.route('/edit_post/<title>/', methods=['PUT'])
@jwt_required()
def editPost(title):
    requestedArticle = request.get_json()
    article = Articles.query.filter_by(link=title).first_or_404()
    if article:
        article.title = requestedArticle['title']
        article.content = requestedArticle['content']
        article.summary = requestedArticle['summary']
        article.date_updated = datetime.now()
        article.tags = requestedArticle['tags']
        article.categories = requestedArticle['categories']
        db.session.commit()
        return jsonify(articleSchema.dump(article))
    return jsonify('Article not found.')
