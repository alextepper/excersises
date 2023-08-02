import random

import requests
import psycopg2


class Country:

    def __init__(self, name, capital, flag, subregion, population):
        self.name = name
        self.capital = capital
        self.flag = flag
        self.subregion = subregion
        self.population = population


    def __str__(self):
        return f"{self.capital} is a capital of {self.name}"
    def add_to_db(self):
        connection = psycopg2.connect(host='localhost', user='postgres', password='password', dbname='countries')
        try:
            with connection:
                with connection.cursor() as curs:
                    query = f"""insert into countries(country_name, capital, country_flag, subregion, population) values('{self.name}', '{self.capital}', '{self.flag}', '{self.subregion}', {self.population})"""
                    curs.execute(query)
        except Exception as err:
            print(err)


def get_list_of_countries():
    url = "https://restcountries.com/v3.1/all"
    response = requests.get(url)
    if response.status_code == 200:
        countries = response.json()
        list_of_countries = []
        for country in countries:
            name = country['name']['common']
            capital = country['capital'][0] if 'capital' in country and country['capital'] else 'N/A'
            flag = country['flags']['svg']
            subregion = country['subregion'][0] if 'subregion' in country and country['subregion'] else 'N/A'
            population = country['population']
            list_of_countries.append(Country(name, capital, flag, subregion, population))
        return list_of_countries
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")


country_list = get_list_of_countries()

for _ in range(10):
    random.choice(country_list).add_to_db()
