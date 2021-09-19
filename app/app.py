import os
import random

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

    register_extensions(app)
    register_blueprints(app)
    register_errorhandlers(app)
    register_routes(app, mongo.db.sea, mongo.db.connections)
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

def register_routes(app, sea, connections):
    @app.route('/')
    def index():
        return render_template('welcome/index.html')

    @app.route('/drop')
    def drop():
        return render_template('welcome/drop.html')

    @app.route('/dive')
    def begin_dive():
        if (sea.count_documents({}) > 0):
            aggregation = sea.aggregate([{ "$sample": { "size": 1 } }])
            for item in list(aggregation):
              return redirect('/dive/' + str(item['_id']))
        else:
          return redirect('/empty')

    @app.route('/dive/<string:id>')
    def view_drop(id):
        # print(id)
        object = sea.find_one({"_id": ObjectId(id)})
        # return render_template('welcome/drop.html') # FIXME: add params
        return object['content']

    @app.route('/empty')
    def desert():
        return render_template('welcome/empty.html')

    @app.route('/half_empty')
    def glass_half():
        return render_template('welcome/half_empty.html')

    @app.route('/swish')
    def stream():
        # drop1 = random.choice(["Brush your teeth", "Look both ways", "Read books"])
        # drop2 = random.choice(["Read Jane Eyre", "Live a healthy lifestyle"])
        if (sea.count_documents({}) == 0):
            return redirect('/empty')
        if (sea.count_documents({}) == 1):
            return redirect('/half_empty')
        # 2 or more elements
        aggregation = sea.aggregate([{ "$sample": { "size": 2 }}, {"$project": {"relations": 0}} ])
        if (not aggregation):
            return redirect('/empty')
        ag_as_list = list(aggregation)
        print("hello")
        print(ag_as_list)
        drop1 = ag_as_list[0]
        drop2 = ag_as_list[1]
        return render_template('welcome/swish.html', drop1=drop1, drop2=drop2)

    @app.route('/swish', methods=['POST'])
    def swish_swish():
        relevance = int(request.form['number'])
        print(relevance)
        should_switch = request.form['shouldSwitch']
        order = 1
        if (should_switch):
          order = 0
        drop1id = request.form['drop1id']
        print(drop1id)
        drop2id = request.form['drop2id']
        print(drop2id)
        result1 = connections.update({"o1": ObjectId(drop1id), "o2": ObjectId(drop2id)}, {"$inc": {"denominator": 1, "relevanceSum": relevance, "orderSum": order}}, upsert=True)
        result2 = connections.update({"o1": ObjectId(drop2id), "o2": ObjectId(drop1id)}, {"$inc": {"denominator": 1, "relevanceSum": relevance, "orderSum": 1 - order}}, upsert=True)
        
        print(result1)
        print(result2)
        return redirect('/swish')

        # new_drop = {'content': content, 'relations': []}
        # result = sea.insert_one(new_drop)
        # if (result.acknowledged):
        #   return {"id": str(result.inserted_id)}
        # return {"submission unsuccessful": "there was no result"}

    @app.route('/test')
    def test_empty():
        return {'hello': 'hi'}
    
    @app.route('/add_drop')
    def drop_form():
      return render_template('welcome/drop.html')

    @app.route('/add_drop', methods=['POST'])
    def add_drop():
        content = request.form['text']
        new_drop = {'content': content, 'relations': []}
        result = sea.insert_one(new_drop)
        if (result.acknowledged):
          return {"id": str(result.inserted_id)}
        return {"submission unsuccessful": "there was no result"}
