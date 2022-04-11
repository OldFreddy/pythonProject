def city_country(city, country):
    cityAndCountry = f"{city}, {country}"
    return cityAndCountry.title()

print("\nEntel city and country ")
city = input("CITY: ")
country = input("COUNTRY: ")

print(city_country(city, country))