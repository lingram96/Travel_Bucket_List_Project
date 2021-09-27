class City:

    def __init__(self, name, country, sight, visited = False, id = None):
        self.name = name
        self.country = country
        self.sight = sight
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True