
  
    

  create  table "postgres"."analytics"."authors__dbt_tmp"
  
  
    as
  
  (
    

with base as (
    select *
    from "postgres"."tap_github"."commits"
)
select distinct (commit -> 'author' -> 'name') as authors
from base
  );
  