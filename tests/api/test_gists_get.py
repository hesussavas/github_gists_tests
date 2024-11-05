import random
from playwright.sync_api import APIRequestContext
from tests.variables import TEST_USER_NAME


def test_get_users_gists_success(api_request_context: APIRequestContext, create_public_test_gist) -> None:
    result = api_request_context.get("/gists")

    assert result.ok

    gists = result.json()
    for gist in gists:
        assert "id" in gist, 'id is not in gist'
        assert "description" in gist,  'description is not in gist'
        assert "files" in gist,  'files is not in gist'
        assert "owner" in gist,  'owner is not in gist'
        assert "public" in gist,  'public is not in gist'


def test_get_public_gist_by_id_success(api_request_context: APIRequestContext, create_public_test_gist):
    test_gist_id, test_gist_description = create_public_test_gist

    result = api_request_context.get(f"/gists/{test_gist_id}")
    assert result.ok
    assert result.json()['description'] == test_gist_description


def test_get_private_gist_by_id_success(api_request_context: APIRequestContext, create_private_test_gist):
    test_gist_id, test_gist_description = create_private_test_gist

    result = api_request_context.get(f"/gists/{test_gist_id}")
    assert result.ok
    assert result.json()['description'] == test_gist_description


def test_get_nonexistent_user_gist_returns_404(api_request_context: APIRequestContext) -> None:
    nonexistent_id = f"{random.randint(1000, 10000)}-test"
    result = api_request_context.get(f"/gists/{nonexistent_id}")

    assert result.status == 404

def test_get_private_gist_by_id_for_unauthorized_user_success (api_request_context_unauthorized: APIRequestContext, create_private_test_gist):
    test_gist_id, test_gist_description = create_private_test_gist
    result = api_request_context_unauthorized.get(f"/gists/{test_gist_id}")

    assert result.ok
    assert result.json()['description'] == test_gist_description

def test_get_list_private_gists_users_by_unatorized_user_failed (api_request_context_unauthorized: APIRequestContext, create_private_test_gist):
    
    result = api_request_context_unauthorized.get(f"/users/{TEST_USER_NAME}/gists")
    assert result.ok
    assert result.json() == []