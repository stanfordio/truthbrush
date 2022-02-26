from email.generator import Generator
from typing import Any, Iterator, List
from loguru import logger
import requests

BASE_URL = "https://truthsocial.com/api/v1"
USER_AGENT = "TruthSocial/45 CFNetwork/1329 Darwin/21.3.0"

class Api:
    def __init__(self, auth_id):
        self.auth_id = auth_id

    def _get(self, url: str, params: dict=None) -> Any:
        return requests.get(BASE_URL + url, params=params, headers={
            "authorization": "Bearer " + self.auth_id,
            "user-agent": USER_AGENT,
        }).json()

    def _get_paginated(self, url: str, params: dict=None) -> Any:
        next_link = url
        while next_link is not None:
            resp = requests.get(BASE_URL + url, params=params, headers={
                "authorization": "Bearer " + self.auth_id,
                "user-agent": USER_AGENT,
            })

            next_link = resp.links.get('next', {}).get('url')
            yield resp.json()

    def lookup(self, user_handle: str=None) -> dict:
        """Lookup a user's information."""
        
        assert user_handle is not None
        return self._get("/accounts/lookup", params=dict(acct=user_handle))

    def user_followers(self, user_handle: str=None, user_id: str=None, maximum: int=1000) -> Iterator[dict]:
        assert user_handle is not None or user_id is not None
        user_id = user_id if user_id is not None else self.lookup(user_handle)["id"]

        n_output = 0
        for followers_batch in self._get_paginated(f"/accounts/{user_id}/followers"):
            for f in followers_batch:
                yield f
                n_output += 1
                if maximum is not None and n_output >= maximum:
                    return