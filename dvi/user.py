import os.path
from crypt import methods
from urllib.parse import urlparse

from flask import (Flask, current_app, Blueprint, g, redirect, render_template, url_for, request, flash)
from werkzeug.exceptions import abort
from werkzeug.utils import secure_filename
from dvi.db import get_db
from dvi.auth import login_required


bp = Blueprint('user', __name__)

@bp.route('/profile')
@login_required
def profile():
    db = get_db()
    domain = None
    user = db.execute(
        "SELECT pic_path, full_name, username, about_user, region, website_link, register, "
        "CASE STRFTIME('%m', register)"
        "WHEN '01' THEN 'Jan' "
        "WHEN '02' THEN 'Feb' "
        "WHEN '03' THEN 'Mar' "
        "WHEN '04' THEN 'Apr' "
        "WHEN '05' THEN 'May' "
        "WHEN '06' THEN 'Jun' "
        "WHEN '07' THEN 'Jul' "
        "WHEN '08' THEN 'Aug' "
        "WHEN '09' THEN 'Sep' "
        "WHEN '10' THEN 'Oct' "
        "WHEN '11' THEN 'Nov' "
        "WHEN '12' THEN 'Dec' "
        "END AS register_month, "
        "STRFTIME('%Y', register) AS register_year "
        "FROM user WHERE id = ?", (g.user['id'],)).fetchone()

    # Extract user's domain name
    if user['website_link']:
        parsed_url = urlparse(user['website_link'])
        domain = parsed_url.netloc

    return render_template('user/profile.html', user=user, domain=domain)

@bp.route('/profile_update', methods=['GET', 'POST'])
@login_required
def profile_update():
    db = get_db()

    if request.method == 'POST':
        image = request.files.get('pic_path')
        full_name = request.form['full_name']
        about_user = request.form['about_user']
        website_link = request.form['website_link']

        # Initialize filename (image) variable
        filename = None

        # Validate image if it exists
        if image:
            filename = secure_filename(image.filename)
            file_ext = os.path.splitext(filename)[1].lower()

            # Ensure the file has a valid extension
            if file_ext not in current_app.config['UPLOAD_EXTENSIONS']:
                error = 'Invalid image format! Only .jpg, .jpeg & .png are allowed.'
                flash(error, "error")
                return  redirect(request.url)

            # Save the image
            image.save(os.path.join(current_app.config['UPLOAD_PATH'], filename))

        # Keep existing pic
        if not image:
            filename = g.user['pic_path']

        db.execute('UPDATE user SET pic_path = ?, full_name = ?, about_user = ?, website_link = ? WHERE id = ?', (filename, full_name, about_user, website_link, g.user['id'],))
        db.commit()

        # Success message
        success = 'Successfully updated profile.'
        flash(success, "success" )

        # Redirect to profile page with updated data
        return redirect(url_for('user.profile'))

    # If GET request, render the update form with existing user data
    return render_template('user/update.html')

@bp.route('/remove_profile_pic', methods=['GET', 'POST'])
@login_required
def remove_profile_pic():
    db = get_db()

    # get the current user's profile picture
    current_pic_path = g.user['pic_path']

    # If the user has an existing profile picture, remove it.
    if current_pic_path and current_pic_path != 'avatar.png': # because 'avatar.png' is the default picture
        file_path = os.path.join(current_app.config['UPLOAD_PATH'], current_pic_path)

        # Check if the file exists before trying to remove it
        if os.path.exists(file_path):
            os.remove(file_path)

    # Set the profile picture to none in the database
    db.execute('UPDATE user SET pic_path = NULL WHERE id = ?', (g.user['id'],))
    db.commit()
    return render_template('user/update.html')


