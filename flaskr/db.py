import sqlite3

import click
from flask import current_app,g
from flask.cli import with_appcontext

def get_db():
    if 'db' not in g: # g is some special object that stures data that might be accessed by differnet functions
        g.db = sqlite3.connect(
                current_app.config['DATABASE'],
                detect_types=sqlite3.PARSE_DECLTYPES
                )
        g.db.row_factory = sqlite3.Row #makes the connection return rows that behave like dicts access by nde

        return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()
        עע
