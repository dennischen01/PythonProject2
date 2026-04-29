#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import request
from flask.views import MethodView
from internal.schema.account_schema import AccountRegisterReq, AccountLoginReq
from internal.service import AccountService


class AccountRegisterHandler(MethodView):
    def post(self):
        req = AccountRegisterReq(**request.get_json(silent=True) or {})
        account = AccountService.register(req)
        return {"code": "success", "data": {"id": str(account.id)}}, 201


class AccountLoginHandler(MethodView):
    def post(self):
        req = AccountLoginReq(**request.get_json(silent=True) or {})
        token = AccountService.login(req)
        return {"code": "success", "data": {"token": token}}, 200
