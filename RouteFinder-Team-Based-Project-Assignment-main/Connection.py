class Connection:
    def __init__(self, station1, station2, line):
        """Initialize a Connection object with station names and line name."""
        self.station1 = station1
        self.station2 = station2
        self.line = line
    def __eq__(self, other):
        """Check if two Connection objects are equal based on attributes."""
        return (isinstance(other, Connection) and
            self.station1 == other.station1 and
            self.station2 == other.station2 and
            self.line == other.line)
    def __str__(self):
        """Return a string representation of the Connection object."""
        return f"({self.station1},{self.station2},{self.line})"
    __repr__ = __str__
    def get_station1(self):
        return self.station1
    def get_station2(self):
        return self.station2
    def get_line(self):
        return self.line