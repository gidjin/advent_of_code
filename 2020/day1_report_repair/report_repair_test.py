import report_repair
import pytest


@pytest.fixture
def basic_data():
    return [
            1721, 979, 366, 299, 675, 1456
            ]


@pytest.fixture
def answer_not_first_data():
    return [
            123, 1721, 979, 366, 299, 675, 1456
            ]


@pytest.fixture
def deep_data():
    return [
            1, 2, 3, 4, 5, 6, 123, 1721, 979, 366, 299, 675, 1456
            ]


@pytest.fixture
def deep_mixed_data():
    return [
            1, 2, 3, 4, 5, 6, 123, 1721, 979, 7, 8, 366, 299, 675, 1456
            ]


class TestFindPair:
    def test_finds_a_pair(self, basic_data):
        assert report_repair.find_pair_2020(basic_data) == (1721, 299), \
                "finds two that add up to 2020"

    def test_finds_a_pair_not_first(self, answer_not_first_data):
        assert report_repair.find_pair_2020(answer_not_first_data) == (
                    1721, 299
                ), "finds a pair not at start"

    def test_finds_a_pair_is_deep(self, deep_data):
        assert report_repair.find_pair_2020(deep_data) == (1721, 299), \
                "finds a pair is deep"


class TestFindTriplets:
    def test_find_a_triplet_not_first(self, basic_data):
        assert report_repair.find_triple_2020(basic_data) == (979, 366, 675), \
                "find 3 again"

    def test_finds_a_trip_is_deep(self, deep_data):
        assert report_repair.find_triple_2020(deep_data) == (979, 366, 675), \
                "finds a trip is deep"

    def test_finds_a_trip_is_middle(self, deep_mixed_data):
        assert report_repair.find_triple_2020(deep_mixed_data) == (
                    979, 366, 675
                ), \
                "finds a trip is middle"


class TestCalculateAnswer:
    def test_sample(self, basic_data):
        assert report_repair.calculate_answer(basic_data) == 514579, \
                "found the issue"

    def test_part_two(self, basic_data):
        assert report_repair.calculate_answer_two(basic_data) == 241861950, \
                "found the issue"
