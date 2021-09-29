# Travel_Bucket_List_Project

Build an app to track someone's travel adventures.

## Brief

The chosen project was to create an app to track someone's travel adventures. The brief, MVP and possible extensions are explained below:

### MVP

* The app should allow the user to track countries and cities they want to visit and those they have visited.
* The user should be able to create and edit countries
* Each country should have one or more cities to visit
* The user should be able to create and delete entries for cities
* The app should allow the user to mark destinations as visited or still to see

### Possible Extensions

* Have separate pages for destinations visited and those still to visit
* Add sights to the destination cities
* Search for destination by continent, city or country
* Any other ideas you might come up with

## Setup and running

Pre-requisites and usage

* Install Python3 and pip3

* Install postgreSQL

* Install Flask: pip3 install flask

* Install psycopg2: pip3 install psycopg2

* Clone/download the project and navigate to that directory in your terminal client

* Create the database:

`createdb travel_bucket_list`

* Create the database table structure:

`psql -d travel_bucket_list -f db/travel_bucket_list.sql`

* Import the seed console: python3 console.py

* Start Flask:

`flask run`

Navigate to the site in your browser at http://localhost:5000
