def compare_countries(country1, country2):
    x_first = country1 < country2  # True if country1 comes first alphabetically
    y_first = country2 < country1  # True if country2 comes first alphabetically

    print(f"The result of {country1} comes first in the dictionary than {country2} is {x_first}.")
    print(f"The result of {country2} comes first in the dictionary than {country1} is {y_first}.")

# Example usage
compare_countries("Bangladesh", "Barbados")
