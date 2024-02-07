{% macro get_rating_category(column_name) %}
    case
        {% for score, category in [(4.5, 'excellent'), (4.0, 'good'), (3.0, 'average')] %}
        when {{ column_name }} >= {{ score }} then '{{ category }}'
        {% endfor %}
        else 'poor'
    end
{% endmacro %}