# Name: Patrick Punch
# Date: 4/25/2024
# -- Due to extenuating circumstances, my completion of the project was delayed until today. My work schedule and other coursework prevented me from completing any work on this assignment on 4/23 and 4/24.
# Collaborators: Daniel Lounsbury


4. The number of times it found the optimal solution (optimal here is measured as “found the best solution out of the four search algorithms)
- When running the test city pairs, the A* algorithm always found the optimal solution. The A* algorithm has the lowest average score at 1097 with the provided data. The next best algorithm is BFS and UCS, with an average of 1373/1377. The biggest differene influencing these algorithms is the weight of the heuristic in the A* algorithm. The UCS algorithm performs on average surprisingly similarly to the BFS Algorithm, which approach the solution with different logic. The worst performing algorithm is DLS, with an average cost of 2538. 
bfs # of optimal solutions:  0/9
dls # of optimal solutions:  0/9
ucs # of optimal solutions:  0/9
astar # of optimal solutions:  9/9
Total Scores:   BCS:  12360 DLS:  22844 UCS:  12400 A*:  9875
Average Scores: BCS:  1373 DLS:  2538 UCS:  1377 A*:  1097
