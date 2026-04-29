#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from config import Config
from internal.extension.database_extension import init_app as init_db
from internal.router.router import register_routes
from internal.exception import AppException


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(Config)

    init_db(app)
    register_routes(app)
    _register_error_handlers(app)

    return app


def _register_error_handlers(app: Flask):
    @app.errorhandler(AppException)
    def handle_app_exception(e: AppException):
        return e.to_dict(), e.http_status
