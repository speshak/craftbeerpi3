from flask import Flask, render_template, redirect
from flask_socketio import SocketIO, emit

import pprint

from modules.core.db import get_db

import modules.steps
import modules.config
import modules.logs
import modules.sensors
import modules.actor
import modules.notification
import modules.fermenter
from modules.addon.endpoints import initPlugins
import modules.ui
import modules.system
import modules.buzzer
import modules.kettle
import modules.recipe_import
import modules.core.db_mirgrate
from app_config import cbpi, app


pp = pprint.PrettyPrinter(indent=6)


@app.route('/')
def index():
    return redirect('ui')


def init_db():
    """Build the database: This will create the database file using
    SQLAlchemy"""
    app.logger.info("INIT DB")
    with app.app_context():
        db = get_db()

        try:
            with app.open_resource('../config/schema.sql', mode='r') as f:
                db.cursor().executescript(f.read())

            db.commit()
        except Exception as e:
            app.logger.warn(e)


init_db()
initPlugins()
cbpi.run_init()

cbpi.run_background_processes()


app.logger.info("##########################################")
app.logger.info("### STARTUP COMPLETE")
app.logger.info("##########################################")
