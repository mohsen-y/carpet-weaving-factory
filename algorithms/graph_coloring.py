from typing import Dict, List, Tuple

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
