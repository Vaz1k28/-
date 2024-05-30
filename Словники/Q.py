def find_countries_for_cities(country_data, city_queries):
    city_to_country = {}

    for data in country_data:
        entries = data.split()
        country = entries[0]
        cities = entries[1:]
        for city in cities:
            city_to_country[city] = country

    results = []
    for city in city_queries:
        if city in city_to_country:
            results.append(city_to_country[city])
        else:
            results.append("Unknown")

    return results

def main():
    country_data = [
        "Germany Berlin Hamburg Munich Dortmund",
        "Ukraine Kyiv Lviv Odessa"
    ]
    city_queries = [
        "Odessa",
        "Dortmund",
        "Berlin"
    ]

    results = find_countries_for_cities(country_data, city_queries)

    for result in results:
        print(result)

if __name__ == "__main__":
    main()
