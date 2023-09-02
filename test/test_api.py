
from datetime import datetime, timezone
from dateutil import parser as date_parse

import pytest

from truthbrush.api import Api


@pytest.fixture(scope="module")
def api():
    return Api()


def as_datetime(date_str):
    return date_parse.parse(date_str).replace(tzinfo=timezone.utc)


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
    full_timeline = list(api.pull_statuses(username=username, replies=False, verbose=True))
    assert len(full_timeline) > 25 # more than one page

    latest = full_timeline[0]
    latest_at = as_datetime(latest["created_at"])
    earliest = full_timeline[-1]
    earliest_at = as_datetime(earliest["created_at"])
    assert earliest_at < latest_at

    # can use created_after param for filtering out posts:
    # (this test assumes no posts generated between the first pull and now)

    next_pull = list(api.pull_statuses(username=username, replies=False, created_after=latest_at, verbose=True))
    assert not any(next_pull)

    n_posts = 50
    recent = full_timeline[n_posts]
    recent_at = as_datetime(recent["created_at"])
    partial_pull = list(api.pull_statuses(username=username, replies=False, created_after=recent_at, verbose=True))
    assert len(partial_pull) == n_posts
    assert recent["id"] not in [post["id"] for post in partial_pull]

    # can use id_after param for filtering out posts:
    # (this test assumes no posts generated between the first pull and now)
    #latest_id = latest["id"]
    #next_pull = list(api.pull_statuses(username=username, replies=False, id_after=latest_id, verbose=True))
    #assert not any(next_pull)


    # contains status info
    assert list(latest.keys()) == ['id', 'created_at',
        'in_reply_to_id', 'quote_id', 'in_reply_to_account_id',
        'sensitive', 'spoiler_text', 'visibility', 'language', 'uri', 'url',
        'content', 'account', 'media_attachments', 'mentions', 'tags', 'card',
        'group', 'quote', 'in_reply_to', 'reblog', 'sponsored',
        'replies_count', 'reblogs_count', 'favourites_count', 'favourited', 'reblogged',
        'muted', 'pinned', 'bookmarked', 'poll', 'emojis', '_pulled'
    ]
