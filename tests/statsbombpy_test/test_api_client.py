from unittest import mock

import pytest
import requests as req

from statsbombpy import api_client

CREDS = {"user": "u", "passwd": "p"}


def _resp(status, body=None):
    r = mock.Mock(status_code=status)
    if status >= 400:
        r.raise_for_status.side_effect = req.HTTPError(str(status), response=r)
    r.json.return_value = body
    return r


@pytest.mark.parametrize("status", [500, 502, 504])
def test_get_resource_raises_on_server_error(status):
    with mock.patch.object(api_client.session, "get", return_value=_resp(status)):
        with pytest.raises(req.HTTPError) as exc:
            api_client.get_resource("http://x/y", CREDS)
    assert exc.value.response.status_code == status


def test_get_resource_client_error_returns_empty(capsys):
    with mock.patch.object(api_client.session, "get", return_value=_resp(404)):
        assert api_client.get_resource("http://x/y", CREDS) == []


def test_get_resource_ok():
    with mock.patch.object(api_client.session, "get", return_value=_resp(200, [1])):
        assert api_client.get_resource("http://x/y", CREDS) == [1]


def test_endpoint_versions_falls_back_on_server_error():
    with mock.patch.object(api_client.session, "get", return_value=_resp(503)):
        assert api_client._fetch_endpoint_versions(CREDS) is None
