from flask import Flask, request, jsonify
from zekacore.zekabot_tasks import run_code
from zekacore.zekabot_scraper import scrape_data
from zekacore.zekabot_login import login_to_site
from zekacore.zekabot_messenger import send_whatsapp_message, receive_whatsapp_message
from zekacore.zekabot_guard import validate_and_log
from zekacore.zekabot_report import get_daily_report

app = Flask(__name__)

@app.route("/")
def home():
    return "Zekabot aktif ve çalışıyor."

@app.route("/run", methods=["POST"])
def run():
    code = request.json.get("code")
    result = run_code(code)
    validate_and_log("Kod çalıştırıldı", code)
    return jsonify(result=result)

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.json.get("url")
    selector = request.json.get("selector")
    data = scrape_data(url, selector)
    return jsonify(data=data)

@app.route("/login", methods=["POST"])
def login():
    url = request.json.get("url")
    payload = request.json.get("payload")
    result = login_to_site(url, payload)
    return jsonify(result=result)

@app.route("/whatsapp/send", methods=["POST"])
def send_message():
    number = request.json.get("number")
    message = request.json.get("message")
    result = send_whatsapp_message(number, message)
    return jsonify(result=result)

@app.route("/whatsapp/receive", methods=["GET"])
def receive_message():
    messages = receive_whatsapp_message()
    return jsonify(messages=messages)

@app.route("/report", methods=["GET"])
def report():
    return jsonify(get_daily_report())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)