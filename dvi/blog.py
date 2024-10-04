from flask import (Blueprint, flash, g, redirect, render_template, request, url_for)
from werkzeug.exceptions import abort
from dvi.auth import login_required
from dvi.db import get_db

bp = Blueprint('blog', __name__)

@bp.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, body, created, author_id, full_name, username FROM post p JOIN user u ON p.author_id = '
        'u.id ORDER BY created DESC'
    ).fetchall()
    return render_template('blog/index.html', page_name='index', posts=posts)

@bp.route('/create', methods=['GET', 'POST'])
@login_required
def create():
    if request.method == 'POST':
        body = request.form['body']

        db = get_db()
        db.execute(
            'INSERT INTO post ( body, author_id) VALUES (?, ?)', (body, g.user['id'])
        )
        db.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/create.html')

# fetch a post by id and check if the author matches the logged in user.
'''
The check_author argument is defined so that the function can be used to get a post without checking the author. 
This would be useful cuz i wrote a view to show an individual post on a page, where the user doesn’t matter because 
they’re not modifying the post.
'''
def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.id, title, body, created, author_id, username FROM post p JOIN user u ON p.author_id = '
        'u.id WHERE p.id = ?', (id,).fetchone()
    )

    if post is None:
        abort(404, f"Post id {id} doesn't exist.")

    if check_author and post['author_id'] != g.user['id']:
        abort(403)

    return post

@bp.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        body = request.form['body']
        db = get_db()
        db.execute(
            'UPDATE post SET body = ? WHERE id = ?', (body, id)
        )
        db.commit()
        return redirect(url_for('blog.index'))
    return render_template('blog/update.html', post=post)

@bp.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM post WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))