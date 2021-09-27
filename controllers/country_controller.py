from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import country_repository, city_repository
from models.country import Country

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries = countries)

@countries_blueprint.route("/countries/<id>")
def show(id):
    countries = country_repository.select(id)
    visited = country_repository.visited(countries)
    return render_template("countries/show.html", countries = countries, visited = visited)

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("countries/new.html", countries = countries, cities = cities)