import os


GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")


HEADERS = {
    # Those headers are per GitHub guidelines.
    "Accept": "application/vnd.github.v3+json",
    "X-GitHub-Api-Version": "2022-11-28",

    "Authorization": f"token {GITHUB_API_TOKEN}"
}


DESCRIPTION = "test description"
PUBLIC = True
PRIVATE = False
FILES = {
    "README.md":
    {
        "content": "Hello World"
    }
}

PUBLIC_BODY = {
    "description": DESCRIPTION,
    "public": PUBLIC,
    "files": FILES
}

PRIVATE_BODY = {
    "description": DESCRIPTION,
    "public": PRIVATE,
    "files": FILES
}
