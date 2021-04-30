from flashgeotext.geotext import GeoText
from flashgeotext.lookup import LookupData, load_data_from_file
import pathlib

path = pathlib.Path(__file__).parent.absolute()


class GermanCityExtractor:

    def __init__(self, cities=True, communities=True, states=True):
        self.geotext = GeoText(config={"use_demo_data": False, "case_sensitive": False})
        if cities:
            self.add_cities_to_lookup()
        if communities:
            self.add_communities_to_lookup()
        if states:
            self.add_states_to_lookup()

    def add_cities_to_lookup(self):
        lookup_city = LookupData(name="german_cities", data=load_data_from_file(f"{path}/json/cities.json"))
        self.geotext.add(lookup_city, case_sensitive=False)

    def add_communities_to_lookup(self):
        lookup_community = LookupData(name="german_communities", data=load_data_from_file(f"{path}/json/communities.json"))
        self.geotext.add(lookup_community, case_sensitive=False)

    def add_states_to_lookup(self):
        lookup_state = LookupData(name="german_states", data=load_data_from_file(f"{path}/json/states.json"))
        self.geotext.add(lookup_state, case_sensitive=False)

    def extract_entities(self, msg):
        return self.geotext.extract(input_text=msg, span_info=False)


if __name__ == '__main__':
    text = "München liegt in Bayern."
    extractor = GermanCityExtractor()
    entities = extractor.extract_entities(text)
    print(entities)