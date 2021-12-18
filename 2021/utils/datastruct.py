import heapq
import itertools
import networkx
from typing import List

from types import Coord, Points


def largest(l: List[any], n: int) -> List[any]:
    """Finds the n largest elements in a list."""
    return heapq.nlargest(n, l)


def smallest(l: List[any], n: int) -> List[any]:
    """Finds the n smallest elements in a list."""
    return heapq.nsmallest(n, l)


class Grid:
    def __init__(self, points: Points, rows: int, cols: int) -> None:
        self.points = points
        self.rows = rows
        self.columns = cols
        self.graph = self.to_graph()

    def get_neighbors(point: tuple, include_diagonals: bool = False):
        def _add_vector(position: tuple, vector: tuple):
            return tuple(x + y for x, y in zip(position, vector))

        dims = len(point)
        zero = tuple(0 for _ in range(dims))
        for vector in itertools.product([-1, 0, 1], repeat=dims):
            if vector != zero and (include_diagonals or sum(vector) == 1):
                yield _add_vector(point, vector)

    def to_graph(self) -> networkx.Graph:
        graph = networkx.Graph()
        for pt, val in self.points.items():
            graph.add_node(pt, value=val)
        for point in self.points:
            for neighbor in self.get_neighbors(point):
                if neighbor in self.points:
                    graph.add_edge(point, neighbor)

        return graph

    def __getitem__(self, point: Coord):
        return self.points[point]

    def __setitem__(self, point: Coord, value):
        self.points[point] = value

    def __iter__(self):
        for point in self.points:
            yield point

    def __len__(self):
        return len(self.points)

    def items(self):
        for point, value in self.points.items():
            yield point, value

    def neighbors(self, point: Coord):
        for neighbor in self.graph.neighbors(point):
            yield neighbor


class DiagonalGrid(Grid):
    def to_graph(self):
        graph = networkx.Graph()
        for point, value in self.points.items():
            graph.add_node(point, value=value)

        for point in self.points:
            for neighbor in self.get_neighbors(point, include_diagonals=True):
                if neighbor in self.points:
                    graph.add_edge(point, neighbor)

        return graph
