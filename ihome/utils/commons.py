# coding:utf-8
from functools import wraps
from werkzeug.routing import BaseConverter
from flask import session, jsonify, g
from ihome.utils.response_code import RET


class RegexConverter(BaseConverter):
    def __init__(self, url_map, regex):
        super(RegexConverter, self).__init__(url_map)
        self.regex = regex


def login_required(view_func):
    """检验用户的登录状态"""

    @wraps(view_func)
    def wrapper(*args, **kwargs):
        user_id = session.get("user_id")
        if user_id is not None:
            # 表示用户登录
            g.user_id = user_id
            return view_func(*args, **kwargs)
        else:
            # 用户未登录
            resp = {
                "errno": RET.SESSIONERR,
                "errmsg": "用户未登录"
            }
            return jsonify(resp)

    return wrapper
