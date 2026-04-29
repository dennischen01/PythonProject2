#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import requests


class GitHubOAuth:
    CLIENT_ID: str = os.environ.get("GITHUB_CLIENT_ID", "")
    CLIENT_SECRET: str = os.environ.get("GITHUB_CLIENT_SECRET", "")
    AUTHORIZE_URL: str = "https://github.com/login/oauth/authorize"
    TOKEN_URL: str = "https://github.com/login/oauth/access_token"
    USER_API: str = "https://api.github.com/user"

    @classmethod
    def get_authorize_url(cls, redirect_uri: str) -> str:
        return (
            f"{cls.AUTHORIZE_URL}?client_id={cls.CLIENT_ID}"
            f"&redirect_uri={redirect_uri}&scope=user:email"
        )

    @classmethod
    def fetch_user_info(cls, code: str, redirect_uri: str) -> dict:
        resp = requests.post(
            cls.TOKEN_URL,
            json={"client_id": cls.CLIENT_ID, "client_secret": cls.CLIENT_SECRET,
                  "code": code, "redirect_uri": redirect_uri},
            headers={"Accept": "application/json"},
            timeout=10,
        )
        resp.raise_for_status()
        access_token = resp.json().get("access_token", "")

        user_resp = requests.get(
            cls.USER_API,
            headers={"Authorization": f"Bearer {access_token}", "Accept": "application/json"},
            timeout=10,
        )
        user_resp.raise_for_status()
        return user_resp.json()
