#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from internal.handler.account_handler import AccountRegisterHandler, AccountLoginHandler


def register_routes(app):
    api = Blueprint("api", __name__, url_prefix="/api")

    api.add_url_rule("/account/register", view_func=AccountRegisterHandler.as_view("account_register"))
    api.add_url_rule("/account/login", view_func=AccountLoginHandler.as_view("account_login"))

    app.register_blueprint(api)
