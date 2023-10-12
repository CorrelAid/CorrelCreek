#!/bin/bash

env_files=(".env" "meltano/.env" "dagster/.env")
secret_env_file="secret.env"

for env_file in "${env_files[@]}"; do
  echo "POSTGRES_PASSWORD=dagster" > "$env_file"
  echo "POSTGRES_DB=main" >> "$env_file"
  echo "POSTGRES_PORT=5432" >> "$env_file"
  echo "POSTGRES_HOST=localhost" >> "$env_file"
  echo "POSTGRES_SCHEMA=analytics" >> "$env_file"
  echo "POSTGRES_USER=dagster" >> "$env_file"
  if [[ "$env_file" == "meltano/.env" ]]; then
    source "$secret_env_file"
    echo "TAP_GITHUB_AUTH_TOKEN=$GITHUB_AUTH_TOKEN" >> "$env_file"
  fi
  if [[ "$env_file" == "dagster/.env" ]]; then
    source "$secret_env_file"
    echo "GITHUB_ACCESS_TOKEN=$GITHUB_OPEN_DATA_ACCESS_TOKEN" >> "$env_file"
    echo "GITHUB_REPO_NAME=CorrelAid/open-data-test" >> "$env_file"
  fi
done

docker compose -f dev_database.yml up -d