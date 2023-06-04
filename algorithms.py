from typing import Dict, List, Literal, Union, Tuple
import heapq

def graph_coloring(
    graph: Dict[str, List[str]]
) -> Tuple[Dict[str, int], int]:
    """
    Time Complexity: O(V log V + E)
    Space Complexity: O(V)
    """
    colored_areas = {}  # Dictionary to store the assigned colors for each area

    # Sort the areas in descending order of their degrees (number of adjacent areas)
    sorted_areas = sorted(
        graph.keys(), key=lambda area: len(graph[area]), reverse=True
    )

    # Assign colors to the areas
    for area in sorted_areas:
        used_colors = set()
        for neighbor in graph[area]:
            if neighbor in colored_areas:
                used_colors.add(colored_areas[neighbor])

        # Find the smallest unused color for the current area
        color = 0
        while color in used_colors:
            color += 1

        colored_areas[area] = color

    # Calculate the minimum number of colors required
    min_colors = max(colored_areas.values()) + 1

    return (colored_areas, min_colors)


def buy_maximum_carpets(
    carpets: List[Dict[str, Union[str, int]]],
    budget: int,
) -> List[Dict[str, Union[str, int]]]:
    """
    Time Complexity: O(num_carpets * budget)
    Space Complexity: O((num_carpets + 1) * (budget + 1))
    """
    num_carpets = len(carpets)
    # Create a table to store the maximum number of carpets for the given budget
    table = [[0] * (budget + 1) for _ in range(num_carpets + 1)]

    for i in range(1, num_carpets + 1):
        for j in range(1, budget + 1):
            # If the current carpet's price is less than or equal to the current budget,
            # we have two choices: include the carpet or exclude it
            if carpets[i - 1]['price'] <= j:
                # Calculate the maximum number of carpets by considering both choices
                table[i][j] = max(table[i - 1][j], table[i - 1][j - carpets[i - 1]['price']] + 1)
            else:
                # If the current carpet's price is greater than the budget, exclude the carpet
                table[i][j] = table[i - 1][j]

    # Trace back the table to find the carpets that were selected
    selected_carpets = []
    i, j = num_carpets, budget
    while i > 0 and j > 0:
        if table[i][j] != table[i - 1][j]:
            selected_carpets.append(carpets[i - 1])
            j -= carpets[i - 1]['price']
        i -= 1

    return selected_carpets


def dijkstra_shortest_paths(
    graph: Dict[str, Dict[str, int]],
    start_node: str,
    target_nodes: List[str],
) -> Dict[
    str, Dict[Literal["distance", "path"], Union[int, List[str]]]
]:
    """
    Time Complexity: O((V + E) * log V)
    Space Complexity: O(V)
    """
    distances = {node: float("inf") for node in graph}
    distances[start_node] = 0
    paths = {start_node: [start_node]}

    # Use a min-heap to track nodes with minimum distance
    heap = [(0, start_node)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        # Stop the algorithm if all target nodes have been found
        if not target_nodes:
            break

        # Explore neighboring nodes
        for neighbor, edge_weight in graph[current_node].items():
            distance = current_distance + edge_weight

            # Update distance and path if a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                paths[neighbor] = paths[current_node] + [neighbor]
                heapq.heappush(heap, (distance, neighbor))

                # Check if the neighbor is a target node
                if neighbor in target_nodes:
                    target_nodes.remove(neighbor)

    shortest_paths = {
        node: {
            "distance": distances[node],
            "path": paths[node],
        } for node in paths if node not in target_nodes
    }

    return shortest_paths
