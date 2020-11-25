import pytest

from exercise.maze import Maze
from exercise.search import Search


# No need to change these tests.
class TestExercise2_4_4_2:

    def test_greedy_path(self):
        a_maze = Maze(10, 10, (100, 100))
        greedy = Search(a_maze)
        a_maze.generate_room()
        a_maze.set_target(a_maze.grid[3][3])
        greedy.greedy_search()
        assert a_maze.target.distance == 6, "Greedy should find in the room from (0,0) to (3,3) a path of length 6"

    def test_greedy_none(self):
        a_maze = Maze(10, 10, (100, 100))
        a_maze.generate_room()
        a_maze.set_target(a_maze.grid[3][3])
        for cell in a_maze.possible_neighbours(a_maze.target):  # remove all neighbours            ...
            a_maze.del_link(a_maze.target, cell)
        greedy = Search(a_maze)
        greedy.greedy_search()
        assert a_maze.grid[1][1].parent is not None, "The search should pass cell (1,1)."
        assert a_maze.grid[1][1].score == 4, "The score of (1,1) should be 4"
        assert a_maze.target.distance is None, "Greedy should not find any path"


class TestExercise2_4_4_3:

    def test_astar_path(self):
        a_maze = Maze(10, 10, (100, 100))
        astar = Search(a_maze)
        a_maze.generate_room()
        a_maze.set_target(a_maze.grid[3][3])
        astar.a_star_search()
        assert a_maze.target.distance == 6, "Greedy should find in the room from (0,0) to (3,3) a path of length 6"

    def test_star_none(self):
        a_maze = Maze(10, 10, (100, 100))
        a_maze.generate_room()
        a_maze.set_target(a_maze.grid[3][3])
        for cell in a_maze.possible_neighbours(a_maze.target):  # remove all neighbours            ...
            a_maze.del_link(a_maze.target, cell)
        astar = Search(a_maze)
        astar.a_star_search()
        assert a_maze.grid[1][1].parent is not None, "The search should pass cell (1,1)."
        assert a_maze.grid[1][1].score == 6, "The score of (1,1) should be 6"
        assert a_maze.target.distance is None, "Greedy should not find any path"
