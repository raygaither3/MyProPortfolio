from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    return render_template('main/landing.html')

@main_bp.route('/projects')
def projects():
    return render_template('main/projects.html')

@main_bp.route('/services')
def services():
    return render_template('main/services.html')

@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html')