#!/usr/bin/env python
# -*- coding: utf-8 -*-
from dataclasses import dataclass


@dataclass
class AccountRegisterReq:
    name: str = ""
    email: str = ""
    password: str = ""


@dataclass
class AccountLoginReq:
    email: str = ""
    password: str = ""
