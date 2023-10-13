#!/bin/bash

env_files=(".env" "meltano/.env" "dagster/.env")
secret_env_file="secret.env"

export POSTGRES_PASSWORD="dagster"
export POSTGRES_DB="main"
export POSTGRES_PORT="5432"
export POSTGRES_HOST="localhost"
export POSTGRES_SCHEMA="analytics"
export POSTGRES_USER="dagster"

for env_file in "${env_files[@]}"; do

  if [[ "$env_file" == "meltano/.env" ]]; then
    source "$secret_env_file"
    echo "TAP_GITHUB_AUTH_TOKEN=$GITHUB_AUTH_TOKEN" > "$env_file"
    echo "DBT_POSTGRES_PASSWORD=$POSTGRES_PASSWORD" >> "$env_file"
    echo "DBT_POSTGRES_DBNAME=$POSTGRES_DB" >> "$env_file"
    echo "DBT_POSTGRES_PORT=$POSTGRES_PORT" >> "$env_file"
    echo "DBT_POSTGRES_HOST=$POSTGRES_HOST" >> "$env_file"
    echo "DBT_POSTGRES_SCHEMA=$POSTGRES_SCHEMA" >> "$env_file"
    echo "DBT_POSTGRES_USER=$POSTGRES_USER" >> "$env_file"
  else 
    echo "POSTGRES_PASSWORD=$POSTGRES_PASSWORD" > "$env_file"
    echo "POSTGRES_DB=$POSTGRES_DB" >> "$env_file"
    echo "POSTGRES_PORT=$POSTGRES_PORT" >> "$env_file"
    echo "POSTGRES_HOST=$POSTGRES_HOST" >> "$env_file"
    echo "POSTGRES_SCHEMA=$POSTGRES_SCHEMA" >> "$env_file"
    echo "POSTGRES_USER=$POSTGRES_USER" >> "$env_file"
  fi

  if [[ "$env_file" == "dagster/.env" ]]; then
    echo "GITHUB_ACCESS_TOKEN=$GITHUB_OPEN_DATA_ACCESS_TOKEN" > "$env_file"
    echo "GITHUB_REPO_NAME=CorrelAid/open-data-test" >> "$env_file"
  fi
done

docker compose -f dev_database.yml up -d