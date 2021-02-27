#Import dependencies
from flask import Flask, jsonify
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import numpy as np

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

#CREATE ALL FLASK ROUTES
#Create route outlining all routes
@app.route("/")
def welcome():
    """Home Page"""
    """List all routes that are available."""
    return(
        f"Mahalo! Welcome to the Hawaiin Weather API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#Create route for the precipitation levels
@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a dictionary using date as the key and prcp as the value."""
    """Return the JSON representation of your dictionary."""
    session=Session(engine)

    last_date=session.query(func.max(Measurements.date)).first() 
    twelve_months=dt.date(2017, 8, 23)-dt.timedelta(days=365)

    climate_results=session.query(Measurements.date, Measurements.prcp).\
    filter(Measurements.date >= twelve_months).all()

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset"""
    session=Session(engine)

    results=session.query(Stations.station, Stations.name).all()

    session.close()

    all_stations=[]
    for station, name in results:
        station_dict = {}
        station_dict["station"]= station
        station_dict["name"]= name
        all_stations.append(station_dict)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Query the dates and temperature observations of the most active station for the last year of data"""
    """Return a JSON list of temperature observations (TOBS) for the previous year."""

    session=Session(engine)

    results=session.query(Stations.)

@app.route("/api/v1.0/<start>")
def start():
    """Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range."""
    """When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""
    session=Session(engine)

    results=session.query(Measurements.station, func.min(Measurements.tobs), func.max(Measurements.tobs), func.avg(Measurements.tobs)).\
    group_by(Measurements.station).all()