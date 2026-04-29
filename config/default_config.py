#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os


class DefaultConfig:
    # Flask
    DEBUG: bool = False
    SECRET_KEY: str = os.environ.get("SECRET_KEY", "change-me-in-production")

    # Database
    SQLALCHEMY_DATABASE_URI: str = os.environ.get(
        "DATABASE_URL", "postgresql://user:password@localhost:5432/llmops"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False

    # Redis
    REDIS_URL: str = os.environ.get("REDIS_URL", "redis://localhost:6379/0")

    # JWT
    JWT_SECRET_KEY: str = os.environ.get("JWT_SECRET_KEY", "jwt-secret-change-me")
    JWT_ACCESS_TOKEN_EXPIRES: int = 3600  # seconds
