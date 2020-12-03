from toboggan_trajectory import \
        multiply_all, \
        is_tree, \
        count_trees, \
        count_right3_down1_trees
import pytest


@pytest.fixture
def basic_data():
    return [
            "..##.......",
            "#...#...#..",
            ".#....#..#.",
            "..#.#...#.#",
            ".#...##..#.",
            "..#.##.....",
            ".#.#.#....#",
            ".#........#",
            "#.##...#...",
            "#...##....#",
            ".#..#...#.#",
            ]


class TestIsTree:
    def test_returns_true_for_tree(self):
        assert is_tree("#") is True

    def test_returns_false_for_open(self):
        assert is_tree(".") is False


class TestMultiplyAll:
    def test(self):
        assert multiply_all([2, 7, 3, 4, 2]) == 336


class TestCountTrees:
    def test(self, basic_data):
        assert count_trees(basic_data, 1, 1) == 2
        assert count_trees(basic_data, 3, 1) == 7
        assert count_trees(basic_data, 5, 1) == 3
        assert count_trees(basic_data, 7, 1) == 4
        assert count_trees(basic_data, 1, 2) == 2


class TestCountRight3Down1Trees:
    def test_returns_count(self, basic_data):
        assert count_right3_down1_trees(basic_data) == 7
