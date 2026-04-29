#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pkg.oauth.github_oauth import GitHubOAuth


class OAuthService:
    @staticmethod
    def github_authorize_url(redirect_uri: str) -> str:
        return GitHubOAuth.get_authorize_url(redirect_uri)

    @staticmethod
    def github_callback(code: str, redirect_uri: str) -> dict:
        return GitHubOAuth.fetch_user_info(code, redirect_uri)
