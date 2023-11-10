from Subway import Subway
from SubwayPrinter import SubwayPrinter


class SubwayLoader:
    def __init__(self):
        self.subway = Subway()
    def get_subway(self):
        return self.subway
    def load_from_file(self, filename):
        with open(filename, "r") as file:
            self.load_stations(file)
            line = file.readline().strip()
            while line:
                self.load_line(file, line)
                line = file.readline().strip()
    def load_stations(self, data):
        for line in data:
            station = line.strip()
            if not station:
                break
            self.subway.add_station(station)
    def load_line(self, data, line):
        station1 = data.readline().strip()
        station2 = data.readline().strip()
        while station2:
            self.subway.add_connection(station1, station2, line)
            station1 = station2
            station2 = data.readline().strip()
if __name__ == '__main__':
    loader = SubwayLoader()
    loader.load_from_file("ObjectvilleSubway.txt")
    subway = loader.get_subway()
    stations_to_test = ["DRY Drive", "Servlet Springs", "Boards 'R' Us"]
    print("Testing stations...", end=" ")
    if all(subway.has_station(station) for station in stations_to_test):
        print("PASSED!")
    else:
        print("FAILED!")
    connections_to_test = [
        ("DRY Drive", "PMP Place"),
        ("GoF Gardens", "JSP Junction"),
        ("LSP Lane", "Head First Labs"),
    ]
    print("Testing connections...", end=" ")
    if all(subway.has_connection(station1, station2) for station1, station2 in connections_to_test):
        print("PASSED!")
    else:
        print("FAILED!")
    print()
    print("-" * 70)
    p = SubwayPrinter()
    print("-" * 70)
