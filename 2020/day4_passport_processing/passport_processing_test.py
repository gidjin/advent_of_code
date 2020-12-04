from passport_processing import \
        is_valid_passport, \
        count_valid, \
        parse_passport, \
        parse_multiple, \
        PassportFields
import pytest


@pytest.fixture
def whole_import_file():
    return [
            "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1937 iyr:2017 cid:147 hgt:183cm",
            "",
            "iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884",
            "hcl:#cfa07d byr:1929",
            "",
            "hcl:#ae17e1 iyr:2013",
            "eyr:2024",
            "ecl:brn pid:760753108 byr:1931",
            "hgt:179cm",
            "",
            "hcl:#cfa07d eyr:2025 pid:166559648",
            "iyr:2011 ecl:brn hgt:59in"
            "",
            "ecl:org pid:860033327 eyr:2020 hcl:#fffffd",
            "byr:1907 iyr:2017 cid:147 hgt:183cm",
            ]


@pytest.fixture
def valid_passport():
    passport = dict()
    passport[PassportFields.BIRTH_YEAR] = '1937'
    passport[PassportFields.COUNTRY_ID] = '147'
    passport[PassportFields.EXPIRATION_YEAR] = '2020'
    passport[PassportFields.EYE_COLOR] = 'gry'
    passport[PassportFields.HAIR_COLOR] = '#fffffd'
    passport[PassportFields.HEIGHT] = '183cm'
    passport[PassportFields.ISSUE_YEAR] = '2017'
    passport[PassportFields.PASSPORT_ID] = '860033327'
    return passport


@pytest.fixture
def north_pole_passport():
    passport = dict()
    passport[PassportFields.HAIR_COLOR] = '#ae17e1'
    passport[PassportFields.ISSUE_YEAR] = '2013'
    passport[PassportFields.EXPIRATION_YEAR] = '2024'
    passport[PassportFields.EYE_COLOR] = 'brn'
    passport[PassportFields.PASSPORT_ID] = '760753108'
    passport[PassportFields.BIRTH_YEAR] = '1931'
    passport[PassportFields.HEIGHT] = '179cm'
    return passport


@pytest.fixture
def invalid_passport():
    passport = dict()
    passport[PassportFields.HAIR_COLOR] = '#cfa07d'
    passport[PassportFields.EXPIRATION_YEAR] = '2025'
    passport[PassportFields.PASSPORT_ID] = '166559648'
    passport[PassportFields.ISSUE_YEAR] = '2011'
    passport[PassportFields.EYE_COLOR] = 'brn'
    passport[PassportFields.HEIGHT] = '59in'
    return passport

class TestParseMultipleAndCount:
    def test_count_valid(self, whole_import_file):
        assert count_valid(whole_import_file) == 3

    def test_count_valid_strict(self, whole_import_file):
        assert count_valid(whole_import_file, True) == 2

    def test_parse_multiple(self, whole_import_file, valid_passport, north_pole_passport, invalid_passport):
        parsed = parse_multiple(whole_import_file)
        assert len(parsed) == 4
        assert parsed[0] == valid_passport
        assert parsed[2] == north_pole_passport


class TestIsValidPassport:
    def test_with_valid_passport(self, valid_passport):
        assert is_valid_passport(valid_passport) is True

    def test_with_strict_valid_passport(self, valid_passport):
        assert is_valid_passport(valid_passport, True) is True

    def test_with_bad_birth(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.BIRTH_YEAR: 1919})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.BIRTH_YEAR: 2003})
        assert is_valid_passport(missing, True) is False

    def test_with_bad_iyr(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.ISSUE_YEAR: 2009})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.ISSUE_YEAR: 2021})
        assert is_valid_passport(missing, True) is False

    def test_with_bad_eyr(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.EXPIRATION_YEAR: 2019})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.EXPIRATION_YEAR: 2031})
        assert is_valid_passport(missing, True) is False

    def test_with_bad_hgt(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.HEIGHT: "149cm"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.HEIGHT: "194cm"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.HEIGHT: "58in"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.HEIGHT: "77in"})
        assert is_valid_passport(missing, True) is False

    def test_with_bad_hcl(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.HAIR_COLOR: "#abc"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.HAIR_COLOR: "#abcdefasdf"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.HAIR_COLOR: "#12345M"})
        assert is_valid_passport(missing, True) is False

    def test_with_bad_ecl(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.EYE_COLOR: "org"})
        assert is_valid_passport(missing, True) is False
        for color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            missing.update({PassportFields.EYE_COLOR: color})
            assert is_valid_passport(missing, True) is True

    def test_with_bad_pid(self, valid_passport):
        missing = valid_passport.copy()
        missing.update({PassportFields.PASSPORT_ID: "12345678"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.PASSPORT_ID: "1234567890"})
        assert is_valid_passport(missing, True) is False
        missing.update({PassportFields.PASSPORT_ID: "003467890"})
        assert is_valid_passport(missing, True) is True

    def test_with_missing_data(self, valid_passport):
        for field in PassportFields:
            missing = valid_passport.copy()
            missing.pop(field, None)
            if field == PassportFields.COUNTRY_ID:
                assert is_valid_passport(missing) is True
            else:
                assert is_valid_passport(missing) is False


class TestParsePassport:
    def test_with_valid_passport(self, valid_passport):
        assert parse_passport(
                "ecl:gry pid:860033327 eyr:2020 hcl:#fffffd\nbyr:1937 iyr:2017 cid:147 hgt:183cm"
                ) == valid_passport

    def test_with_north_pole_passport(self, north_pole_passport):
        assert parse_passport(
                "hcl:#ae17e1 iyr:2013\n\reyr:2024\n\recl:brn pid:760753108 byr:1931\n\rhgt:179cm"
                ) == north_pole_passport

    def test_with_invalid_passport(self, invalid_passport):
        assert parse_passport(
                "hcl:#cfa07d eyr:2025 pid:166559648\niyr:2011 ecl:brn hgt:59in"
                ) == invalid_passport
