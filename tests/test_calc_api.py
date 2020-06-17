import pytest
from werkzeug.exceptions import BadRequest


def test_single_param(client):
    response = client.get('/calc?codeine=7.0')
    assert response.json == 1.05


def test_multi_param(client):
    response = client.get('/calc?methadone=21.1&codeine=7.0')
    assert response.json == 168.8 + 1.05


def test_bogus_value(client):
    response = client.get('/calc?codeine=wrong')
    assert response.status_code == 400


def test_bogus_param(client):
    response = client.get('/calc?notreal=7.0')
    assert response.status_code == 400
