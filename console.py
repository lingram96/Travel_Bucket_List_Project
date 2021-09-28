from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Italy", "Rome", "Europe", True, "Visit the Vatican and Coliseum.")
country_repository.save(country_1)

country_2 = Country("Canada", "Toronto", "North America", True, "Check out the CN Tower and Lake Ontario.")
country_repository.save(country_2)

country_3 = Country("Portugal", "Lisbon", "Europe", True, "Ride the cable cars.")
country_repository.save(country_3)

country_4 = Country("Spain", "Madrid", "Europe", True, "Go see a Real Madrid game.")
country_repository.save(country_4)

country_5 = Country("Sweden", "Stockholm", "Europe", True, "Check out the Vasa Museum and spend all my money.")
country_repository.save(country_5)

country_6 = Country("Ireland", "Dublin", "Europe", True, "Have a pint in Temple Bar.")
country_repository.save(country_6)

country_7 = Country("Morocco", "Rabat", "Africa", False, "Smoke some Moroccan Hash.")
country_repository.save(country_7)

country_8 = Country("Japan", "Tokyo", "Asia", False, "Eat ramen and fight a sumo wrestler.")
country_repository.save(country_8)

country_9 = Country("Slovenia", "Ljubljana", "Europe", True, "See the castle.")
country_repository.save(country_9)

city_1 = City("Rome", country_1, "Vatican", True)
city_repository.save(city_1)

city_2 = City("Venice", country_1, "Canals", False)
city_repository.save(city_2)

city_3 = City("Toronto", country_2, "Casa Loma", True)
city_repository.save(city_3)

city_4 = City("Lisbon", country_3, "Belém Tower", False)
city_repository.save(city_4)

city_5 = City("Seville", country_4, "Royal Palace", False)
city_repository.save(city_5)

print(country_repository.select_all()[0].id)
print(city_repository.select_all()[0].id)