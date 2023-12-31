{{ config(
    materialized='table',
    alias='daily_stats'
) }}

WITH commits AS (
    SELECT
        *,
        DATE_TRUNC('day', commit_timestamp) AS commit_date
    FROM tap_github.commits
),

stargazers AS (
    SELECT DATE_TRUNC('day', starred_at) AS starred_date
    FROM SOURCE('tap_github', 'stargazers')
),

commit_counts AS (
    SELECT
        commits.commit_date,
        COUNT(*) AS commit_count,
        COUNT(DISTINCT commits.author ->> 'id') AS active_users_count
    FROM commits
    GROUP BY commits.commit_date
),

stargazer_counts AS (
    SELECT
        stargazers.starred_date,
        COUNT(*) AS stargazers_count
    FROM stargazers
    GROUP BY stargazers.starred_date
),

joined_counts AS (
    SELECT
        COALESCE(
            commit_counts.commit_date, stargazer_counts.starred_date
        ) AS "day",
        COALESCE(commit_counts.commit_count, 0) AS commit_count,
        COALESCE(commit_counts.active_users_count, 0) AS active_users_count,
        COALESCE(stargazer_counts.stargazers_count, 0) AS stargazers_count
    FROM commit_counts
    FULL OUTER JOIN stargazer_counts
        ON commit_counts.commit_date = stargazer_counts.starred_date
)

SELECT
    joined_counts.date,
    joined_counts.commit_count,
    joined_counts.stargazers_count,
    joined_counts.active_users_count,
    SUM(joined_counts.commit_count)
        OVER (ORDER BY joined_counts.date ASC)
    AS total_commits,
    SUM(joined_counts.stargazers_count)
        OVER (ORDER BY joined_counts.date ASC)
    AS total_starred
FROM joined_counts
ORDER BY joined_counts.date DESC
