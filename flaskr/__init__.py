import os

from flask import Flask

def create_app(test_config=None): # creates the Flask instance
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True) # name gives the current python module name
    app.config.from_mapping(# some default configuration that the app will use
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlit')
            )
    if test_config is None:
        #load the instance config, if it exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        #load test config if passed in
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return "Hello, World"

    return app
