import pytest

from extractor.geotext import GermanCityExtractor


def test_pool():
    geotext = GermanCityExtractor()
    print("d")
    assert geotext.pool["german_cities"]
    assert geotext.pool["german_communities"]
    assert geotext.pool["german_states"]

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"