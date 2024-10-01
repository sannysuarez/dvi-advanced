import functools
from crypt import methods

from flask import (Blueprint, flash, g, redirect, render_template, request, session, url_for )
from werkzeug.security import check_password_hash, generate_password_hash
from dvi.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        full_name = request.form['full_name']
        gender = request.form['gender']
        dob = request.form['dob']
        region = request.form['region']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not full_name:
            error = 'Names are required!'
        elif not gender:
            error = 'Gender required!'
        elif not doc:
            error = 'D.O.B required!'
        elif not region:
            error = 'Region required!'
        elif not email:
            error = 'Email required!'
        elif not username:
            error = 'Username required!'
        elif not password:
            error = 'Password required!'

        if error is None:
            try:
                db.execute("INSERT INTO user (full_name, gender, dob, region, email, username, password) VALUES(?, ?, ?, ?, ?, ?, ?)", (full_name, gender, dob, region, email, username, generate_password_hash(password)),)
                db.commit()
            except db.IntegrityError:
                error = f"{email} is already registered."
            else:
                success = 'Registered successfully.'
                flash(success)
                return redirect(url_for("auth.login"))
        flash(error)
    return render_template('auth/register.html')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        identifier = request.form['identifier'] # Can be Username or Email
        password = request.form['password']

        db = get_db()
        error = None
        # Check if the identifier is an Email or Username
        user = db.execute('SELECT * FROM user WHERE username = ? OR email = ?', (identifier, identifier)).fetchone()

        if user is None:
            error = 'Incorrect Username or Email.'
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password!'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))
        flash(error)
    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute('SELECT * FROM user WHERE id = ?', (user_id,)).fetchone


# remove the user ID from the session. then load_logged_in_user won't load a user on subsequent requests.
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view













