#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
from internal.extension.database_extension import db
from internal.model.account import Account
from internal.exception import NotFoundException, ValidateException


class AccountService:
    @staticmethod
    def register(req) -> Account:
        if Account.query.filter_by(email=req.email).first():
            raise ValidateException("Email already exists")
        account = Account(
            name=req.name,
            email=req.email,
            password=hashlib.sha256(req.password.encode()).hexdigest(),
        )
        db.session.add(account)
        db.session.commit()
        return account

    @staticmethod
    def login(req) -> str:
        account = Account.query.filter_by(email=req.email).first()
        if not account:
            raise NotFoundException("Account not found")
        hashed = hashlib.sha256(req.password.encode()).hexdigest()
        if account.password != hashed:
            raise ValidateException("Invalid password")
        # TODO: generate JWT
        return "token-placeholder"
