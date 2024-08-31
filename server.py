import os
import platform
import subprocess
import time

import psutil
from flask import Flask, jsonify, render_template, request
from setproctitle import getproctitle, setproctitle

from API.api import app
from API.get_info import (fetch_cpu_info, get_ip_address, get_uptime, gpu_info,
                          model_info, os_name)
from config import dictConfig


@app.route("/")
def index():
    return render_template("index.html")


@app.errorhandler(404)
def not_found(error):
    return render_template("error.html"), 404


if __name__ == "__main__":
    setproctitle("SDash")
    app.run(debug=True, host=get_ip_address())
