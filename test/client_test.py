
from truthbrush.api import Api, TRUTHSOCIAL_USERNAME, TRUTHSOCIAL_PASSWORD

def test_client_initialization(client):

    assert isinstance(client, Api)

    # attributes:
    assert client._Api__username == TRUTHSOCIAL_USERNAME
    assert client._Api__password == TRUTHSOCIAL_PASSWORD

    # not yet authorized:
    assert client.auth_id == None


def test_client_login(client):

    breakpoint()
