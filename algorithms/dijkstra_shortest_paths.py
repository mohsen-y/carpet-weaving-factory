from typing import Dict, List, Literal, Union
import heapq

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

    return {}
    return shortest_paths
