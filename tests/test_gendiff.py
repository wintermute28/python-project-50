from gendiff import generate_diff


def test_generate_diff():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result