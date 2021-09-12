from __init__ import create_app

def test_shorten(client):
    response = client.get('/home')
    assert b'Shorten' in response