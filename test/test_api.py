
from datetime import datetime, timezone
from dateutil import parser as date_parse

import pytest

from truthbrush import Api

@pytest.fixture(scope="module")
def api():
    return Api()


def test_lookup(api):
    user = api.lookup(user_handle="realDonaldTrump")
    assert list(user.keys()) == [
        'id', 'username', 'acct', 'display_name',
        'locked', 'bot', 'discoverable', 'group', 'created_at',
        'note', 'url', 'avatar', 'avatar_static', 'header', 'header_static',
        'followers_count', 'following_count', 'statuses_count', 'last_status_at',
        'verified', 'location', 'website',
        'accepting_messages', 'chats_onboarded', 'feeds_onboarded',
        'show_nonmember_group_statuses', 'pleroma', 'emojis', 'fields'
    ]


def test_pull_statuses(api):
    username = "truthsocial"

    # it fetches a timeline of the user's posts:
    full_timeline = list(api.pull_statuses(username=username, replies=False))
    latest = full_timeline[-1]
    assert any(full_timeline)
    print(len(full_timeline))
    assert list(latest.keys()) == ['id', 'created_at',
        'in_reply_to_id', 'quote_id', 'in_reply_to_account_id',
        'sensitive', 'spoiler_text', 'visibility', 'language', 'uri', 'url',
        'content', 'account', 'media_attachments', 'mentions', 'tags', 'card',
        'group', 'quote', 'in_reply_to', 'reblog', 'sponsored',
        'replies_count', 'reblogs_count', 'favourites_count', 'favourited', 'reblogged',
        'muted', 'pinned', 'bookmarked', 'poll', 'emojis', '_pulled'
    ]

    # can use created_after param for filtering out posts:
    # (this test assumes no posts generated between the previous pull and now)
    latest_at = latest["created_at"]
    latest_at = date_parse.parse(latest_at).replace(tzinfo=timezone.utc)
    next_pull = list(api.pull_statuses(username=username, replies=False, created_after=latest_at))
    print(len(next_pull))
    assert not any(next_pull)
