import os
from crypt import methods
from subprocess import check_call
from urllib.parse import urlparse

import uuid
from datetime import datetime

from flask import (Flask, current_app, Blueprint, g, redirect, render_template, url_for, request, flash)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from dvi.db import get_db
from dvi.auth import login_required
from dvi.utils import get_countries
import re


bp = Blueprint('user', __name__)

@bp.route('/<username>')
@login_required
def profile(username):
    domain = None
    user = get_user_profile(username)

    # Extract user's domain name
    if user['website_link']:
        parsed_url = urlparse(user['website_link'])
        domain = parsed_url.netloc

    return render_template('user/profile.html', user=user, domain=domain)


# Get all the user's profile by user-name
def get_user_profile(username):
    user = get_db().execute("SELECT id, pic_path, full_name, username, region, about_user, website_link, register, "
        "CASE STRFTIME('%m', register) "
        "WHEN '01' THEN 'January' "
        "WHEN '02' THEN 'February' "
        "WHEN '03' THEN 'March' "
        "WHEN '04' THEN 'April' "
        "WHEN '05' THEN 'May' "
        "WHEN '06' THEN 'June' "
        "WHEN '07' THEN 'July' "
        "WHEN '08' THEN 'August' "
        "WHEN '09' THEN 'September' "
        "WHEN '10' THEN 'October' "
        "WHEN '11' THEN 'November' "
        "WHEN '12' THEN 'December' "
        "END AS register_month, "
        "STRFTIME('%Y', register) AS register_year "
        "FROM user WHERE username = ?", (username,)).fetchone()

    if user is None:
        abort(404, f"username {username} doesn't exit.")

    return  user


@bp.route('/profile_update', methods=['GET', 'POST'])
@login_required
def profile_update():
    db = get_db()
    countries = get_countries()
    error = None

    if request.method == 'POST':
        image = request.files.get('pic_path')
        full_name = request.form['full_name']
        username = request.form['username']
        region = request.form['region']
        about_user = request.form['about_user']
        website_link = request.form['website_link']

        # Check if the username contains only allowed characters
        if not re.match(r'^[\w]+$', username): # Regex for letters, numbers, and underscores only.
            error = 'Username can only contain letters, numbers, and underscores.'
            flash(error, 'error')
            return redirect(request.url)

        if len(about_user) > 60:
            error = 'The "about" section cannot exceed 60 characters.'
            flash(error, 'error')
            return redirect(request.url)
        elif not full_name:
            error = 'Names field must not be empty.'
            flash(error, 'error')
            return redirect(request.url)


        # Initialize filename (image) variable
        new_filename = None

        # Validate image if it exists
        if image:
            filename = secure_filename(image.filename)
            file_ext = os.path.splitext(filename)[1].lower() # Extract file extension and  convert to lowercase.

            # Ensure the file has a valid extension
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                error = 'Invalid image format! Only .jpg, .jpeg & .png are allowed.'
                flash(error, "error")
                return  redirect(request.url)

            # Generate a unique filename if a file with the same name exists
            new_filename = os.path.splitext(filename)[0] + uuid.uuid4().hex + file_ext # Generate a unique ID using UUID

            # Save the image to the upload directory.
            image.save(os.path.join(current_app.config['UPLOAD_PATH'], new_filename))

        # Keep existing pic ( The default avatar) if no image is uploaded
        if not image:
            new_filename = g.user['pic_path']

        db.execute('UPDATE user SET pic_path = ?, full_name = ?, username = ?, region = ?, about_user = ?, website_link = ? WHERE id = ?', (new_filename, full_name, username, region, about_user, website_link, g.user['id'],))
        db.commit()

        # Success message
        success = 'Profile update successful.'
        flash(success, "success" )

        # Redirect to home page with updated infos
        return redirect(url_for('blog.index'))

    # If GET request, render the update form with existing user data
    return render_template('user/update.html', countries=countries)


# Allow user to remove profile picture.
@bp.route('/remove_profile_pic', methods=['GET', 'POST'])
@login_required
def remove_profile_pic():
    db = get_db()

    # get the current user's profile picture
    current_path = g.user['pic_path']

    # If the user has an existing profile picture, remove it.
    if current_path is not None:
        file_path = os.path.join(current_app.config['UPLOAD_PATH'], current_path)

        # Check if the file exists before trying to remove it
        if os.path.exists(file_path):
            os.remove(file_path)

            # Set the profile picture path in the database to None (the default avatar)
            db.execute('UPDATE user SET pic_path = ? WHERE id = ?', (None, g.user['id'],))
            db.commit()
            return redirect(url_for('user.profile', username=g.user['username']))

    return render_template('user/update.html')


