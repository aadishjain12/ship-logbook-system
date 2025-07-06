from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from config import Config
from nlp_processor import process_voice_log
from iot_simulator import fetch_real_time_data
from report_generator import generate_report
from extensions import db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

from database import LogEntry

@app.route("/")
def index():
    logs = LogEntry.query.order_by(LogEntry.timestamp.desc()).limit(10).all()
    return render_template("index.html", logs=logs)

@app.route("/log", methods=["POST"])
def add_log():
    data = request.get_json()
    nlp_data = process_voice_log(data.get("voice_log", ""))
    real_data = fetch_real_time_data()

    log = LogEntry(
        timestamp=real_data['timestamp'],
        ship_id=data.get("ship_id", "SHIP-001"),
        latitude=real_data['lat'],
        longitude=real_data['lon'],
        speed=nlp_data.get("speed"),
        weather=real_data['weather'],
        voice_log=data.get("voice_log")
    )
    db.session.add(log)
    db.session.commit()
    return jsonify({"status": "success", "data": log.serialize()})

@app.route("/logs", methods=["GET"])
def get_logs():
    logs = LogEntry.query.all()
    return jsonify([log.serialize() for log in logs])

@app.route("/report", methods=["GET"])
def report():
    logs = LogEntry.query.all()
    html, chart_data, map_data = generate_report(logs)
    return render_template("report.html", html=html, chart_data=chart_data, map_data=map_data)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
