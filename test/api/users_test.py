





def test_lookup_user(client):
    user = client.lookup(user_handle="realDonaldTrump")
    assert isinstance(user, dict)

    assert isinstance(user["id"], str)

    expected_attributes = [

    ]
    assert sorted(list(user.keys())) == expected_attributes
