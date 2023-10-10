{{
  config(
    materialized='table'
  )
}}

WITH commits AS (
    SELECT *
    FROM {{ source('tap_github', 'commits') }}
)

SELECT
    COUNT(DISTINCT (commits.author ->> 'id')) AS total_active_users
FROM commits
WHERE (commits.author ->> 'type') = 'User'
