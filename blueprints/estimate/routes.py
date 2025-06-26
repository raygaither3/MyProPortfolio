from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
import os
from werkzeug.utils import secure_filename

estimate_bp = Blueprint('estimate', __name__)

@estimate_bp.route('/estimate', methods=['GET', 'POST'])
def request_estimate():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        project_type = request.form.get('project_type')
        budget = request.form.get('budget')
        deadline = request.form.get('deadline')
        description = request.form.get('description')
        file = request.files.get('file')

        if not all([name, email, project_type, budget, deadline, description]):
            flash('Please fill out all required fields.', 'danger')
            return redirect(url_for('estimate.request_estimate'))

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(current_app.config['UPLOAD_FOLDER'], filename))

        # TODO: Send email or log estimate
        flash('Estimate request sent! I’ll be in touch soon.', 'success')
        return redirect(url_for('estimate.request_estimate'))

    return render_template('estimate/estimate.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in current_app.config['ALLOWED_EXTENSIONS']