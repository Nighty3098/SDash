import logging
import os
from logging.config import dictConfig

from flask import Flask

app = Flask(__name__)

app_version = "0.3.6"

logging.basicConfig(
    encoding="utf-8",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(threadName)s : %(message)s"
)
