from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import country_repository, city_repository
from models.country import Country
import pdb

countries_blueprint = Blueprint("countries", __name__)

@countries_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    # pdb.set_trace()
    return render_template("countries/index.html", countries = countries, title = "Countries -")

@countries_blueprint.route("/countries/new", methods=['GET'])
def new_country():
    countries = country_repository.select_all()
    cities = city_repository.select_all()
    return render_template("countries/new.html", countries = countries, cities = cities, title = "New Country -")

@countries_blueprint.route("/countries",  methods=['POST'])
def create_country():
    name = request.form['country_name']
    capital = request.form['capital_name']
    continent = request.form['continent']
    visited = request.form['visited']
    plan = request.form ['plan']
    country = Country(name, capital, continent, visited, plan)
    country_repository.save(country)
    return redirect('/countries')

@countries_blueprint.route("/countries/<id>", methods=["GET"])
def show_country(id):
    country = country_repository.select(id)
    return render_template('countries/show.html', country = country)


@countries_blueprint.route("/countries/<id>/edit", methods=["GET"])
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country = country)


@countries_blueprint.route("/countries/<id>", methods=["POST"])
def update_country(id):
    name = request.form['name']
    capital = request.form['capital']
    continent = request.form['continent']
    visited = request.form['visited']
    plan = request.form['plan']
    country = Country(name, capital, continent, visited, plan, id)
    country_repository.update(country)
    return redirect('/countries')
   

@countries_blueprint.route("/countries/<id>/delete", methods=["POST"])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')

@countries_blueprint.route("/countries/visited")
def countries_visited():
    countries = country_repository.select_all()
    return render_template("countries/visited.html", countries = countries, title = "Visited -")

@countries_blueprint.route("/countries/tovisit")
def countries_tovisit():
    countries = country_repository.select_all()
    return render_template("countries/tovisit.html", countries = countries, title = "To Visit -")

