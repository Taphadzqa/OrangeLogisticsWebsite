from flask import Blueprint, current_app
from flask_httpauth import HTTPBasicAuth
import string
import random


webhook = Blueprint('webhook', __name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify(username, password):
    if username in current_app.config['AUTHENTICATION'] and password == current_app.config['AUTHENTICATION'].get(username):
        return username


@auth.login_required
def generateOTP(size=4, characters=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(characters) for _ in range(size))


# OTP generator
@webhook.route('/webhook/J2ldMcfuano42sNv1ABVY_g6vol9fQ', methods=['POST'])
def hook():
    return generateOTP()
