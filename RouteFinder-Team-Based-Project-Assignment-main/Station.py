class Station:
    def __init__(self, name):
        """Initialize a Station object with a lowercase station name."""
        self.name = name.lower()
    def __eq__(self, other):
        """Check if two Station objects are equal based on their names."""
        return self.name == other.name
    def __hash__(self):
        """Return a hash value for the Station based on its name."""
        return hash(self.name)
    def __str__(self):
        """Return the lowercase name of the Station as a string."""
        return self.name
    def get_name(self):
        """Get the lowercase name of the Station."""
        return self.name
