#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@Time   : 2026/4/30 05:00
@Author : chenxican01@gmail.com
@File   : app.py
"""
from internal.server import create_app

app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
