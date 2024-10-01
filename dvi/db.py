import sqlite3
import click
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect( current_app.config['DATABASE'], detect_types=sqlite3.PARSE_DECTYPES)
        g.db.row_factory = sqlite3.Row # tells the connection to return rows that behave like dicts. This allows accessing the columns by name.
        return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()