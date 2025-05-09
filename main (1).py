
from flask import Flask, request, jsonify
from zekabot_görevler import run_code
from zekabot_scraper import scrape_data
from zekabot_giriş import login_to_site
from zekabot_guard import decrypt, encrypt
from zekabot_raporu import get_daily_report
from zekabot_messenger import send_whatsapp_message

app = Flask(__name__)

@app.route("/")
def home():
    return "Zekabot v0.7 çalışıyor!"

@app.route("/run", methods=["POST"])
def run():
    code = request.json.get("code")
    result = run_code(code)
    return jsonify({"result": result})

@app.route("/scrape", methods=["POST"])
def scrape():
    url = request.json.get("url")
    selector = request.json.get("selector")
    result = scrape_data(url, selector)
    return jsonify({"result": result})

@app.route("/login", methods=["POST"])
def login():
    url = request.json.get("url")
    payload = request.json.get("payload")
    result = login_to_site(url, payload)
    return jsonify({"result": result})

@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    number = request.json.get("number")
    message = request.json.get("message")
    result = send_whatsapp_message(number, message)
    return jsonify({"status": result})

@app.route("/encrypt", methods=["POST"])
def enc():
    text = request.json.get("text")
    result = encrypt(text)
    return jsonify({"encrypted": result})

@app.route("/decrypt", methods=["POST"])
def dec():
    text = request.json.get("text")
    result = decrypt(text)
    return jsonify({"decrypted": result})

@app.route("/report", methods=["GET"])
def report():
    return jsonify(get_daily_report())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
