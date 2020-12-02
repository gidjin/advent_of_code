from password_philosophy import \
        parse_password_data, \
        password_is_valid, \
        real_toboggan_password_is_valid, \
        count_valid_passwords
import pytest


@pytest.fixture
def basic_data():
    return [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc',
            '2-5 d: ddddddddd',
            '1-3 b: cdbfg',
            '1-5 b: cbavbfg',
            ]


@pytest.fixture
def long_data():
    return [
            '12-13 l: lllllllljlplqlll',
            '1-10 k: kkkknqxfszj',
            '14-16 j: jfjnbjmttjvwkjhq',
            '1-5 p: cppspppgpspbvj',
            '10-15 z: zfzzzzzzzmdzznjjzpz',
            '14-20 c: cccvcccccccrcccccpcc',
            ]


class TestParseLine:
    def test_returns_first_int(self, basic_data):
        assert parse_password_data(basic_data[0])[0] == 1, \
                "parses first int"

    def test_returns_second_int(self, basic_data):
        assert parse_password_data(basic_data[0])[1] == 3, \
                "parses second int"

    def test_returns_letter(self, basic_data):
        assert parse_password_data(basic_data[0])[2] == 'a', \
                "parses letter"

    def test_returns_password(self, basic_data):
        assert parse_password_data(basic_data[0])[3] == 'abcde', \
                "parses password"


class TestPasswordIsValid:
    def test_with_valid_password(self, basic_data):
        data = parse_password_data(basic_data[0])
        assert password_is_valid(data) is True, "valid password is true"

    def test_with_invalid_password(self, basic_data):
        data = parse_password_data(basic_data[1])
        assert password_is_valid(data) is False, "invalid password is false"

    def test_with_valid_password_repeats(self, basic_data):
        data = parse_password_data(basic_data[2])
        assert password_is_valid(data) is True, "valid password is true"

    def test_with_invalid_password_repeats_too_much(self, basic_data):
        data = parse_password_data(basic_data[3])
        assert password_is_valid(data) is False, "invalid password is false"


class TestRealTobogganPasswordIsValid:
    def test_with_valid_password(self, basic_data):
        data = parse_password_data(basic_data[0])
        assert real_toboggan_password_is_valid(data) is True, \
            "valid password is true"

    def test_with_invalid_password(self, basic_data):
        for sample in basic_data[1:4]:
            data = parse_password_data(sample)
            assert real_toboggan_password_is_valid(data) is False, \
                f"{sample} invalid password is false"

    def test_with_valid_password_pos2(self, basic_data):
        data = parse_password_data(basic_data[4])
        assert real_toboggan_password_is_valid(data) is True, \
            "valid password is true"

    def test_with_valid_password_pos2_offset(self, basic_data):
        data = parse_password_data(basic_data[5])
        assert real_toboggan_password_is_valid(data) is True, \
            "valid password is true"

    def test_long_data_with_valid(self, long_data):
        for sample in long_data[0:3]:
            data = parse_password_data(sample)
            assert real_toboggan_password_is_valid(data) is True, \
                f"{sample} valid password is true"

    def test_long_data_with_invalid(self, long_data):
        for sample in long_data[4:]:
            data = parse_password_data(sample)
            assert real_toboggan_password_is_valid(data) is False, \
                f"{sample} invalid password is false"


class TestCountValidPasswords:
    def test_count_valid_passwords(self, basic_data):
        assert count_valid_passwords(basic_data, password_is_valid) == 4, \
            "find 4 valid passwords"

    def test_count_valid_passwords_real(self, basic_data):
        assert count_valid_passwords(
                basic_data,
                real_toboggan_password_is_valid
            ) == 3, \
            "find 3 valid passwords"
