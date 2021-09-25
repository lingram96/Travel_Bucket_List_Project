class City:

    def __init__(self, name, info, sight, visited, id = None):
        self.name = name
        self.info = info
        self.sight = sight
        self.visited = visited
        self.id = id

    def mark_visited(self):
        self.visited = True