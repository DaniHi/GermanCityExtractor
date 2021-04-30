from unittest import TestCase
from extractor.geotext import GermanCityExtractor


class TestGermanCityExtractor(TestCase):
    def test_add_cities_to_lookup(self):
        extractor = GermanCityExtractor(True, False, False)
        geotext = extractor.geotext
        self.assertTrue("german_cities" in geotext.pool)
        self.assertFalse("german_communities" in geotext.pool)
        self.assertFalse("german_states" in geotext.pool)

    def test_add_communities_to_lookup(self):
        extractor = GermanCityExtractor(False, True, False)
        geotext = extractor.geotext
        self.assertFalse("german_cities" in geotext.pool)
        self.assertTrue("german_communities" in geotext.pool)
        self.assertFalse("german_states" in geotext.pool)

    def test_add_states_to_lookup(self):
        extractor = GermanCityExtractor(False, False, True)
        geotext = extractor.geotext
        self.assertFalse("german_cities" in geotext.pool)
        self.assertFalse("german_communities" in geotext.pool)
        self.assertTrue("german_states" in geotext.pool)

    def test_extract_entities(self):
        text = "München liegt in Bayern."
        extractor = GermanCityExtractor()
        entities = extractor.extract_entities(text)
        print(entities)
        self.assertTrue("München" in entities["german_cities"])
        self.assertTrue("Bayern" in entities["german_states"])

    def test_all(self):
        extractor = GermanCityExtractor()
        geotext = extractor.geotext
        print(geotext.pool["german_cities"])
        assert geotext.pool["german_cities"]
        assert geotext.pool["german_communities"]
        assert geotext.pool["german_states"]
