# Correl Creek: Codebase

## Dev Setup

1. Spin up a postgres database with:

```
docker compose -f dev_database.yml up -d
```

2. Navigate to the dagster folder and install requirements for the dagster project with poetry:

```
poetry install
```

3. Install meltano



4. Create a GitHub Token, navigate to the meltano folder and create a .env file with the following contents:

```
TAP_GITHUB_AUTH_TOKEN='ghp_token'
```