

WITH commits AS (
    SELECT *
    FROM "postgres"."tap_github"."commits"
)

SELECT
    COUNT(DISTINCT (commits.author ->> 'id')) AS total_active_users
FROM commits
WHERE (commits.author ->> 'type') = 'User'