# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

blueprint = Blueprint('welcome', __name__)

@blueprint.route('/')
def index():
    return render_template('welcome/index.html')

@blueprint.route('/example')
def example():
    return render_template('welcome/example.html')