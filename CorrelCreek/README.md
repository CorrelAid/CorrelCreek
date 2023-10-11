# Correl Creek: Codebase

## Dev Setup

1. Create a file called secret.env with the following contents

```
TAP_GITHUB_AUTH_TOKEN='gh_token'

```

2. Run the setup script to create .env files and spin up Postgres with Docker:

```
bash dev_setup.sh
```

3. Navigate to the Dagster folder and install requirements for the Dagster project with poetry:

```
poetry install
```

4. Install meltano



