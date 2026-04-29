#!/usr/bin/env python
# -*- coding: utf-8 -*-
from http import HTTPStatus


class AppException(Exception):
    http_status: int = HTTPStatus.INTERNAL_SERVER_ERROR
    code: str = "INTERNAL_ERROR"
    message: str = "Internal server error"

    def __init__(self, message: str = None, code: str = None):
        self.message = message or self.__class__.message
        self.code = code or self.__class__.code
        super().__init__(self.message)

    def to_dict(self) -> dict:
        return {"code": self.code, "message": self.message}


class NotFoundException(AppException):
    http_status = HTTPStatus.NOT_FOUND
    code = "NOT_FOUND"
    message = "Resource not found"


class UnauthorizedException(AppException):
    http_status = HTTPStatus.UNAUTHORIZED
    code = "UNAUTHORIZED"
    message = "Authentication required"


class ForbiddenException(AppException):
    http_status = HTTPStatus.FORBIDDEN
    code = "FORBIDDEN"
    message = "Permission denied"


class ValidateException(AppException):
    http_status = HTTPStatus.UNPROCESSABLE_ENTITY
    code = "VALIDATE_ERROR"
    message = "Validation failed"
