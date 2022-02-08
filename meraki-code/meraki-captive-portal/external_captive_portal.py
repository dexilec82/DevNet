#!/usr/bin/env python3
"""External Captive Portal Web Server."""

from flask import Flask, redirect, render_template, request
from waitress import serve


# Module Variables
base_grant_url = ""
user_continue_url = ""
success_url = ""

app = Flask(__name__, static_url_path='/5004/static')


# Flask micro-webservice URI endpoints
@app.route("/click", methods=["GET"])
def get_click():
    """Process GET requests to the /click URI; render the click.html page."""
    global base_grant_url
    global user_continue_url
    global success_url

    host = request.host_url
    base_grant_url = request.args.get('base_grant_url')
    user_continue_url = request.args.get('user_continue_url')
    node_mac = request.args.get('node_mac')
    client_ip = request.args.get('client_ip')
    client_mac = request.args.get('client_mac')
    success_url = host + "success"

    if base_grant_url != None and base_grant_url.startswith('http://'):
        base_grant_url = base_grant_url.replace("http://", "https://", 1) #hack to run excap in LL2.0

    return render_template(
        "click.html",
        client_ip=client_ip,
        client_mac=client_mac,
        node_mac=node_mac,
        user_continue_url=user_continue_url,
        success_url=success_url,
    )


@app.route("/login", methods=["POST"])
def get_login():
    """Process POST requests to the /login URI; redirect to grant URL."""
    redirect_url = base_grant_url+"?continue_url="+success_url
    return redirect(redirect_url, code=302)


@app.route("/success", methods=["GET"])
def get_success():
    """Process GET requests to the /success URI; render success.html."""
    global user_continue_url

    return render_template(
        "success.html",
        user_continue_url=user_continue_url,
    )


# If this script is the main script being executed, start the web server.
if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=5004, debug=True)
    serve(app, host='0.0.0.0', port=5004, url_scheme='https')

