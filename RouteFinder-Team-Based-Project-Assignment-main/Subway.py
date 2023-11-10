from Connection import Connection


class Subway:
    def __init__(self):
        """Initialize a Subway object with stations and connections."""
        self.stations = []
        self.connections = {}

    def add_station(self, name):
        """Add a station to the subway network if it doesn't already exist."""
        if name not in self.stations:
            self.stations.append(name)

    def add_connection(self, name1, name2, line):
        """
        Add a connection between two stations with a specified line.

        If the stations don't exist, they are added to the network.
        """
        self.add_station(name1)
        self.add_station(name2)
        if name1 not in self.connections:
            self.connections[name1] = {}
        if name2 not in self.connections:
            self.connections[name2] = {}
        self.connections[name1][name2] = line
        self.connections[name2][name1] = line

    def get_directions(self, name1, name2):
        """
        Find directions between two stations.

        Returns a list of Connection objects representing the path.
        """
        if name1 not in self.stations or name2 not in self.stations:
            return []

        visited = set()
        queue = [(name1, [])]

        while queue:
            current_station, path = queue.pop(0)
            visited.add(current_station)
            for neighbor, line in self.connections.get(current_station, {}).items():
                connection = Connection(current_station, neighbor, line)
                if neighbor == name2:
                    return path + [connection]
                if neighbor not in visited:
                    queue.append((neighbor, path + [connection]))
        return []

    def has_station(self, name):
        """Check if a station exists in the subway network."""
        return name in self.stations

    def has_connection(self, name1, name2):
        """Check if there is a connection between two stations."""
        return name1 in self.connections and name2 in self.connections[name1]

    def get_all_stations(self):
        return self.stations
