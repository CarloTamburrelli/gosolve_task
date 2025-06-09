import pytest
from app.service import SearchService
from config import Config


@pytest.fixture(scope="module")
def search_service():
    return SearchService(Config.DATA_FILE)

def test_search_returns_none_for_string_input(search_service):
    with pytest.raises(TypeError):
        search_service.search("abc")

def test_search_finds_exact_match_in_hash(search_service):
    result = search_service.search(0)
    assert result is not None
    assert result.index == 0
    assert isinstance(result.value, int)

def test_search_returns_none_for_value_out_of_tolerance(search_service):
    result = search_service.search(100000000000000000000)
    assert result is None
