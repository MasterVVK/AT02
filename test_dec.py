import pytest

@pytest.fixture
def sample_data():
    return "Sample Data"

@pytest.mark.parametrize("input_str, expected_count", [
    ("aeiouAEIOU", 10),
    ("bcdfg", 0),
    ("Hello World", 3),
    ("PyThOn PrOgRaMmInG", 4),
])
@pytest.mark.usefixtures("sample_data")
@pytest.mark.skipif(condition=False, reason="Пример использования skipif")
@pytest.mark.timeout(2)
def test_combined(input_str, expected_count, sample_data):
    from main import count_vowels
    assert count_vowels(input_str) == expected_count
    assert sample_data == "Sample Data"
