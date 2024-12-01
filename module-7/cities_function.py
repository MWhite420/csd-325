def city_country(city, country, population=None, language=None):
    if population and language:
        return f"{city}, {country}, {population}, {language}"
    
    elif population:
        return f"{city}, {country}, {population}"
    
    elif language:
        return f"{city}, {country}, {language}"

    else:
        return f"{city}, {country}"
# Call the function with different values
print(city_country("Santiago", "Chile" ))
print(city_country("New York", "USA", "19,570,000"))
print(city_country("Tokyo", "Japan", "14,190,000", "Japanese"))