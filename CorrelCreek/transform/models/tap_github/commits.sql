{{
  config(
    materialized='table'
  )
}}

WITH base AS (
    SELECT *
    FROM {{ source('tap_github', 'commits') }}
),
repos AS (
    SELECT *
    FROM {{ source('tap_github', 'repositories') }}
)
SELECT
    base.sha AS sha,
    base.repo_id AS repo_id,
    base.repo AS repo_name,
    base.commit_timestamp AS commit_timestamp,
    repos.language AS language
FROM base
JOIN repos ON repo_id = repos.id
ORDER BY base.commit_timestamp DESC