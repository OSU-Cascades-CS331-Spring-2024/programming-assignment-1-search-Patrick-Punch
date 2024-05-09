# Patrick Punch

class Map:
    def __init__(self):
        self.cities = {}
        self.city_location = {}

    def add_city(self, city):
        if city not in self.cities:
            self.cities[city] = []

    def add_edge(self, city_1, city_2, distance):
        if city_1 not in self.cities:
            self.add_city(city_1)
        if city_2 not in self.cities:
            self.add_city(city_2)
        if (city_2, distance) not in self.cities[city_1]:
            self.cities[city_1].append((city_2, distance))

    def get_neighbors(self, city):
        if city in self.cities:
            return self.cities[city]
        else:
            return []

    def create_map(self, map_file):
        # https://www.pythonforbeginners.com/files/reading-and-writing-files-in-python#htoc-reading-files-in-python
        with open(map_file) as file:
            for line in file:
                data = line.rstrip().split("-->")
                city = data[0].strip().split()
                edges = data[1].strip().split()
                city_name = city[0]
                latitude = " ".join(city[1:5]).strip()
                # print(latitude)
                longitude = " ".join(city[5:]).strip()
                # print(longitude)
                self.city_location[city_name] = (latitude, longitude)
                # print(city_name, " Location: ", self.city_location[city_name])
                self.add_city(city_name)
                for i in range(len(edges)):
                    if edges[i].startswith('va-'):
                        edges[i] = edges[i][3:]
                for i in range(0, len(edges), 2):
                    neighbor_name = edges[i]
                    distance = int(edges[i + 1])
                    self.add_edge(city_name, neighbor_name, distance)

    def display_map(self):
        for item in self.cities:
            print('\nCity: ', item, '\nLocation: ', self.city_location[item], '\nNeighbor(s): ', self.cities[item])