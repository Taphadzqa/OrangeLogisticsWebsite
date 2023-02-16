from flask import render_template, Blueprint
import datetime


main = Blueprint('main', __name__)


@main.route('/')
def home():
    return render_template('main/home.html', title='Welcome')


@main.route('/about')
def about():
    return render_template('main/about.html', title='About us')


@main.route('/contact')
def contact():
    return render_template('main/contact.html', title='Contact us')


@main.route('/services')
def services():
    return render_template('main/services.html', title='Services')


@main.route('/management')
def management():
    return render_template('main/management.html', title='Management')


@main.route('/petroleum')
def petroleum():
    return render_template('main/petroleum.html', title='Petroleum')

