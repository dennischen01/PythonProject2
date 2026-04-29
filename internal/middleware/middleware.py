#!/usr/bin/env python
# -*- coding: utf-8 -*-
from functools import wraps
from flask import request, g
from internal.exception import UnauthorizedException


def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization", "").removeprefix("Bearer ").strip()
        if not token:
            raise UnauthorizedException()
        # TODO: validate JWT and set g.current_user
        return f(*args, **kwargs)
    return decorated
