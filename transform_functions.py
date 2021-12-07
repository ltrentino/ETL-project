# Function to import country code list
import pycountry


def convert_country_code(main_df):
    input_countries = main_df["country"]

    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    codes = [countries.get(country, 'Unknown code') for country in input_countries]

    return codes