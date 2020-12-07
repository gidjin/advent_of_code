from custom_customs import unique_group_list, \
        parse_groups, \
        calculate_total, \
        calculate_total_part2, \
        shared_answer_list
import pytest


@pytest.fixture
def simple_group():
    return "abcx abcy abcz"


@pytest.fixture
def simple_groups():
    return [
            "abc",
            "",
            "a",
            "b",
            "c",
            "",
            "ab",
            "ac",
            "",
            "a",
            "a",
            "a",
            "a",
            "",
            "b",
            ]


class TestUniqueGroup:
    def test_simple_samples(self, simple_group):
        assert unique_group_list(simple_group) == ["a", "b", "c", "x", "y", "z"]
        assert len(unique_group_list(simple_group)) == 6

    def test_return_shared(self, simple_group):
        assert shared_answer_list(simple_group) == ["a", "b", "c"]
        assert len(shared_answer_list(simple_group)) == 3


class TestParseGroups:
    def test_simple_samples(self, simple_groups):
        assert parse_groups(simple_groups) == ["abc", "a b c", "ab ac", "a a a a", "b"]


class TestCalcTotal:
    def test_simple_samples(self, simple_groups):
        assert calculate_total(simple_groups) == 11

    def test_part_2_simple_samples(self, simple_groups):
        assert calculate_total_part2(simple_groups) == 6
