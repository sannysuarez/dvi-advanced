from flask import (Flask, Blueprint, g, redirect, render_template, url_for)
from werkzeug.exceptions import abort
from dvi.db import get_db
from dvi.auth import login_required


bp = Blueprint('user', __name__)

@bp.route('/profile')
@login_required
def profile():
    db = get_db()
    user = db.execute('SELECT pic_path, full_name, username, about_user, region, website_link FROM user WHERE id = ?', (g.user['id'],)).fetchone()
    return render_template('user/profile.html', user=user)

@bp.route('/profile_update')
@login_required
def profile_update():
    return render_template('user/update.html')

