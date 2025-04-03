def compare_countries(country1, country2):
    if country1 < country2:
        print(f"The result of {country1} comes first in the dictionary than {country2} is True.")
        print(f"The result of {country2} comes first in the dictionary than {country1} is False.")
    else:
        print(f"The result of {country1} comes first in the dictionary than {country2} is False.")
        print(f"The result of {country2} comes first in the dictionary than {country1} is True.")

# Example usage
compare_countries("Bangladesh", "Barbados")
