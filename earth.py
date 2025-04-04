def earth():

    country1 = "Bangladesh"
    country2 = "Barbados"

    if country1 < country2:  # Correct way to check which comes first in alphabetical order
        x_first = True
        y_first = False
    else:
        x_first = False
        y_first = True

    print(f"The result of {country1} comes first in the dictionary than {country2} is {x_first}.")
    print(f"The result of {country2} comes first in the dictionary than {country1} is {y_first}.")
