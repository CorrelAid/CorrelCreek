# Correl Creek: Codebase

## Dev Setup

1. Create a file called secret.env with the following contents

```
GITHUB_AUTH_TOKEN='gh_token'
GITHUB_OPEN_DATA_ACCESS_TOKEN='token'

```

2. Run the setup script to create .env files and spin up Postgres with Docker:

```
bash dev_setup.sh
```

3. Navigate to the Dagster folder and install requirements for the Dagster project with poetry:

```
poetry install
poetry run pre-commit install
```

4. Navigate to the meltano folder and install requirements:
```
poetry install
poetry run meltano install
poetry run pre-commit install
```

### Quality Insurance
### Meltano
Sqlfluff is used for sql linitin. Lint the sql files by running:
```
poetry run meltano invoke sqlfluff:lint
``` 
There is a VS Code extension for sqlfluff
## Dagster
Black is used for formatting, Ruff is used for linting.

