with films_with_ratings as (
    select
        film_id,
        title,
        price,
        release_date,
        rating,
        user_rating,
        case
            when user_rating >= 4.5 then 'excellent'
            when user_rating >= 4.0 then 'good'
            when user_rating >= 3.0 then 'average'
            else 'poor'
        end as rating_category
    from {{ ref('films') }}
),
films_with_actors as (
    select
        f.film_id,
        f.title,
        STRING_AGG(a.actor_name, ',') as actors
    from {{ ref('films') }} f
    left join {{ ref('film_actors') }} fa on f.film_id = fa.film_id
    left join {{ ref('actors') }} a on fa.actor_id = a.actor_id
    group by 1,2 
)

select
    fwr.*,
    fwa.actors
from films_with_ratings fwr
left join films_with_actors fwa using (film_id)