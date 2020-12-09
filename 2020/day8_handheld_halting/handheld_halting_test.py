from handheld_halting import find_repeat_instruction, parse_command, Ops, parse_argument, fix_repeat_instruction
import pytest


@pytest.fixture
def sample_data():
    return [
            "nop +0",
            "acc +1",
            "jmp +4",
            "acc +3",
            "jmp -3",
            "acc -99",
            "acc +1",
            "jmp -4",
            "acc +6",
            ]


class TestFindRepeat:
    def test_sample_data(self, sample_data):
        # assert find_repeat_instruction(sample_data) == 5
        assert fix_repeat_instruction(sample_data) == 8


class TestParsers:
    def test_sample_data(self, sample_data):
        assert parse_command(sample_data[0]) == Ops.NOP
        assert parse_command(sample_data[1]) == Ops.ACC
        assert parse_command(sample_data[2]) == Ops.JMP

    def test_parse_argument(self, sample_data):
        assert parse_argument(sample_data[0]) == 0
        assert parse_argument(sample_data[1]) == 1
        assert parse_argument(sample_data[4]) == -3
        assert parse_argument(sample_data[5]) == -99
