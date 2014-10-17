#!/usr/bin/env python
# encoding: utf-8
# vim: set et sw=4 ts=4 sts=4 fenc=utf-8
# Author: YuanLin

import os
import time
import datetime
import logging
import hashlib
from flask import request, g
from flask_mail import Mail

from ._flask import Flask
from .models import db

def create_app(config=None):
    app = Flask(
            __name__,
            template_folder="templates",
            )


