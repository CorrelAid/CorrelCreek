

with base as (
    select *
    from "postgres"."tap_github"."commits"
)
select distinct (commit -> 'author' -> 'name') as authors
from base