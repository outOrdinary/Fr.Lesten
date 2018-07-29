# coding:utf-8

from flask import Blueprint

api = Blueprint("api_1_0", __name__)

import index, venify_code, passport, profile, houses
