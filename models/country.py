class Country:

    def __init__(self, name, capital, continent, visited, id = None):
        self.name = name
        self.capital = capital
        self.continent = continent
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True