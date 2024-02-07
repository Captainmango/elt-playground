{% macro generate_film_ratings() %}
    with films_with_ratings as (
        select
            film_id,
            title,
            price,
            release_date,
            rating,
            user_rating,
            {{ get_rating_category('user_rating') }} as rating_category
        from {{ ref('films') }}
    ),
    films_with_actors as (
        select
            f.film_id,
            f.title,
            STRING_AGG(a.actor_name, ',') as actors
        from {{ ref('films') }} f
        left join {{ ref('film_actors') }} fa using(film_id)
        left join {{ ref('actors') }} a using(actor_id)
        group by 1,2 
    )

    select
        fwr.*,
        fwa.actors
    from films_with_ratings fwr
    left join films_with_actors fwa using (film_id)
{% endmacro %}