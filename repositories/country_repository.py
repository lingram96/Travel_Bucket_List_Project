from db.run_sql import run_sql

from models.country import Country
from models.city import City

import repositories.city_repository as city_repository


def save(country):
    sql = "INSERT INTO countries (name, capital, continent, visited, plan) VALUES (%s, %s, %s, %s, %s) RETURNING id"
    values = [country.name, country.capital, country.continent, country.visited, country.plan]
    results = run_sql(sql, values)
    country.id = results[0]['id']
    return country


def select_all():
    countries = []

    sql = "SELECT * FROM countries"
    results = run_sql(sql)

    for row in results:
        country = Country(row['name'], row['capital'], row['continent'], row['visited'], row['plan'], row['id'])
        countries.append(country)
    return countries


def select(id):
    country = None
    sql = "SELECT * FROM countries WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        country = Country(result['name'], result['capital'], result['continent'], result['visited'], result['plan'], result['id'])
    return country


def update(country):
    sql = "UPDATE countries SET (name, capital, continent, visited, plan) = (%s, %s, %s, %s, %s) WHERE id = %s"
    values = [country.name, country.capital, country.continent, country.visited, country.plan, country.id]
    run_sql (sql, values)


def delete_all():
    sql = "DELETE  FROM countries"
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM countries WHERE id = %s"
    values = [id]
    run_sql(sql, values)
