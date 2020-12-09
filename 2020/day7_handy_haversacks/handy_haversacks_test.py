from handy_haversacks import parse_rule, count_possibilities, count_total_bags
import pytest


@pytest.fixture
def sample_data():
    return [
            "light red bags contain 1 bright white bag, 2 muted yellow bags.",
            "dark orange bags contain 3 bright white bags, 4 muted yellow bags.",
            "bright white bags contain 1 shiny gold bag.",
            "muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.",
            "shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.",
            "dark olive bags contain 3 faded blue bags, 4 dotted black bags.",
            "vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.",
            "faded blue bags contain no other bags.",
            "dotted black bags contain no other bags."
            ]


@pytest.fixture
def ridiculous_data():
    return [
            "shiny gold bags contain 2 dark red bags.",
            "dark red bags contain 2 dark orange bags.",
            "dark orange bags contain 2 dark yellow bags.",
            "dark yellow bags contain 2 dark green bags.",
            "dark green bags contain 2 dark blue bags.",
            "dark blue bags contain 2 dark violet bags.",
            "dark violet bags contain no other bags.",
            ]


class TestParse:
    def test_parse_one(self, sample_data):
        assert parse_rule(sample_data[0]) == ('light red', ['bright white', 'muted yellow'])
        assert parse_rule(sample_data[2]) == ('bright white', ['shiny gold'])
        assert parse_rule(sample_data[7]) == ('faded blue', [])

    def test_parse_with_count(self, sample_data):
        assert parse_rule(sample_data[0], True) == ('light red', [('bright white', 1), ('muted yellow', 2)])
        assert parse_rule(sample_data[2], True) == ('bright white', [('shiny gold', 1)])
        assert parse_rule(sample_data[7], True) == ('faded blue', [])


class TestCount:
    def test_count_possibilities(self, sample_data):
        assert count_possibilities(sample_data, 'shiny gold') == 4

    def test_count_total_bags(self, sample_data, ridiculous_data):
        assert count_total_bags(sample_data, 'shiny gold') == 32
        assert count_total_bags(ridiculous_data, 'dark blue') == 2
        assert count_total_bags(ridiculous_data, 'dark green') == 2 + 2 * 2
        assert count_total_bags(ridiculous_data, 'dark yellow') == 2 + 2 * 6
        assert count_total_bags(ridiculous_data, 'dark orange') == 2 + 2 * 14
        assert count_total_bags(ridiculous_data, 'dark red') == 2 + 2 * 30
        assert count_total_bags(ridiculous_data, 'shiny gold') == 126

