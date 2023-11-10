class SubwayPrinter:
    def print_directions(self, route):
        previous_line = None
        for index, connection in enumerate(route):
            station1 = connection[0]
            station2 = connection[1]
            current_line = connection[2]

            if index == 0:
                print(f"Start out at {station1}.")
            elif current_line == previous_line:
                print(f"Continue past {station1}...")
            else:
                print(
                    f"When you get to {station1}, get off the {previous_line}.")
                print(
                    f"Switch over to the {current_line}, heading towards {station2}.")
            previous_line = current_line
        print(f"Get off at {station2} and enjoy yourself!")
