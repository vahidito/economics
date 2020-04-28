countries = ('United States', 'Iran', 'India', 'France')
cities = ('NewYork', 'Tehran', 'Delhi', 'Paris')

for country, city in zip(countries, cities):
    print(f'The capital of {country} is {city}')
