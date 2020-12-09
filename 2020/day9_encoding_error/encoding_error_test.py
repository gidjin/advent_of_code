from encoding_error import is_valid, find_first_invalid, find_list_adding_to, encryption_weakness
import pytest


@pytest.fixture
def sample_data():
    return [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576,
            ]


@pytest.fixture
def long_data():
    return [
            2,
            3,
            4,
            5,
            6,
            7,
            8,
            9,
            10,
            11,
            12,
            13,
            1,
            14,
            15,
            16,
            17,
            18,
            19,
            20,
            21,
            22,
            23,
            24,
            25,
            26,
            49,
            100,
            50,
            ]


class TestIsValid:
    def test_sample_data(self, sample_data):
        assert is_valid(sample_data[0:4], sample_data[5]) == True
        assert is_valid(sample_data[1:5], sample_data[6]) == True
        assert is_valid(sample_data[9:13], sample_data[14]) == False


class TestFind:
    def test_sample_data(self, sample_data):
        assert find_first_invalid(sample_data, 5) == 127
        assert find_list_adding_to(sample_data, 127) == [15, 25, 47, 40]
        assert encryption_weakness(sample_data, 127) == 62

    def test_long_data(self, long_data):
        assert find_first_invalid(long_data) == 100
