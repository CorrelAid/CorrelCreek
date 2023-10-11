

WITH base AS (
    SELECT
        *,
        DATE_TRUNC('day', commit_timestamp) AS commit_date
    FROM tap_github.commits
)

SELECT
    base.commit_date AS "time",
    COUNT(*) AS commit_count,
    sum(COUNT(*)) over (order by base.commit_date desc) AS running_total
FROM base
GROUP BY
    base.commit_date
ORDER BY
    base.commit_date DESC