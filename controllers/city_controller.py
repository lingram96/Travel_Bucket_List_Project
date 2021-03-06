from flask import Flask, render_template, request, redirect
from flask import Blueprint
from repositories import city_repository, country_repository
from models.city import City
import pdb

cities_blueprint = Blueprint("cities", __name__)

@cities_blueprint.route("/cities")
def cities():
    cities = city_repository.select_all()
    # pdb.set_trace()
    return render_template("cities/index.html", cities = cities, title = "Cities -")


@cities_blueprint.route("/cities/new", methods=['GET'])
def new_city():
    cities = city_repository.select_all()
    countries = country_repository.select_all()
    return render_template("cities/new.html", cities = cities, countries = countries, title = "New City -")


@cities_blueprint.route("/cities",  methods=['POST'])
def create_city():
    name = request.form['name']
    country_id = request.form['country_id']
    sight = request.form['sight']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    city = City(name, country, sight, visited)
    city_repository.save(city)
    return redirect('/cities')


@cities_blueprint.route("/cities/<id>", methods=["GET"])
def show_city(id):
    city = city_repository.select(id)
    return render_template('cities/show.html', city = city)


@cities_blueprint.route("/cities/<id>/edit", methods=["GET"])
def edit_city(id):
    city = city_repository.select(id)
    return render_template('cities/edit.html', city = city)


@cities_blueprint.route("/cities/<id>", methods=["POST"])
def update_city(id):
    found_city = city_repository.select(id)
    country = found_city.country
    name = request.form['name']
    sight = request.form['sight']
    visited = request.form['visited']
    city = City(name, country, sight, visited, id)
    city_repository.update(city)
    return redirect('/cities')
   

@cities_blueprint.route("/cities/<id>/delete", methods=["POST"])
def delete_city(id):
    city_repository.delete(id)
    return redirect('/cities')

@cities_blueprint.route("/cities/visited")
def cities_visited():
    cities = city_repository.select_all()
    return render_template("cities/visited.html", cities = cities, title = "Visited -")

@cities_blueprint.route("/cities/tovisit")
def cities_tovisit():
    cities = city_repository.select_all()
    return render_template("cities/tovisit.html", cities = cities, title = "To Visit -")

@cities_blueprint.route("/cities/sights")
def city_sights():
    cities = city_repository.select_all()
    return render_template("cities/sights.html", cities = cities, title = "Sights -")
