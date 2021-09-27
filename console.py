from models.country import Country
from models.city import City

import repositories.country_repository as country_repository
import repositories.city_repository as city_repository

city_repository.delete_all()
country_repository.delete_all()

country_1 = Country("Italy", "Rome", "Europe", False)
country_repository.save(country_1)

country_2 = Country("Canada", "Niagra Falls", "North America", True)
country_repository.save(country_2)

city_1 = City("Rome", country_1, "Vatican", False)
city_repository.save(city_1)

city_2 = City("Venice", country_1, "Canals", False)
city_repository.save(city_2)

city_3 = City("Ottawa", country_2, "Parliament", True)
city_repository.save(city_3)


print(country_repository.select_all()[0].id)
print(city_repository.select_all()[0].id)