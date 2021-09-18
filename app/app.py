import os

from flask import Flask, render_template, request, redirect
from flask_pymongo.wrappers import MongoClient
from . import settings, controllers, models
from .extensions import db
from datetime import datetime
from flask_pymongo import PyMongo
import os
from bson.objectid import ObjectId

project_dir = os.path.dirname(os.path.abspath(__file__))

def create_app(config_object=settings):
    # create and configure the app (mlh template)
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)

    # -- Initialization section --
    app = Flask(__name__)
    
    app.config['MONGO_DBNAME'] = os.getenv('DBNAME')
    dbname = app.config['MONGO_DBNAME']
    app.config['USER'] = os.getenv('DBUSER')
    user = app.config['USER']
    app.config['MONGO_PWD'] = os.getenv('DBPWD')   
    pwd = app.config['MONGO_PWD']

    app.config['MONGO_URI'] = "mongodb+srv://"+str(user)+":"+str(pwd)+"@cluster0.seola.mongodb.net/"+str(dbname)+"?retryWrites=true&w=majority"
    mongo = PyMongo(app)
    print("hello")
    print(mongo.db.sea) ###
    
    client = MongoClient(app.config['MONGO_URI'])
    db = client['knowledge_sea']
    collection = db['sea']

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_routes(app, mongo.db.sea)
    return app

def register_extensions(app):
    """Register Flask extensions."""
    # db.init_app(app)

    # with app.app_context():
    #     db.create_all()
    return None

def register_blueprints(app):
    """Register Flask blueprints."""
    # app.register_blueprint(controllers.home.blueprint)
    # app.register_blueprint(controllers.auth.blueprint)
    # app.register_blueprint(controllers.tutorial.blueprint)
    return None

def register_errorhandlers(app):
    """Register error handlers."""
    @app.errorhandler(401)
    def internal_error(error):
        return render_template('401.html'), 401

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    @app.errorhandler(500)
    def internal_error(error):
        return render_template('500.html'), 500

    return None

def register_routes(app, collection):
    @app.route('/')
    def index():
        return render_template('welcome/index.html')

    @app.route('/drop')
    def drop():
        return render_template('welcome/drop.html')

    @app.route('/dive')
    def begin_dive():
        if (collection.count() > 0):
            id = collection.aggregate([{ "$sample": { "size": 1 } }])
            print(id)
            return redirect('/dive/' + id)
        else:
          return redirect('/empty')

    @app.route('/dive/<string:id>')
    def view_drop(id):
        return render_template('welcome/drop.html') # FIXME: add params

    @app.route('/stream')
    def stream():
        return render_template('welcome/stream.html')
