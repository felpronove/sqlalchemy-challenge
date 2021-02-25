#Import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

#set up the datebase
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
#relect the database into a new model
Base = automap_base()
#reflect the tables
Base.prepare(engine, reflect=True)
# Save references to each table
Measurements=Base.classes.measurement #reflect the hawaii measurements into a "Measurements" table
Stations=Base.classes.station #reflect the hawaii stations into a "Stations" table

#create an app
app = Flask(__name__)
