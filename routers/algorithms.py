from algorithms.dijkstra_shortest_paths import dijkstra_shortest_paths
from algorithms.maximum_carpets import buy_maximum_carpets
from algorithms.graph_coloring import graph_coloring
from fastapi import APIRouter
from typing import Dict, List
from schemas import schemas
import json, copy, os

router = APIRouter(prefix="/api", tags=["Algorithms"])

@router.get(
    path="/carpets",
    response_model=List[schemas.Carpet],
)
def get_list_of_carpets():
    return json.load(
        open(file=os.path.join("database", "carpets.json"), mode="r")
    )


@router.post(
    path="/assign-colors",
    response_model=schemas.ColoredAreas,
)
def assign_colors_to_areas(
    adjacency_list: Dict
):
    colored_areas, min_colors = graph_coloring(
        graph=adjacency_list
    )

    return schemas.ColoredAreas(
        colored_areas=colored_areas,
        min_colors=min_colors,
    )


@router.post(
    path="/purchase-carpets",
    response_model=List[schemas.Carpet],
)
def purchase_maximum_number_of_carpets(
    budget: int
):
    carpets = json.load(
        open(file=os.path.join("database", "carpets.json"), mode="r")
    )

    return buy_maximum_carpets(
        carpets=carpets,
        budget=budget,
    )


@router.post(
    path="/nearest-branch",
    response_model=schemas.Route,
)
def find_nearest_factory_branch(
    start_point: str
):
    coordinates = json.load(
        open(file=os.path.join("database", "coordinates.json"), mode="r")
    )
    city_map = coordinates["city_map"]
    branches = coordinates["branches"]

    if start_point in branches:
        return schemas.Route(
            start_point=start_point,
            destination=start_point,
            route=start_point,
            distance=0,
        )

    shortest_paths = dijkstra_shortest_paths(
        graph=city_map,
        start_node=start_point,
        target_nodes=copy.deepcopy(branches),
    )

    branch_with_shortest_distance = branches[0]
    if len(branches) > 1:
        for branch in branches[1:]:
            if shortest_paths[branch]["distance"]\
                < shortest_paths[branch_with_shortest_distance]["distance"]:
                branch_with_shortest_distance = branch

    return schemas.Route(
        start_point=start_point,
        destination=branch_with_shortest_distance,
        route=" -> ".join(
            shortest_paths[branch_with_shortest_distance]["path"]
        ),
        distance=shortest_paths[branch_with_shortest_distance]["distance"],
    )
