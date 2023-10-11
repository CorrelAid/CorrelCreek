

WITH base AS (
    SELECT *
    FROM "postgres"."tap_github"."commits"
),
repos AS (
    SELECT *
    FROM "postgres"."tap_github"."repositories"
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