# Patrick Punch
import map
import search
import argparse

def Main():

    def parse_arguments():
        parser = argparse.ArgumentParser()
        parser.add_argument("-A", "--start-city", help="Start city")
        parser.add_argument("-B", "--end-city", help="Goal city")
        parser.add_argument("-m", "--map-file", help="Map file")
        parser.add_argument("-s", "--search-algorithm", default="bfs", help="Search Algorithm")
        return parser.parse_args()

    args = parse_arguments()
    start_city = args.start_city
    goal_city = args.end_city
    map_file = args.map_file
    search_algorithm = args.search_algorithm

    state_map = map.Map()
    state_map.create_map(map_file)
    # state_map.display_map()
    search_map = search.Search(state_map)


    if not start_city and not goal_city:
        test_cities = [
            ("brest", "nice"),
            ("montpellier", "calais"),
            ("strasbourg", "bordeaux"),
            ("paris", "grenoble"),
            ("grenoble", "paris"),
            ("brest", "grenoble"),
            ("grenoble", "brest"),
            ("nice", "nantes"),
            ("caen", "strasbourg")
        ]
        optimal_solution_counts = {'bfs': 0, 'dls': 0, 'ucs': 0, 'astar': 0}
        temp_scores = [0, 0, 0, 0]
        count = 0
        bcs_total = 0
        dls_total = 0
        ucs_total = 0
        astar_total = 0
        for pair in test_cities:
            start_city, goal_city = pair
            for search_algorithm in ["bfs", "dls", "ucs", "astar"]:
                    if search_algorithm == "bfs":
                        temp_scores[0] = 0
                        bfs_test = search.Search(state_map)
                        result = bfs_test.bfs(start_city, goal_city)
                        path, cost, explored, expanded, maintained = result
                        temp_scores[0] += cost
                        bcs_total += cost
                        with open("solutions.txt", "a") as f:
                            f.write(f"Start City: {start_city}, Goal City: {goal_city}\n")
                            f.write(f"Search Algorithm: {search_algorithm}\n")
                            f.write(f"Path: {path}\n")
                            f.write(f"Cost: {cost}\n")
                            f.write(f"Nodes Explored: {explored}\n")
                            f.write(f"Nodes Expanded: {expanded}\n")
                            f.write(f"Nodes Maintained: {maintained}\n")
                            f.write("\n")
                    elif search_algorithm == "dls":
                        temp_scores[1] = 0
                        dls_test = search.Search(state_map)
                        result = dls_test.dls(start_city, goal_city, 1)
                        path, cost, explored, expanded, maintained = result
                        temp_scores[1] += cost
                        dls_total += cost
                        with open("solutions.txt", "a") as f:
                            f.write(f"Start City: {start_city}, Goal City: {goal_city}\n")
                            f.write(f"Search Algorithm: {search_algorithm}\n")
                            f.write(f"Path: {path}\n")
                            f.write(f"Cost: {cost}\n")
                            f.write(f"Nodes Explored: {explored}\n")
                            f.write(f"Nodes Expanded: {expanded}\n")
                            f.write(f"Nodes Maintained: {maintained}\n")
                            f.write("\n")
                    elif search_algorithm == "ucs":
                        temp_scores[2] = 0
                        ucs_test = search.Search(state_map)
                        result = ucs_test.ucs(start_city, goal_city)
                        path, cost, explored, expanded, maintained = result
                        temp_scores[2] += cost
                        ucs_total += cost
                        with open("solutions.txt", "a") as f:
                            f.write(f"Start City: {start_city}, Goal City: {goal_city}\n")
                            f.write(f"Search Algorithm: {search_algorithm}\n")
                            f.write(f"Path: {path}\n")
                            f.write(f"Cost: {cost}\n")
                            f.write(f"Nodes Explored: {explored}\n")
                            f.write(f"Nodes Expanded: {expanded}\n")
                            f.write(f"Nodes Maintained: {maintained}\n")
                            f.write("\n")
                    elif search_algorithm == "astar":
                        temp_scores[3] = 0
                        start_latitude = state_map.city_location[start_city][0]
                        start_longitude = state_map.city_location[start_city][1]
                        goal_latitude = state_map.city_location[goal_city][0]
                        goal_longitude = state_map.city_location[goal_city][1]
                        astar_test = search.Search(state_map)
                        result = astar_test.astar(start_city, goal_city, start_latitude, start_longitude,goal_latitude, goal_longitude)
                        path, cost, explored, expanded, maintained = result
                        temp_scores[3] += cost
                        astar_total += cost
                        with open("solutions.txt", "a") as f:
                            f.write(f"Start City: {start_city}, Goal City: {goal_city}\n")
                            f.write(f"Search Algorithm: {search_algorithm}\n")
                            f.write(f"Path: {path}\n")
                            f.write(f"Cost: {cost}\n")
                            f.write(f"Nodes Explored: {explored}\n")
                            f.write(f"Nodes Expanded: {expanded}\n")
                            f.write(f"Nodes Maintained: {maintained}\n")
                            f.write("\n")
            lowest_score = min(temp_scores)
            if lowest_score == temp_scores[0]:
                optimal_solution_counts['bfs'] += 1
            if lowest_score == temp_scores[1]:
                optimal_solution_counts['dls'] += 1
            if lowest_score == temp_scores[2]:
                optimal_solution_counts['ucs'] += 1
            if lowest_score == temp_scores[3]:
                optimal_solution_counts['astar'] += 1
            count += 1
    else:
        if search_algorithm == 'bfs':
            result = search_map.bfs(start_city, goal_city)
        if search_algorithm == 'dls':
            result = search_map.dls(start_city, goal_city, 1)
        if search_algorithm == 'ucs':
            result = search_map.ucs(start_city, goal_city)
        if search_algorithm == 'astar':
            start_latitude = state_map.city_location[start_city][0]
            start_longitude = state_map.city_location[start_city][1]
            goal_latitude = state_map.city_location[goal_city][0]
            goal_longitude = state_map.city_location[goal_city][1]
            result = search_map.astar(start_city, goal_city, start_latitude, start_longitude,goal_latitude, goal_longitude)

if __name__ == "__main__":
    Main()