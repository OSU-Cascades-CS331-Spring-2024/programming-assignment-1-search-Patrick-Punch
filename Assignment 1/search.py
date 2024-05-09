# Patrick Punch
import math

class Search():

    def __init__(self, map_file):
        self.map = map_file
        self.path_cost = 0
        self.frontier_size = 0
        self.total_expanded = 0
        self.total_visited = 0

    def bfs(self, start, goal):
        visited = []
        frontier = [[start]]
        while frontier:
            path = frontier.pop(0)
            node = path[-1]
            if node == goal:
                for node in path:
                    neighbor = self.map.cities[node][0]
                    distance = neighbor[1]
                    self.path_cost += distance
                return "Path: " + " -> ".join(path), self.path_cost, self.total_expanded, self.total_visited, self.frontier_size
            if node not in visited:
                visited.append(node)
                self.total_visited += 1
                for neighbor, _ in self.map.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    self.total_expanded += 1
                    frontier.append(new_path)
            self.frontier_size = len(frontier)
        print('no path found (╯°□°）╯︵ ┻━┻	')
        return None

    def dls(self, start, goal, depth_limit):
        for i in range(depth_limit + 1):
            result = self.dls_helper(start, goal)
            if result is not None:
                return result
        return None

    def dls_helper(self, start, goal):
        visited = []
        path = []
        frontier = [(start, path)]
        while frontier:
            node, path = frontier.pop()
            if node == goal:
                for node in path:
                    neighbor = self.map.cities[node][0]
                    distance = neighbor[1]
                    self.path_cost += distance
                return "Path: " + " -> ".join(path), self.path_cost, self.total_expanded, self.total_visited, self.frontier_size
            if node not in visited:
                visited.append(node)
                self.total_visited += 1
                for neighbor, _ in self.map.get_neighbors(node):
                    frontier.append((neighbor, path + [neighbor]))
                    self.total_expanded += 1
            self.frontier_size = len(frontier)
        return None

    def ucs(self, start, goal):
        visited = []
        frontier = [(0, [start])]
        while frontier:
            frontier.sort()  # Sort frontier based on cost
            cost, path = frontier.pop(0)  # Pop the path with the lowest cost
            node = path[-1]
            if node == goal:
                for node in path:
                    neighbor = self.map.cities[node][0]
                    distance = neighbor[1]
                    self.path_cost += distance
                return "Path: " + " -> ".join(path), self.path_cost, self.total_expanded, self.total_visited, self.frontier_size
            if node not in visited:
                for neighbor, distance in self.map.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    self.total_expanded += 1
                    new_cost = cost + distance
                    frontier.append((new_cost, new_path))
                visited.append(node)
                self.total_visited += 1
            self.frontier_size = len(frontier)
        return None

    def heuristic(self, lat1, lon1, lat2, lon2):
        # https://www.omnicalculator.com/math/euclidean-distance#how-do-i-calculate-the-euclidean-distance
        # https://www.geeksforgeeks.org/euclidean-distance/

        # Convert latitude and longitude from degrees to radians
        lat1_rad = math.radians(float(lat1.split()[0]))
        lon1_rad = math.radians(float(lon1.split()[0]))
        lat2_rad = math.radians(float(lat2.split()[0]))
        lon2_rad = math.radians(float(lon2.split()[0]))

        # Calculate the differences between latitudes and longitudes
        lat_diff = lat2_rad - lat1_rad
        lon_diff = lon2_rad - lon1_rad

        # Calculate the Euclidean distance
        euclidean_distance = math.sqrt(lat_diff ** 2 + lon_diff ** 2)
        return euclidean_distance

    def astar(self, start, goal, start_lat, start_lon, goal_lat, goal_lon):
        visited = []
        frontier = [(0, [start])]
        while frontier:
            # Sort frontier
            frontier.sort(key=lambda x: x[0] + self.heuristic(start_lat, start_lon, goal_lat, goal_lon))
            
            # Pop the path with the lowest f value
            cost, path = frontier.pop(0)
            node = path[-1]
            
            if node == goal:
                # Calculate the actual cost of the path
                actual_cost = sum(self.map.cities[node][0][1] for node in path[:-1])
                return "Path: " + " -> ".join(path), actual_cost, self.total_expanded, self.total_visited, self.frontier_size
            
            if node not in visited:
                for neighbor, distance in self.map.get_neighbors(node):
                    new_path = list(path)
                    new_path.append(neighbor)
                    self.total_expanded += 1
                    # Calculate new cost with the heuristic
                    new_cost = cost + distance
                    frontier.append((new_cost, new_path))
                visited.append(node)
                self.total_visited += 1
            self.frontier_size = len(frontier)
        return None


