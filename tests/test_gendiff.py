from gendiff import generate_diff
from gendiff.stylish import converte
from gendiff.stylish import stylish


def test_generate_diff_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', stylish) == result


def test_generate_diff_yml():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', stylish) == result


def test_generate_diff_yml_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.json', stylish) == result
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', stylish) == result


def test_converte():
    result = 'true'
    assert converte(True) == result
