import pytest
from playwright.sync_api import APIRequestContext


@pytest.mark.parametrize("public", [True, False])
def test_create_gist_sucsess(api_request_context: APIRequestContext, cleanup_gists: list, public) -> None:
    description = "bla-bla"
    body = {
        "description": description,
        "public": public,
        "files":
        {
            "README.md":
                {
                    "content": "Hello World"
                }
        }
    }
    result = api_request_context.post("/gists", data=body)

    assert result.status == 201
    result_body = result.json()

    # to clean up this gist in the fixture after test is finished
    cleanup_gists.append(result_body['id'])

    assert result_body['description'] == description
    assert result_body['public'] == public
    assert "README.md" in result_body['files']
    assert "Hello World" in result_body['files']['README.md']['content']


def test_create_gist_without_files_failed(api_request_context: APIRequestContext) -> None:
    description = "test description"
    public = False
    body = {
        "description": description,
        "public": public
    }
    result = api_request_context.post("/gists", data=body)
    assert result.status == 422
