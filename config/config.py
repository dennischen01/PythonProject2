#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from config.default_config import DefaultConfig


class DevelopmentConfig(DefaultConfig):
    DEBUG: bool = True


class ProductionConfig(DefaultConfig):
    DEBUG: bool = False


class TestingConfig(DefaultConfig):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///:memory:"


_config_map = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
    "testing": TestingConfig,
}

Config = _config_map.get(os.environ.get("FLASK_ENV", "development"), DevelopmentConfig)
