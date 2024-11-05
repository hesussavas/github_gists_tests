from time import sleep
from typing import Generator

import pytest
from playwright.sync_api import Playwright, APIRequestContext

from variables import HEADERS, PRIVATE_BODY, PUBLIC_BODY, DESCRIPTION


@pytest.fixture(scope="session")
def api_request_context(
    playwright: Playwright,
) -> Generator[APIRequestContext, None, None]:
    request_context = playwright.request.new_context(
        base_url="https://api.github.com", extra_http_headers=HEADERS
    )
    yield request_context
    request_context.dispose()



@pytest.fixture()
def create_public_test_gist(api_request_context: APIRequestContext) -> Generator[None, None, None]:
    # Before test
    response = api_request_context.post("/gists", data=PUBLIC_BODY)
    assert response.ok
    gist_id = response.json()['id']
    yield gist_id, DESCRIPTION
    # After test
    response = api_request_context.delete(f"/gists/{gist_id}")
    assert response.ok


@pytest.fixture()
def create_private_test_gist(api_request_context: APIRequestContext) -> Generator[None, None, None]:
    # Before test
    
    response = api_request_context.post("/gists", data=PRIVATE_BODY)
    assert response.ok
    gist_id = response.json()['id']
    yield gist_id, DESCRIPTION
    # After test
    response = api_request_context.delete(f"/gists/{gist_id}")
    assert response.ok


@pytest.fixture()
def cleanup_gists(api_request_context: APIRequestContext) -> Generator[None, None, None]:
    gist_ids_to_delete = []
    yield gist_ids_to_delete
    
    # After the test
    for gist_id in gist_ids_to_delete: 
        response = api_request_context.delete(f"/gists/{gist_id}")
        assert response.ok
