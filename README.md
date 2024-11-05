
# GitHub Gists API Automated Tests

This project contains automated tests for the GitHub Gists API, implemented in Python using the Playwright framework. It is designed as a test assignment, focusing on basic functionality for creating & retrieving gists.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Test Cases](#test-cases)
- [Project Structure](#project-structure)
- [Notes](#notes)

## Project Overview

This project tests key endpoints of the GitHub Gists API:
1. **Create a gist**
2. **Retrieve a gist**


## Technologies Used

- **Python**: Programming language for test implementation.
- **Playwright**: Framework for end-to-end testing, used here for API testing with Python.
- **GitHub API**: API being tested.

## Setup and Installation

To run this project, ensure that you have Python and Playwright installed on your machine.

1. Clone the repository:
   ```bash
   git clone https://github.com/IuliaSavk/github-gists-api-tests.git
   cd github-gists-api-tests
   ```

2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
   ```

3. Install Playwright browsers:
   ```bash
   playwright install
   ```

4. Set up your GitHub API token:
   - Create a `.env` file in the root directory and add your GitHub token:
     ```
     GITHUB_API_TOKEN=your_personal_access_token
     ```

   This token is required to authenticate API requests.

## Usage

Run the tests with the following command:

```bash
python3 -m pytest tests/
```

## Test Cases

The following test cases are included in this project:

1. **Create Gist**: Verifies that a new gist can be created successfully.
2. **Retrieve Gist**: Ensures that an existing gist can be retrieved by ID.

## Project Structure

The project has a straightforward structure:

```plaintext
├── tests/                      # Contains API tests and configuration files
│   ├── api/                    # Directory for API test files
│   │   ├── test_gists_create.py   # Tests for creating gists
│   │   ├── test_gists_get.py      # Tests for retrieving gists
│   ├── __init__.py             # Initializes tests module, loads environment variables
│   ├── conftest.py             # Configuration file for fixtures
│   ├── variables.py            # File for storing test variables
├── .env                        # Environment file for storing sensitive info (tokens, secrets)
├── README.md                   # Project documentation
└── requirements.txt            # Project dependenciesroject dependencies
```

## Notes

- **Environment Variables**: Ensure your GitHub API token is in the `.env` file to avoid authentication issues.