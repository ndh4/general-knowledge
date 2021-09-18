# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('welcome', __name__)

@blueprint.route('/')
def index():
    return render_template('welcome/index.html')

@blueprint.route('/drop')
def drop():
    return render_template('welcome/drop.html')

@blueprint.route('/sea')
def sea():
    return render_template('welcome/sea.html')

@blueprint.route('/stream')
def stream():
    return render_template('welcome/stream.html')