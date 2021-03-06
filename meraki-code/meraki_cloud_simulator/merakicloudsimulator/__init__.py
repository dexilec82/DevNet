from flask import Flask, request, render_template, redirect, jsonify, abort

merakicloudsimulator = Flask(__name__, static_url_path='/5001/static')

from merakicloudsimulator import meraki_settings
from merakicloudsimulator import alert_settings
from merakicloudsimulator import sample_alert_messages
from merakicloudsimulator import excapsimulator
from merakicloudsimulator import locationscanningsimulator
from merakicloudsimulator import webhooksimulator
