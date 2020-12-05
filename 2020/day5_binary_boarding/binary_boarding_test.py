from binary_boarding import \
        code_to_seat_location, calculate_seat_id, find_highest_seat, find_missing_seat
import pytest


@pytest.fixture
def boarding_passes():
    return [
            ("FBFBBFFRLR", (44, 5), 357),
            ("BFFFBBFRRR", (70, 7), 567),
            ("FFFBBBFRRR", (14, 7), 119),
            ("BBFFBBFRLL", (102, 4), 820)
            ]


@pytest.fixture
def seat_ids():
    return [
            8,
            0,
            2,
            4,
            3,
            6,
            9,
            7,
            11
            ]


class TestFindMissingSeat:
    def test_samples(sefl, seat_ids):
        assert find_missing_seat(seat_ids) == 5


class TestFindHighestSeat:
    def test_samples(self, boarding_passes):
        boarding_pass_codes = map(lambda b: b[0], boarding_passes)
        assert find_highest_seat(list(boarding_pass_codes)) == 820


class TestCodeToSeatLocation:
    def test_samples(self, boarding_passes):
        for bp in boarding_passes:
            assert code_to_seat_location(bp[0]) == bp[1], "Seat Code to Loc"


class TestSeatID:
    def test_samples(self, boarding_passes):
        for bp in boarding_passes:
            assert calculate_seat_id(bp[1]) == bp[2], "Seat ID"
