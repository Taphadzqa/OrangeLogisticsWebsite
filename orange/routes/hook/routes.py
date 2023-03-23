from flask import Blueprint
from flask_httpauth import HTTPBasicAuth
from orange import db
import string
import random


webhook = Blueprint('webhook', __name__)
auth = HTTPBasicAuth()


users = (db.all())[0]


@auth.verify_password
def verify(username, password):
    if username in users and password == users.get(username):
        return username


@auth.login_required
def generateOTP(size=6, characters=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(characters) for _ in range(size))


# OTP generator
@webhook.route('/webhook/J2ldMcfuano42sNv1ABVY_g6vol9fQ', methods=['POST'])
def hook():
    return generateOTP()
